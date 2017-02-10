``geomalgo`` aims at prodiving basic geometric 2D and 3D algorithms, for
example computing the area of 2D triangle, or finding intersection points of
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

    conda install -c dfroger geomalgo

Documentation
-------------

.. toctree::
    :maxdepth: 1

    tutorial
    points
    vectors
    segments
    triangles
    triangulation
    devel

Development and contact
-----------------------

``geomalgo`` is developed on `GitHub <https://github.com/dfroger/geomalgo>`_,
were issues and pull requests can be made. Or do not hesitate to send me an
email at david.froger@mailoo.org .
