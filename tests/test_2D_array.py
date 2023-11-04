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

    figure.show()


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

    figure.show()


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

    figure.show()


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

    figure.show()


@patch("matplotlib.pyplot.show")
def test_Colorbar(patch):
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

    ax.add_colorbar()

    figure.show()


@patch("matplotlib.pyplot.show")
def test_Contour(patch):
    x, y = numpy.mgrid[-100:100, -100:100]
    scalar = numpy.sqrt(x**2 + y**2)

    figure = SceneMatrix(unit_size=(4, 4), title='random data simple line')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    iso_values = numpy.linspace(scalar.min(), scalar.max(), 10)

    ax.add_contour(
        x=x,
        y=y,
        scalar=scalar,
        iso_values=iso_values,
        fill_contour=True
    )

    figure.show()


@patch("matplotlib.pyplot.show")
def test_VerticalLine(patch):
    figure = SceneMatrix(unit_size=(4, 4), title='random data simple line')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    ax.add_vertical_line(
        x=numpy.linspace(0, 10, 10),
        y_min=0,
        y_max=1,
        label='vertical line'
    )

    figure.show()


@patch("matplotlib.pyplot.show")
def test_scatter(patch):
    figure = SceneMatrix(title='Random text')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    ax.add_scatter(
        x=[0, 1, 2, 3],
        y=[0, 1, 2, 3],
        marker='o',
        label='test',
        color='black',
        marker_size=100,
        edge_color='red',
        line_width=3
    )

    figure.show()


@patch("matplotlib.pyplot.show")
def test_polygon(patch):
    figure = SceneMatrix(title='Random text')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    ax.add_polygon(
        coordinates=[[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
        x_scale_factor=2,
    )

    figure.show()


@patch("matplotlib.pyplot.show")
def test_annotation(patch):
    figure = SceneMatrix(title='Random text')

    _ = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    _ = figure.append_ax(
        row=1,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    _ = figure.append_ax(
        row=0,
        column=1,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    figure.annotate_axis()

    figure.show()


@patch("matplotlib.pyplot.show")
def test_text(patch):
    figure = SceneMatrix(title='Random text')

    ax = figure.append_ax(
        row=0,
        column=0,
        x_label='x data',
        y_label='y data',
        show_legend=True
    )

    ax.add_text(
        text='this is a text',
        position=(0.5, 0.5),
    )

    figure.show()

# -
