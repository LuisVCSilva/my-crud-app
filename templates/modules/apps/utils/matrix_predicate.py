from sympy import Q as question_query
from sympy.abc import *

attrs = [question_query.commutative(x), question_query.is_true(x), question_query.symmetric(x), question_query.invertible(x), question_query.orthogonal(x), question_query.unitary(x), question_query.positive_definite(x), question_query.upper_triangular(x), question_query.lower_triangular(x), question_query.diagonal(x), question_query.fullrank(x), question_query.square(x), question_query.integer_elements(x), question_query.real_elements(x), question_query.complex_elements(x), question_query.singular(x), question_query.normal(x), question_query.triangular(x), question_query.unit_triangular(x)]
