"""
Simple Line
===========
"""

import numpy
from MPSPlots.render2D import SceneList


x = numpy.linspace(-10, 10, 100)
y0 = x**2
y1 = x**3

figure = SceneList(
    unit_size=(8, 4),
    title='random data simple lines'
)

ax = figure.append_ax(
    x_label='x data',
    y_label='y data',
    show_legend=True,
    line_width=2,
)

_ = ax.add_line(x=x, y=y0, label='line 0', color='blue')
_ = ax.add_line(x=x, y=y1, label='line 1', color='red')

_ = figure.show()
