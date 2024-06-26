
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "gallery/plot_mesh.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_gallery_plot_mesh.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_gallery_plot_mesh.py:


Mesh - Line
~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 7-8

Importing the script dependencies

.. GENERATED FROM PYTHON SOURCE LINES 8-11

.. code-block:: python3

    import numpy
    from MPSPlots.render2D import SceneList








.. GENERATED FROM PYTHON SOURCE LINES 12-13

Define data

.. GENERATED FROM PYTHON SOURCE LINES 13-15

.. code-block:: python3

    x, y, = numpy.mgrid[0:100, 0:100]








.. GENERATED FROM PYTHON SOURCE LINES 16-17

Creating the Scene

.. GENERATED FROM PYTHON SOURCE LINES 17-22

.. code-block:: python3

    figure = SceneList(
        unit_size=(8, 4),
        title='random data simple lines'
    )








.. GENERATED FROM PYTHON SOURCE LINES 23-24

Adding few axis to the scene for the plots

.. GENERATED FROM PYTHON SOURCE LINES 24-36

.. code-block:: python3

    ax_0 = figure.append_ax(
        x_label='x data',
        y_label='y data',
        show_legend=False
    )

    ax_1 = figure.append_ax(
        x_label='x data',
        y_label='y data',
        show_legend=False
    )








.. GENERATED FROM PYTHON SOURCE LINES 37-38

Adding a Mesh artist to first axis

.. GENERATED FROM PYTHON SOURCE LINES 38-46

.. code-block:: python3

    artist_0 = ax_0.add_mesh(
        scalar=x + y,
        x=x,
        y=y,
    )

    ax_0.add_colorbar(artist=artist_0)








.. GENERATED FROM PYTHON SOURCE LINES 47-48

Adding a Mesh artist to second axis

.. GENERATED FROM PYTHON SOURCE LINES 48-54

.. code-block:: python3

    artist_1 = ax_1.add_mesh(
        scalar=x**2,
        x=x,
        y=y,
    )








.. GENERATED FROM PYTHON SOURCE LINES 55-56

Extra decoration of the axes

.. GENERATED FROM PYTHON SOURCE LINES 56-58

.. code-block:: python3

    figure.annotate_axis(numerotation_type='roman')








.. GENERATED FROM PYTHON SOURCE LINES 59-60

Showing the figure

.. GENERATED FROM PYTHON SOURCE LINES 60-61

.. code-block:: python3

    _ = figure.show()



.. image-sg:: /gallery/images/sphx_glr_plot_mesh_001.png
   :alt: random data simple lines
   :srcset: /gallery/images/sphx_glr_plot_mesh_001.png
   :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 0.235 seconds)


.. _sphx_glr_download_gallery_plot_mesh.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example




    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: plot_mesh.py <plot_mesh.py>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: plot_mesh.ipynb <plot_mesh.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
