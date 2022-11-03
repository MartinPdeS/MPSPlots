#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, numpy
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib import colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.gridspec as gridspec
from itertools import cycle
from . import CMAP

from dataclasses import dataclass


import matplotlib
matplotlib.style.use('ggplot')


linecycler = cycle(["-","--","-.",":"])


@dataclass
class ColorBar:
    Color: str = 'viridis'
    Discreet: bool = False
    Position: str = 'left'
    Orientation: str = "vertical"
    Symmetric: bool = False
    LogNorm: bool = False
    Format: str = ':.3f'
    LogNorm: bool = False

    def Render(self, Ax, Scalar, Image):
        divider = make_axes_locatable(Ax._ax)
        cax = divider.append_axes(self.Position, size="10%", pad=0.15)

        if self.Discreet:
            Values = numpy.unique(Scalar)
            Norm = colors.BoundaryNorm(Values, Values.size+1, extend='both')
            Norm.autoscale(Scalar)
            Image.set_norm(Norm)
            ticks = numpy.unique(Scalar)
            plt.colorbar(mappable=Image, norm=Norm, boundaries=ticks, cax=cax, orientation=self.Orientation)
            return

        if self.LogNorm:
            if self.Symmetric:

                Norm = matplotlib.colors.SymLogNorm(linthresh=1e-10)
                Norm.autoscale(Scalar)
                Image.set_norm(Norm)
                plt.colorbar(mappable=Image, norm=Norm, cax=cax, orientation=self.Orientation)
                return
        
            if not self.Symmetric:
                Norm = matplotlib.colors.LogNorm(linthresh=0.03)
                Norm.autoscale(Scalar)
                Image.set_norm(Norm)
                plt.colorbar(mappable=Image, norm=Norm, cax=cax, orientation=self.Orientation)
                return
        
        plt.colorbar(mappable=Image, norm=None, cax=cax, orientation=self.Orientation)


@dataclass
class Contour:
    X: numpy.ndarray
    Y: numpy.ndarray
    Scalar: numpy.ndarray
    ColorMap: str = CMAP.BKR
    xLabel: str = ''
    yLabel: str = ''
    IsoLines: list = None

    def Render(self, Ax):
        Image = Ax.contour(self.X,
                            self.Y,
                            self.Scalar,
                            level = self.IsoLines,
                            colors="black",
                            linewidth=.5 )

        Image = Ax.contourf(self.X,
                            self.Y,
                            self.Scalar,
                            level = self.IsoLines,
                            cmap=self.ColorMap,
                            norm=colors.LogNorm() )


@dataclass
class Mesh:
    X: numpy.ndarray
    Y: numpy.ndarray
    Scalar: numpy.ndarray
    ColorMap: str = CMAP.BKR
    Label: str = ''

    def Render(self, Ax):
        Image = Ax._ax.pcolormesh(self.X, self.Y, self.Scalar.T, cmap=self.ColorMap, shading='auto')
        Image.set_edgecolor('face')

        if Ax.Colorbar is not None:
            Ax.Colorbar.Render(Ax=Ax, Scalar=self.Scalar, Image=Image)

        return Image


@dataclass
class FillLine:
    X: numpy.ndarray
    Y0: numpy.ndarray
    Y1: numpy.ndarray
    Label: str = None
    Fill: bool = False
    Color: str = None
    LineStyle: str = None
    Outline: bool = True
    
    def Render(self, Ax):
        if self.LineStyle is None: self.LineStyle = next(linecycler)
        Ax._ax.fill_between(self.X, self.Y0, self.Y1, color=self.Color, linestyle=self.LineStyle, alpha=0.7, label=self.Label)
        
        if self.Outline:
            Ax._ax.plot(self.X, self.Y1, color='k', linestyle='-', linewidth=1)


@dataclass
class STDLine:
    X: numpy.ndarray
    YMean: numpy.ndarray
    YSTD: numpy.ndarray
    Label: str = None
    Fill: bool = False
    Color: str = None
    LineStyle: str = None
    
    def Render(self, Ax):
        if self.LineStyle is None: 
            self.LineStyle = next(linecycler)

        y0 = self.YMean - self.YSTD / 2
        y1 = self.YMean + self.YSTD / 2

        line = Ax._ax.plot(self.X, self.YMean, color=self.Color, label=self.Label + '[mean]', linestyle=self.LineStyle)

        Ax._ax.fill_between(self.X, y0, y1, color=line[-1].get_color(), linestyle='-', alpha=0.3, label=self.Label + '[std]')


