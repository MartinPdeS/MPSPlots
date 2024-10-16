
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "gallery/plot_ellipse.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_gallery_plot_ellipse.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_gallery_plot_ellipse.py:


STD line
~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 7-8

Importing the script dependencies

.. GENERATED FROM PYTHON SOURCE LINES 8-11

.. code-block:: python3

    import numpy
    from MPSPlots.render2D import SceneList








.. GENERATED FROM PYTHON SOURCE LINES 12-13

Define data

.. GENERATED FROM PYTHON SOURCE LINES 13-18

.. code-block:: python3

    x = numpy.arange(100)
    y = numpy.random.rand(10, 100)
    y_mean = numpy.mean(y, axis=0)
    y_std = numpy.std(y, axis=0)








.. GENERATED FROM PYTHON SOURCE LINES 19-20

Creating the Scene

.. GENERATED FROM PYTHON SOURCE LINES 20-25

.. code-block:: python3

    figure = SceneList(
        unit_size=(8, 4),
        title='Polygon'
    )








.. GENERATED FROM PYTHON SOURCE LINES 26-27

Adding an axis to the scene for the plots

.. GENERATED FROM PYTHON SOURCE LINES 27-37

.. code-block:: python3

    ax = figure.append_ax(
        x_label='x data',
        y_label='y data',
        show_legend=True,
        equal_limits=True,
        aspect_ratio='equal'
    )

    coordinates = [(0, -1), (0, 1), (4, 1), (4, -1)]








.. GENERATED FROM PYTHON SOURCE LINES 38-39

Adding a Polygon artist to first axis

.. GENERATED FROM PYTHON SOURCE LINES 39-46

.. code-block:: python3

    _ = ax.add_polygon(
        coordinates=coordinates,
        edgecolor='black',
        facecolor='red'
    )









.. GENERATED FROM PYTHON SOURCE LINES 47-48

Adding a Polygon artist to first axis

.. GENERATED FROM PYTHON SOURCE LINES 48-57

.. code-block:: python3

    _ = ax.add_ellipse(
        position=(0, 1),
        width=1,
        height=2,
        angle=45,
        edgecolor='black',
        facecolor='red'
    )








.. GENERATED FROM PYTHON SOURCE LINES 58-59

Showing the figure

.. GENERATED FROM PYTHON SOURCE LINES 59-60

.. code-block:: python3

    _ = figure.show()



.. image-sg:: /gallery/images/sphx_glr_plot_ellipse_001.png
   :alt: Polygon
   :srcset: /gallery/images/sphx_glr_plot_ellipse_001.png
   :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 0.235 seconds)


.. _sphx_glr_download_gallery_plot_ellipse.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example




    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: plot_ellipse.py <plot_ellipse.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: plot_ellipse.ipynb <plot_ellipse.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
