"""
Multi ax plots
~~~~~~~~~~~~~~
"""

# %%
# Importing the script dependencies
import numpy
from MPSPlots.render2D import SceneList

# %%
# Define data
x = numpy.arange(100)
y0 = numpy.random.rand(100) + x
y1 = numpy.random.rand(100) - x

# %%
# Creating the Scene
figure = SceneList(
    unit_size=(8, 4),
    title='random data simple lines'
)

# %%
# Adding a first axis to the scene for the plots
ax0 = figure.append_ax(
    x_label='x data',
    y_label='y data',
    show_legend=True,
    equal_limits=True,
    water_mark='yoyo'
)

# %%
# Adding a second axis to the scene for the plots
ax1 = figure.append_ax(
    x_label='x data',
    y_label='y data',
    show_legend=True
)

# %%
# Adding a FillLine artist to first axis
_ = ax0.add_fill_line(
    x=x,
    y0=y0,
    y1=y1,
    label='Fill between lines',
    show_outline=True
)

# %%
# Adding a FillLine artist to second axis
_ = ax1.add_fill_line(
    x=x,
    y0=y0,
    y1=y1,
    label='Fill between lines',
    show_outline=False,
    color='red'
)

# %%
# Showing the figure
_ = figure.show()
