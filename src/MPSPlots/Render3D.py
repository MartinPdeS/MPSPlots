
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyvista, logging, numpy

class Scene3D:
    
    def __init__(self, **kwargs):
        self.Figure = pyvista.Plotter(theme=pyvista.themes.DocumentTheme(), **kwargs)


    def Add_Unstructured(self, Coordinate: numpy.ndarray, Scalar: numpy.ndarray=None, Plot: tuple=(0,0), **kwargs):
        self.Figure.subplot(*Plot)
        Coordinate = numpy.array(Coordinate).T
        Points = pyvista.wrap(Coordinate)
        self.Figure.add_points(Points, scalars=Scalar, point_size=20, render_points_as_spheres=True, **kwargs)


    def Add_Mesh(self, Coordinate: numpy.ndarray, Plot: tuple=(0,0), **kwargs):
        self.Figure.subplot(*Plot)
        mesh = pyvista.StructuredGrid(*Coordinate)

        self.Figure.add_mesh(mesh, **kwargs)

        return self.Figure


    def __add_unit_sphere__(self, Plot: tuple=(0,0), **kwargs):
        self.Figure.subplot(*Plot)
        sphere = pyvista.Sphere(radius=1)
        self.Figure.add_mesh(sphere, opacity=0.3)


    def __add_axes__(self, Plot: tuple=(0,0)):
        self.Figure.subplot(*Plot)
        self.Figure.add_axes_at_origin(labels_off=True)


    def __add__text__(self, Plot: tuple=(0,0), Text='', **kwargs):
        self.Figure.subplot(*Plot)
        self.Figure.add_text(Text, **kwargs)


    def Show(self):
        self.Figure.show()

