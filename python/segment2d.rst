*********
Segment2D
*********

Contruction
===========

.. py:class:: Segment2D(A, B)

    Create a segment :math:`[AB]`, where ``A`` and ``B`` can be either
    :class:`Point2D` or tuple ``(x,y)``.

Read-write attributes
=====================

.. py:attribute:: A: Point2D

.. py:attribute:: B: Point2D

Segment Points. They may be replaced by another points, for example:

.. code-block:: python

    AB.A = Point2D(1, 2)

or coordinate may be changed inplace, for example:

.. code-block:: python

    AB.A.y = -2

Read only attributes
====================

.. py:attribute:: area: length

    Segment length :math:`|AB|`

Methods
=======

In either case, the method :meth:`recompute` must be called after change(s).

.. py:method:: recompute(self)

Recompute segment property (length, vector). Must be called when
a segment point is changed, or its coordinate is chanded.
