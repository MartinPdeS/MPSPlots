#!/usr/bin/env python
"""Sphinx configuration for MPSPlots."""

import os
from importlib.metadata import version as distribution_version

import matplotlib.pyplot as plt
from martinpdes_docs import configure
from sphinx_gallery.sorting import FileNameSortKey


package_name = "MPSPlots"
version = distribution_version(package_name)


def reset_mpl(gallery_conf, fname):
    """Restore the package plotting style before each gallery example."""
    plt.rcdefaults()


globals().update(
    configure(
        project=package_name,
        package=package_name,
        version=os.getenv("tag", version),
        repository="MartinPdeS/MPSPlots",
        logo="../images/logo.png",
        favicon="../images/logo.png",
        extensions=[
            "pyvista.ext.plot_directive",
            "sphinx.ext.autodoc",
            "sphinx.ext.napoleon",
            "sphinx.ext.viewcode",
            "sphinx.ext.autosectionlabel",
            "sphinx.ext.intersphinx",
            "sphinx_gallery.gen_gallery",
        ],
        html_theme_options={
            "show_nav_level": 1,
            "show_toc_level": 2,
        },
        sphinx_gallery_conf={
            "reset_modules": [reset_mpl],
            "within_subsection_order": FileNameSortKey,
        },
    )
)

# Keep the local layout refinements alongside the shared documentation theme.
html_css_files = ["default.css", "layout.css", "martinpdes_layout.css"]
