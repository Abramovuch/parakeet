
# Authors: Nathan Faggian, Stefan van der Walt, Aron Ahmadia, Olivier Grisel
# https://github.com/stefanv/growcut_py

import numpy as np

def growcut_python(image, state, state_next, window_radius):
    changes = 0
    height = image.shape[0]
    width = image.shape[1]
    for j in xrange(width):
        for i in xrange(height):
            winning_colony = state[i, j, 0]
            defense_strength = state[i, j, 1]
            for jj in xrange(max(j-window_radius,0), min(j+window_radius+1, width)):
                for ii in xrange(max(i-window_radius, 0), min(i+window_radius+1, height)):
                    if ii != i or jj != j:
                        d = image[i, j, :] - image[ii, jj, :]
                        s = np.sum(d**2) 
                        gval = 1.0 - np.sqrt(s) / np.sqrt(3)
                        attack_strength = gval * state[ii, jj, 1]
                        if attack_strength > defense_strength:
                            defense_strength = attack_strength
                            winning_colony = state[ii, jj, 0]
                            changes += 1
            state_next[i, j, 0] = winning_colony
            state_next[i, j, 1] = defense_strength
    return changes

from parakeet.testing_helpers import expect, run_local_tests 

def run_growcut(N = 3, window_radius = 2):
  image = np.zeros((N, N, 3), dtype=np.double)
  state = np.zeros((N, N, 2), dtype=np.double)
  state_next = np.empty_like(state)

  # colony 1 is strength 1 at position 0,0
  # colony 0 is strength 0 at all other positions
  state[0, 0, 0] = 1
  state[0, 0, 1] = 1
  growcut_python(image, state, state_next, window_radius)
  return state_next 

def test_growcut():
  res = run_growcut()
  expect(run_growcut, [], res)


if __name__ == "__main__":
  run_local_tests()
