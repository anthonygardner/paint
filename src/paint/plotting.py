from pydantic.dataclasses import dataclass

from paint.config import Plot

import plotly.io as pio
import logging


pio.kaleido.scope.mathjax = None


plot = Plot


def plot_all(
    plot: Plot, 
    make_html: bool = True,
    make_pdf: bool = True,
):
    fig = make_subplots(
        rows=plot.n_rows,
        cols=plot.n_cols,
        subplot_titles=plot.titles,
        shared_xaxes=plot.shared_xaxes,
    )

    if make_html:
        fig.write_html(f"")
        logging.info(f"an html file has been generated at: {Directories.RESULTS_HTML}")
    else:
        fig.show()

    if make_pdf:
        pio.write_image(
            fig=fig,
            file=f"",
            format="pdf",
            height=1000,
            width=1000,
        )
        logging.info(f"a pdf file has been generated at: ...")
    else:
        fig.show()

