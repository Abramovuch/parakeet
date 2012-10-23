import syntax 
import core_types 
import tuple_type 

def const_int(n, t = core_types.Int64):
  return syntax.Const(n, type = t)


def const_float(f, t = core_types.Float64):
  return syntax.Const(f, type = t)

def const_bool(b, t = core_types.Bool):
  return syntax.Const(b, type = t)

def const_scalar(x):
  if isinstance(x, int):
    return const_int(x)
  elif isinstance(x, bool):
    return const_bool(x)
  else:
    assert isinstance(x, float)
    return const_float(x)
  
  
def get_type(expr):
  return expr.type

def get_types(exprs):
  return [expr.type for expr in exprs]

def make_tuple(elts):
  elt_types = get_types(elts)
  tuple_t = tuple_type.make_tuple_type(elt_types)
  return syntax.Tuple(elts, type = tuple_t)

def const_tuple(*numbers):
  return make_tuple(map(const_scalar, numbers))