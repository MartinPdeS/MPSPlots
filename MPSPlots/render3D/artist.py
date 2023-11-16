#   !/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import pyvista
import numpy
from MPSPlots.colormaps import blue_black_red


@dataclass
class UnstructuredMesh():
    coordinates: numpy.ndarray
    scalar: numpy.ndarray
    colormap: object = field(default_factory=lambda: blue_black_red)
    symmetric_map: bool = True
    scalar_bar_args: dict = None

    def get_colormap_limit(self):
        if self.symmetric_map:
            max_abs = numpy.abs(self.scalar).max()
            if max_abs == 0:
                return [-1, 1]
            else:
                return [-max_abs, max_abs]

        return None

    def _render_(self, ax):
        ax.scene.figure.subplot(*ax.plot_number)
        self.coordinates = numpy.array(self.coordinates).T

        points = pyvista.wrap(self.coordinates)

        color_map_limit = self.get_colormap_limit()

        ax.scene.figure.add_points(
            points,
            scalars=self.scalar,
            point_size=20,
            render_points_as_spheres=True,
            cmap=self.colormap,
            clim=color_map_limit,
            scalar_bar_args=self.scalar_bar_args
        )


@dataclass
class UnitSphere():
    opacity: float = 1

    def _render_(self, ax) -> None:
        sphere = pyvista.Sphere(radius=1)
        ax.scene.figure.add_mesh(sphere, opacity=self.opacity)


@dataclass
class UnitAxis():
    labels_off: bool = False

    def _render_(self, ax) -> None:
        ax.scene.figure.add_axes_at_origin(
            labels_off=self.labels_off,
        )

# -
