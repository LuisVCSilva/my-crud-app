from sympy import Q as question_query
from sympy.abc import *

attrs = [question_query.hermitian(x), question_query.antihermitian(x), question_query.real(x), question_query.extended_real(x), question_query.imaginary(x), question_query.complex(x), question_query.algebraic(x), question_query.transcendental(x), question_query.integer(x), question_query.rational(x), question_query.irrational(x), question_query.finite(x), question_query.infinite(x), question_query.positive(x), question_query.negative(x), question_query.zero(x), question_query.nonzero(x), question_query.nonpositive(x), question_query.nonnegative(x), question_query.even(x), question_query.odd(x), question_query.prime(x), question_query.composite(x)]

