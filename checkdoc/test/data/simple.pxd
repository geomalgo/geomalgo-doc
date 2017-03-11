from libc.math cimport sqrt

from .bar cimport CBar


# ============================================================================
# Structures
# ============================================================================


cdef struct CFoo:
    double x
    double y


cdef CFoo* new_foo()


cdef void del_foo(CFoo* foo)


cdef inline bint foo_equal(CFoo* self, CFoo* other):
    return foo.x == other.x and foo.y == other.y


# ============================================================================
# Functions
# ============================================================================


cdef void a_function(CBar* bar, const CFoo* B, const CFoo* A)

cdef void a_multiline_function(CFoo* result, CFoo* start,
                               double factor, CBar* bar)

cdef inline double inline_function(CFoo* A, CFoo* B):
    return (B.x - A.x)**2 \
         + (B.y - A.y)**2


# ============================================================================
# Extension type
# ============================================================================


cdef class Foo:
    cdef public:
        int index
        str name

    cdef:
        CFoo* cfoo

    cdef void a_method(Foo self)

    cpdef void another_method(Foo self, double, double b)
