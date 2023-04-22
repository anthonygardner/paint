from argparse import PARSER, ArgumentParser
from colorama import Fore, Style
from dataclasses import fields
from pathlib import Path
from typing import List, Union
from pypdf import PdfMerger

import argcomplete
import colorama
import logging
import subprocess
import sys

from paint.config import Files, Directories


# logger settings
colorama.init()

# FORE.RED Style.RESET_ALL

FORMAT = "%(filename)s:%(lineno)s:%(funcName)s() => %(levelname)s: %(message)s"

logger = logging.getLogger(__name__)
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

def parse_command_line() -> ArgumentParser, ArgumentParser:
    parser: ArgumentParser = ArgumentParser()

    # enable autocomplete
    argcomplete.autocomplete(parser)

    return parser, parser.parse_args()

def clean_html_directory() -> None:
    return [f.unlink() for f in Directories.RESULTS_HTML.glob("*.html") if f.is_file()]

def clean_pdf_directory() -> None:
    return [f.unlink() for f in Directories.RESULTS_PDF.glob("*.pdf") if f.is_file()]

def make_pdf_report() -> None:
    # delete previous report
    Files.final_report_pdf_unlink(missing_ok=True)

    pdfs: List[Path] = sorted([pdf for pdf in Directories.RESULTS_PDF.glob("*.pdf")], reverse=True)

    if len(pdfs) == 0:
        logging.error(f"no pdf's found in '{Directories.RESULTS_PDF}'")
    else:
        merger = PdfMerger()

        for pdf in pdfs:
            merger.append(pdf)

        merger.write(Directories.RESULTS_PDF / "final_report.pdf")
        
        merger.close()
        
        logger.info("a pdf report has been generated at {Files.final_report_pdf}")

def cli() -> None:
    # parse command line args
    parser, args = parse_command_line()

    # display help by default
    _fields = [getattr(args, arg), for arg in vars(args)]
    if all(field is False or field is None or field == "" for field in _fields):
        parser.print_help()
    else:
        # clear results directories
        clean_html_directory()
        clean_pdf_directory()

        # collect data
        dfs = []

        # configure custom subplots with dash
        if args.dash != "":
            from dash import ctx, Dash, dcc, html, Input, Output
            from plotly.subplots ipmort make_subplots

            import plotly.graph_objects as go
            import threading
            import webbrowser

            rows, cols = map(int, args.dash.split(sep="x"))

            fig = make_subplot(rows=rows, cols=cols)

            for row in range(rows):
                for col in range(cols):
                    fig.add_trace(go.Scatter(), row=row+1, col=col+1)

            app = Dash(__name__)
            
            server = app.server
            
            app.layout = html.Div([
                html.Div([
                    html.Div(children=[
                        html.Div([
                            html.Label("DataFrame"),
                            dcc.Dropdown(
                                options=[field.name for field in fields(dfs)],
                                id="dataframe",
                            ),
                        ]),

                        html.Div([
                            html.Label("X-axis"),
                            dcc.Dropdown(
                                options=list(),
                                id="subplot-xaxis-data",
                            ),
                        ]),

                        html.Div([
                            html.Label("Y-axis"),
                            dcc.Dropdown(
                                options=list(),
                                id="subplot-yaxis-data",
                            ),
                        ]),
                    ], style={"padding": 10, "flex": 1}),

                    html.Div(children=[
                        html.Div([
                            html.Label("Row"),
                            dcc.Dropdown(
                                options=[row for row in range(1, rows+1)],
                                id="subplot-row",
                            ),
                        ]),

                        html.Div([
                            html.Label("Column"),
                            dcc.Dropdown(
                                options=[col for col in range(1, cols+1)],
                                id="subplot-column",
                            ),
                        ]),
                    ], style={"padding": 10, "flex": 1}),
                ], style={"diplay": "flex", "flex-direction": "row"}),

                html.Button(
                    "Clear Last",
                    id="clear-last-button",
                    n_clicks=0,
                ),

                html.Button(
                    "Clear All",
                    id="clear-all-button",
                    n_clicks=0,
                ),

                dcc.Graph(id="subplots"),
            ])

            @app.callback(
                Output("dataframe", "value"),
                Input("dataframe", "options"),
            )
            def update_dataframe(df):
                return df

            @app.callback(
                Output("subplot-xaxis-data", "options"),
                Output("subplot-yaxis-data", "options"),
                Input("dataframe", "value"),
            )
            def update_xy_dropdown_options(df):
                _df = getattr(dfs, df)
                # TODO(acg): figure out df initialization
                return _df.columns, _df.columns

            @app.callback(
                Output("subplots", "figure"),
                Input("dataframe", "value"),
                Input("subplot-xaxis-data", "value"),
                Input("subplot-yaxis-data", "value"),
                Input("subplot-row", "value"),
                Input("subplot-column", "value"),
                Input("plot-data-button", "n_clicks"),
                Input("clear-last-button", "n_clicks"),
                Input("clear-all-button", "n_clicks"),
            )
            def update_subplots(
                df,
                x_data, y_data,
                row, col,
                plot_data_button_clicks,
                clear_last_button_clicks,
                clear_all_button_clicks,
            ) -> None:
                _df = getattr(dfs, df)
                clear_last_button_clicks = 0
                if "clear-last-button" == ctx.triggered_id:
                    clear_last_button_clicks += 1
                    fig.data = fig.data[:-clear_last_button_clicks]
                    fig.update_yaxes(title_text="", row=row, col=col)
                    return fig
                elif "clear-all-button" == ctx.triggered_id:
                    fig.data = []
                    return fig
                elif "plot-data-button" == ctx.triggered_id:
                    fig.add_trace(
                        go.Scatter(
                            x=df[x_data],
                            y=df[y_data],
                            name=y_data,
                        ), row=row, col=col,
                    )
                    fig.update_xaxes(title=x_data, row=row, col=col)
                    fig.update_yaxes(title=y_data, row=row, col=col)
                    fig.update_layout(showlegend=False, height=1000)
                    return fig
                else:
                    fig.update_layout(height=1000)
                    return fig
            
            # push to browser
            PORT = 5000  # TODO(acg): add to constants.py
            
            def open_browser() -> None:
                webbrowser.open_new(url=f"http://127.0.0.1:{PORT}/")
            
            threading.Timer(1, open_browser()).start()

            app.run_server(debug=False, port=PORT)

            # launch gui
            if args.gui:
                subprocess.run([
                    f"cd {Directories.GUI.as_posix()} && npm run --silent gui",
                    shell=True,
                ])

            # create pdf
            if args.pdf:
                make_pdf_report()


if __name__ == "__main__":
    cli()
