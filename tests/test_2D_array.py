#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest.mock import patch
import numpy
from MPSPlots.render2D import SceneMatrix


@patch("matplotlib.pyplot.show")
def test_Line(patch):
    x = numpy.arange(100)
    y = numpy.random.rand(100)

    figure = SceneMatrix(title='random data simple line')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    ax.add_line(x=x, y=y, label='test label')

    figure.show(save_directory='unittest_figure.svg')


@patch("matplotlib.pyplot.show")
def test_FillLine(patch):
    x = numpy.arange(100)
    y0 = numpy.random.rand(100) + x
    y1 = numpy.random.rand(100)

    figure = SceneMatrix(title='random data simple line')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    ax.add_fill_line(x=x, y0=y0, y1=y1, label='test label')

    figure.show(save_directory='unittest_figure.svg')


@patch("matplotlib.pyplot.show")
def test_STDLine(patch):
    x = numpy.arange(100)
    y = numpy.random.rand(10, 100)
    y_mean = numpy.mean(y, axis=0)
    y_std = numpy.std(y, axis=0)

    figure = SceneMatrix(title='random data simple line')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    ax.add_std_line(x=x, y_mean=y_mean, y_std=y_std)

    figure.show(save_directory='unittest_figure.svg')


@patch("matplotlib.pyplot.show")
def test_Mesh(patch):
    x, y = numpy.mgrid[-100:100, -100:100]
    scalar = x**2

    figure = SceneMatrix(title='random data simple line')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    ax.add_mesh(x=x, y=y, scalar=scalar)

    figure.show(save_directory='unittest_figure.png')

# -
