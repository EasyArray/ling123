from .magics import print123
from .formal import all_theorems, theorem_tree, get_outputs
from .grader import Grader

import pprint
import textwrap
def pp(x):
  if type(x) == str:
    print(textwrap.fill(x))
  else:
    pprint.pp(x, compact=True)

pp(mad_lib)
