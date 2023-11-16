#   !/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
import pyvista
import numpy
import matplotlib
from MPSPlots import colormaps
from MPSPlots.render3D.axis import Axis


@dataclass
class SceneList:
    shape: tuple = (1, 1)
    """ Number of plot and their configuration """
    unit_size: tuple = (800, 800)
    """ Kindof the same as below """
    window_size: tuple = None
    """ Size of the output windows """
    background_color: str = 'white'
    """ Background of the rendering """
    ax_orientation: str = 'horizontal'

    def __post_init__(self) -> None:
        if self.window_size is None:
            self.window_size = (self.unit_size[1] * self.shape[1], self.unit_size[0] * self.shape[0])

        self.figure = pyvista.Plotter(
            theme=pyvista.themes.DocumentTheme(),
            window_size=self.window_size,
            shape=self.shape,
        )

        self.figure.set_background(self.background_color)

        self.axis_list = []

    def get_next_plot_number(self) -> tuple:
        if len(self.axis_list) == 0:
            return (0, 0)

        last_axis = self.axis_list[-1]
        last_plot_number = last_axis.plot_number

        if self.ax_orientation == 'horizontal':
            return last_plot_number[0], last_plot_number[1] + 1

        if self.ax_orientation == 'vertical':
            return last_plot_number[0] + 1, last_plot_number[1]

    def append_ax(self):
        plot_number = self.get_next_plot_number()

        ax = Axis(
            plot_number=plot_number,
            scene=self
        )

        self.axis_list.append(ax)

        return ax

    def add_unstructured_mesh(self, *args, **kwargs) -> None:
        """
        Adds an unstructured mesh to a plot. The  unstructured data is represented
        with 3d points in the volume. If scalars is given then the colormap is used.

        :param      args:    The arguments
        :type       args:    list
        :param      kwargs:  The keywords arguments
        :type       kwargs:  dictionary

        :returns:   No return
        :rtype:     None
        """
        if kwargs.get('scalar', None) is not None:
            return self.add_unstructured_mesh_with_scalar(*args, **kwargs)
        else:
            return self.add_unstructured_mesh_without_scalar(*args, **kwargs)

    def get_color_map_limit(self, scalar: numpy.ndarray, symmetric_map: bool):
        if symmetric_map:
            max_abs = numpy.abs(scalar).max()
            if max_abs == 0:
                color_map_limit = [-1, 1]
            else:
                color_map_limit = [-max_abs, max_abs]
        else:
            color_map_limit = None

        return color_map_limit

    def add_unstructured_mesh_with_scalar(self,
            coordinates: numpy.ndarray,
            scalar: numpy.ndarray = None,
            plot_number: tuple = (0, 0),
            color_map: str = colormaps.blue_black_red,
            scalar_bar_args: dict = None,
            symmetric_map: bool = True) -> None:

        self.figure.subplot(*plot_number)

        points = pyvista.wrap(coordinates)

        color_map_limit = self.get_color_map_limit(scalar=scalar, symmetric_map=symmetric_map)

        self.figure.add_points(
            points,
            scalars=scalar,
            point_size=20,
            render_points_as_spheres=True,
            cmap=color_map,
            clim=color_map_limit,
            scalar_bar_args=scalar_bar_args
        )

    def add_unstructured_mesh_without_scalar(self,
            coordinates: numpy.ndarray,
            plot_number: tuple = (0, 0)) -> None:

        self.figure.subplot(*plot_number)

        points = pyvista.wrap(coordinates)

        self.figure.add_points(
            points,
            point_size=20,
            render_points_as_spheres=True,
            cmap='white'
        )

    def add_mesh(self,
                 x: numpy.ndarray,
                 y: numpy.ndarray,
                 z: numpy.ndarray,
                 plot_number: tuple = (0, 0),
                 color_map: str = colormaps.blue_black_red,
                 **kwargs) -> None:

        if isinstance(color_map, str):  # works only for matplotlib 3.6.1
            color_map = matplotlib.colormaps[color_map]

        self.figure.subplot(*plot_number)

        mesh = pyvista.StructuredGrid(x, y, z)

        self.figure.add_mesh(
            mesh=mesh,
            cmap=color_map,
            style='surface',
            **kwargs
        )

        return self.figure

    def get_spherical_vector_from_coordinates(self, phi: numpy.ndarray, theta: numpy.ndarray, component: str, radius: float = 1.0):
        if component.lower() == 'theta':
            vector = [1, 0, 0]
        elif component.lower() == 'phi':
            vector = [0, 1, 0]
        elif component.lower() == 'r':
            vector = [0, 0, 1]

        x, y, z = pyvista.transform_vectors_sph_to_cart(theta, phi, radius, *vector)

        return numpy.c_[x.ravel(), y.ravel(), z.ravel()]

    def add_spherical_component_vector_to_ax(self, plot_number: tuple,
                                                   component: str,
                                                   theta: numpy.ndarray,
                                                   phi: numpy.ndarray,
                                                   radius: float = 1.03 / 2) -> None:
        self.figure.subplot(*plot_number)

        vector = self.get_spherical_vector_from_coordinates(
            phi=phi,
            theta=theta,
            component=component,
            radius=radius
        )

        spherical_vector = pyvista.grid_from_sph_coords(theta, phi, radius)

        spherical_vector.point_data["component"] = vector * 0.1

        vectors = spherical_vector.glyph(
            orient="component",
            scale="component",
            tolerance=0.005
        )

        self.figure.add_mesh(vectors, color='k')

    def add_theta_vector_field(self, plot_number: list, radius: float = 1.03 / 2) -> None:
        theta = numpy.arange(0, 360, 10)
        phi = numpy.arange(180, 0, -10)

        self.add_spherical_component_vector_to_ax(
            plot_number=plot_number,
            component='theta',
            radius=radius,
            phi=phi,
            theta=theta
        )

    def add_phi_vector_field(self, plot_number: tuple, radius: float = 1.03 / 2) -> None:
        theta = numpy.arange(0, 360, 10)
        phi = numpy.arange(180, 0, -10)

        self.add_spherical_component_vector_to_ax(
            plot_number=plot_number,
            component='phi',
            radius=radius,
            phi=phi,
            theta=theta
        )

    def add_r_vector_field(self, plot_number: tuple, radius: float = [1.03 / 2]) -> None:
        theta = numpy.arange(0, 360, 10)
        phi = numpy.arange(180, 0, -10)

        self.add_spherical_component_vector_to_ax(
            plot_number=plot_number,
            component='r',
            radius=radius,
            phi=phi,
            theta=theta
        )

    def add_unit_sphere_to_ax(self, plot_number: tuple = (0, 0)):
        self.figure.subplot(*plot_number)
        sphere = pyvista.Sphere(radius=1)
        self.figure.add_mesh(sphere, opacity=0.3)

    def add_unit_axes_to_ax(self, plot_number: tuple = (0, 0)):
        self.figure.subplot(*plot_number)
        self.figure.add_axes_at_origin(labels_off=True)

    def add_text_to_axes(self, plot_number: tuple = (0, 0), text='', **kwargs):
        self.figure.subplot(*plot_number)
        self.figure.add_text(text, **kwargs)

    def show(self, save_directory: str = None, window_size: tuple = (1200, 600)):
        for ax in self.axis_list:
            ax._render_()

        self.figure.show(
            screenshot=save_directory,
            window_size=window_size,
        )

        return self

    def close(self):
        self.figure.close()