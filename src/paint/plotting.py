from typing import List, Optional

import logging
import matplotlib.pyplot as plt
import numpy as np
import plotly.io as pio

from mpl_toolkits.mplot3d import Axes3D

from paint.config import Directory, Plot


pio.kaleido.scope.mathjax = None


def draw_3d_arrow(
    arrow_location: np.ndarray,
    arrow_vector: np.ndarray,
    head_length: float = 0.3,
    color: Optional[str] = None,
    name: Optional[str] = None,
    ax: Optional[Axes3D] = None,
) -> Axes3D:
    if ax is None:
        ax = plt.gca(projection="3d")
    
    ax.quiver(
        *arrow_location,
        *arrow_vector,
        arrow_length_ratio=head_length / np.linalg.norm(arrow_vector),
        color=color,
    )

    if name is not None:
        ax.text(*(arrow_location + arrow_vector), name)
    
    return ax

def set_xyz_limits(
    left: Optional[float] = None,
    right: Optional[float] = None,
    ax: Optional[Axes3d]= None,
) -> Axes3D:
    if ax is None:
        ax = plt.gca(projection="3d")
    
    ax.set_xlim3d(left, right)
    ax.set_ylim3d(left, right)
    ax.set_zlim3d(left, right)

    return ax

def set_xyz_ticks(
    ticks: List[float],
    ax: Optional[Axes3D] = None,
) -> Axes3D:
    if ax is None:
        ax = plt.gca(projection="3d")

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_zticks(ticks)

    return ax


class ReferenceFrame:
    def __init__(
        self,
        origin: np.ndarray,
        x_axis: np.ndarray,
        y_axis: np.ndarray,
        z_axis: np.ndarray,
        name: str,
    ) -> None:
        self.origin = origin
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.z_axis = z_axis
        self.name = name

    def draw_3d(
        self,
        head_length: float = 0.3,
        ax: Optional[Axes3D] = None,
    ) -> Axes3D:
        if ax is None:
            ax = plt.gca(projection="3d")

        ax.text(*self.origin + 0.5, f"{self.name}")


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
        logging.info(f"An html file has been generated: {Directory.RESULTS_HTML}")
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
        logging.info(f"A pdf file has been generated at: {Directory.RESULTS_PDF}")
    else:
        fig.show()

