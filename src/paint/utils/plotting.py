import plotly.io as pio
import logging

pio.kaleido.scope.mathjax = None


def plot_all(
    make_html: bool = True,
    make_pdf: bool = True,
):
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