@dataclass
class Line:
    X: numpy.ndarray
    Y: numpy.ndarray
    Label: str = None
    Color: str = None
    LineStyle: str = None
    
    def Render(self, Ax):
        if self.LineStyle is None: 
            self.LineStyle = next(linecycler)

        if numpy.iscomplexobj(self.Y):
            Ax._ax.plot(self.X, self.Y.real, label=self.Label + "[real]", color=self.Color, linestyle=self.LineStyle)
            Ax._ax.plot(self.X, self.Y.imag, label=self.Label + "[imag]", color=self.Color, linestyle=self.LineStyle)
        else:
            Ax._ax.plot(self.X, self.Y, label=self.Label, color=self.Color, linestyle=self.LineStyle)


@dataclass
class Text:
    Position: list = (0.9, 0.9)
    FontSize: int = 8
    Text: str = ''

    def Render(self, Ax):
        art = AnchoredText(self.Text,
                       loc='lower left', prop=dict(size=self.FontSize), frameon=True,
                       bbox_to_anchor=(0.05, 1.0),
                       bbox_transform=Ax._ax.transAxes)

        Ax._ax.get_figure().add_artist(art)


class Scene2D:
    UnitSize = (10, 3)
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams["font.size"] = 10
    plt.rcParams["font.family"] = "serif"
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['legend.fontsize'] = 'medium'

    def __init__(self, Title='', UnitSize=None):
        self.AxisGenerated = False
        self._Axis = []
        self.Title = Title
        self.nCols = 1
        self.nRows = None
        if UnitSize is not None: 
            self.UnitSize = UnitSize

    @property
    def Axis(self):
        if not self.AxisGenerated:

            self.GenerateAxis()

        return self._Axis

    def AddAxes(self, *Axis):
        for ax in Axis:
            self._Axis.append(ax)

        return self

    def GetMaxColsRows(self):
        RowMax, ColMax = 0, 0
        for ax in self._Axis:
            RowMax = ax.Row if ax.Row > RowMax else RowMax
            ColMax = ax.Col if ax.Col > ColMax else ColMax

        return RowMax, ColMax

    def GenerateAxis(self):
        RowMax, ColMax = self.GetMaxColsRows()

        FigSize = [ self.UnitSize[0]*(ColMax+1), self.UnitSize[1]*(RowMax+1) ]

        self.Figure = plt.figure(figsize=FigSize)

        Grid = gridspec.GridSpec(ncols=ColMax+1, nrows=RowMax+1, figure=self.Figure)

        Ax = numpy.full(shape=(RowMax+1, ColMax+1), fill_value=None)

        for axis in self._Axis:
            subplot = self.Figure.add_subplot(Grid[axis.Row, axis.Col], projection=axis.Projection)
            Ax[axis.Row, axis.Col] = subplot

        Ax = numpy.asarray(Ax)

        self.Figure.suptitle(self.Title)

        for ax in self._Axis:
            ax._ax = Ax[ax.Row, ax.Col]

        self.AxisGenerated = True

        return self

    def Render(self):
        for ax in self.Axis:
            ax.Render()

        plt.tight_layout()

        return self

    def Show(self, SaveDir: str = None, **kwargs):
        self.Render()
        if SaveDir is not None:
            plt.savefig(fname=SaveDir, **kwargs)
        plt.show()


@dataclass
class Axis:
    Row: int
    Col: int
    xLabel: str = ''
    yLabel: str = ''
    Title: str = ''
    Grid: bool = True
    Legend: bool = False
    xScale: str = 'linear'
    yScale: str = 'linear'
    xLimits: list = None
    yLimits: list = None
    Equal: bool = False
    Colorbar: ColorBar = None
    WaterMark: str = ''
    Figure: Scene2D = None
    Projection: str = None

    def __post_init__(self):

        self._ax = None
        self.Artist = []

    @property
    def Labels(self):
        return {'x': self.xLabel,
                'y': self.yLabel,
                'Title': self.Title}

    def AddArtist(self, *Artist):
        for art in Artist:
            self.Artist.append(art)

    def Render(self):
        logging.debug("Rendering Axis...")

        for art in self.Artist:
            Image = art.Render(self)

        if self.Legend:
            self._ax.legend(fancybox=True, facecolor='white', edgecolor='k')

        self._ax.grid(self.Grid)

        if self.xLimits is not None: 
            self._ax.set_xlim(self.xLimits)

        if self.yLimits is not None: 
            self._ax.set_ylim(self.yLimits)

        self._ax.set_xlabel(self.Labels['x'])
        self._ax.set_ylabel(self.Labels['y'])
        self._ax.set_title(self.Labels['Title'])

        self._ax.set_xscale(self.xScale)
        self._ax.set_yscale(self.yScale)

        self._ax.text(0.5, 0.1, self.WaterMark, transform=self._ax.transAxes,
                fontsize=30, color='white', alpha=0.2,
                ha='center', va='baseline')

        if self.Equal:
            self._ax.set_aspect("equal")


def Multipage(filename, figs=None, dpi=200):
    pp = PdfPages(filename)

    for fig in figs:
        fig.Figure.savefig(pp, format='pdf')

    pp.close()


# -
