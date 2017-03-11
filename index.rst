``geomalgo`` aims at prodiving basic geometric 2D and 3D algorithms, for
example computing the area of a 2D triangle, or finding intersection points of
3D triangle and a 3D segment.

``geomalgo`` algorithms are primary based on `geomalgorithms
<http://geomalgorithms.com>`_.

``geomalgo`` provides a convenient Python API, and a Cython API to obtain ``C``
performances, typically for computation inside loops.

Installation
------------

`Install <http://conda.pydata.org/miniconda.html>`_ the `Conda
<http://conda.pydata.org>`_ package manager, and install ``geomalgo`` with:

.. code-block:: bash

    conda install -c dfroger geomalgo  # -c conda-forge soon

Documentation
-------------

.. warning::

    This documentation is being drafted. It should be complete around in a few
    weeks (around May 2017).

.. toctree::
    :maxdepth: 1

    tutorial
    points
    vectors
    segments
    triangles
    triangulation
    triangle3d
    devel

Development and contact
-----------------------

``geomalgo`` is developed on `GitHub <https://github.com/dfroger/geomalgo>`_,
were issues and pull requests can be made. Do not hesitate to send me an
email at david.froger@mailoo.org .
