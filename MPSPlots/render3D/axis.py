#   !/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

from MPSPlots.render3D.artist import UnstructuredMesh, UnitSphere, UnitAxis


@dataclass
class Axis():
    plot_number: tuple
    scene: object

    def __post_init__(self) -> None:
        self.artist_list = []

    def add_unstructured_mesh(self, *args, **kwargs) -> UnstructuredMesh:
        artist = UnstructuredMesh(*args, **kwargs)

        self.artist_list.append(artist)

        return artist

    def add_unit_sphere(self, *args, **kwargs) -> UnitSphere:
        artist = UnitSphere(*args, **kwargs)

        self.artist_list.append(artist)

        return artist

    def add_unit_axis(self, *args, **kwargs) -> UnitAxis:
        artist = UnitAxis(*args, **kwargs)

        self.artist_list.append(artist)

        return artist

    def _render_(self):
        for artist in self.artist_list:
            artist._render_(ax=self)

# -
