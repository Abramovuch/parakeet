import numpy as np
from parakeet import jit  
from testing_helpers import expect_eq  

@jit 
def add(x,y):
  return x + y

def test_2d_scalar():
  x = np.zeros((2,3))
  res = add(x, 1)
  expect_eq(res, x + 1)

def test_2d_1d():
  x = np.zeros((2,3))
  y = np.ones((3,))
  res = add(x, y)
  expect_eq(res, x + y)

def test_2d_2d():
  x = np.zeros((2,3))
  y = np.ones((2,3))
  res = add(x, y)
  expect_eq(res, x + y)
  


  
  