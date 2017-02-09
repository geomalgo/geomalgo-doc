**********
Triangle2D
**********

Contruction
===========

.. py:class:: Triangle2D(A, B, C, index=0, force_counterclockwise=False)

    Create a triangle :math:`ABC`, where ``A``, ``B`` and ``C`` are
    :class:`Point2D`.

    ``index`` is an optional integer index for this triangle.

    If force_counterclockwise is True, points A, B and C may be reordered so
    that triangle is counterclockwise

Read-write attributes
=====================

.. py:attribute:: A: Point2D

.. py:attribute:: B: Point2D

.. py:attribute:: C: Point2D

Triangle points. They may be replaced by another points, for example:

.. code-block:: python

    ABC.A = Point2D(1, 2)

or coordinate may be changed inplace, for example:

.. code-block:: python

    ABC.A.y = -2

In either case, the method :meth:`recompute` must be called after change(s).

Read only attributes
====================

.. py:attribute:: area: float

    Triangle area.

.. py:attribute:: center: Point2D

    Triangle center.

.. py:attribute:: counterclockwise: bool

    Whether triangle is counterclockwise.

Methods
=======

.. py:method:: recompute(self)

Recompute triangle properties (signed area, ...). Must be called when
a triangle point is changed, or its coordinate is chanded.

.. py:method:: includes_point(self, P, edge_width=0.)

    Test if the triangle includes (contains) the point :math:`P`.

    If point :math:`P` is on one of the edge of triangle, due to
    `numerical accuracy issues <https://totologic.blogspot.fr/2014/01/accurate-point-in-triangle-test.html>`_,
    the test may failed.

    To solve this issue, if ``edge_width_square`` is not ``0``, triangle will be
    considered to include :math:`P` if distance between :math:`P` and one of
    triangle edge is less than ``edge_width`` (the root square of
    ``edge_width_square``).

.. py:method:: interpolate(self, data: double[3], P: Point2D)

    Interpolate ``data`` defined on triangle vertices, to a point ``P``
    inside the triangle.

.. py:method:: plot(self, style='b-')

    Plot triangle points using matplotlib
