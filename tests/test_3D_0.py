#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
from MPSPlots.render3D import SceneList


def test_unstructured():
    figure = SceneList()

    ax = figure.append_ax()

    x = numpy.arange(100)
    y = numpy.arange(100)
    z = numpy.random.rand(100) * 30

    coordinates = numpy.c_[x, y, z].T

    ax.add_unstructured_mesh(
        coordinates=coordinates,
        scalar=x
    )

    ax.add_unit_sphere()

    ax.add_unit_axis()

    # figure.show()


def test_unit_sphere():
    figure = SceneList()

    ax = figure.append_ax()

    ax.add_unit_sphere()

    # figure.show()


def test_unit_axis():
    figure = SceneList()

    ax = figure.append_ax()

    ax.add_unit_axis()

    # figure.show()

# -
