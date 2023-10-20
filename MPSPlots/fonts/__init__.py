# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

from matplotlib import font_manager
from MPSPlots.tools.directories import fonts_directory


__all__ = [
    'cmu.serif-roman',
    'cmu.serif-bold'
]

for font in __all__:
    font_file = f'{font}.ttf'
    font_file = fonts_directory.joinpath(font_file)
    font_manager.fontManager.addfont(font_file)

# -
