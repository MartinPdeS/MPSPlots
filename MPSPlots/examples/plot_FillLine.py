"""
Fill Line
=========
"""

import numpy
from MPSPlots.render2D import SceneList


x = numpy.arange(100)
y0 = numpy.random.rand(100) + x
y1 = numpy.random.rand(100) - x

figure = SceneList(
    unit_size=(8, 4),
    title='random data simple lines'
)

ax = figure.append_ax(
    x_label='x data',
    y_label='y data',
    show_legend=True
)

_ = ax.add_fill_line(
    x=x,
    y0=y0,
    y1=y1,
    label='Fill between lines',
    show_outline=True
)

_ = figure.show()
