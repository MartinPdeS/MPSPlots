#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest.mock import patch
import numpy
from MPSPlots.render2D import SceneList


@patch("matplotlib.pyplot.show")
def test_Line(patch=None):
    x = numpy.arange(100)
    y = numpy.random.rand(100)

    figure = SceneList(title='random data simple line')

    ax = figure.append_ax(x_label='x data', y_label='y data', show_legend=True)

    ax.add_line(x=x, y=y, label='single label')

    figure.show()


@patch("matplotlib.pyplot.show")
def test_FillLine(patch=None):
    x = numpy.arange(100)
    y0 = numpy.random.rand(100) + x
    y1 = numpy.random.rand(100)

    figure = SceneList(title='random data simple line')

    ax = figure.append_ax(x_label='x data', y_label='y data', show_legend=True)

    ax.add_fill_line(x=x, y0=y0, y1=y1)

    figure.show()


@patch("matplotlib.pyplot.show")
def test_STDLine(patch=None):
    x = numpy.arange(100)
    y = numpy.random.rand(10, 100)
    y_mean = numpy.mean(y, axis=0)
    y_std = numpy.std(y, axis=0)

    figure = SceneList(title='random data simple line')

    ax = figure.append_ax(x_label='x data', y_label='y data', show_legend=True)

    ax.add_std_line(x=x, y_mean=y_mean, y_std=y_std)

    figure.show()

# -
