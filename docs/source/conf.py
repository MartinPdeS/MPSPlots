#!/usr/bin/env python
"""Sphinx configuration for MPSPlots."""

import matplotlib.pyplot as plt
from martinpdes_docs import configure


package_name = "MPSPlots"


def reset_mpl(gallery_conf, fname):
    """Restore the package plotting style before each gallery example."""
    plt.rcdefaults()


globals().update(
    configure(
        project=package_name,
        package=package_name,
        repository="MartinPdeS/MPSPlots",
        logo="../images/logo.png",
        favicon="../images/logo.png",
        prefer_installed_package=True,
        html_theme_options={
            "show_nav_level": 1,
            "show_toc_level": 2,
        },
        gallery_options={
            "reset_modules": [reset_mpl],
        },
        html_css_files=["layout.css"],
        extension_additions=["pyvista.ext.plot_directive"],
    )
)
