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

from contextlib import contextmanager
import builtins
@contextmanager
def mock_input(mocked_responses):
    # Keep a reference to the original input function
    original_input = builtins.input
    
    # Define a generator to yield mock responses
    response_gen = (response for response in mocked_responses)
    
    # This function will replace 'input'
    def input_mock(prompt=""):
        # Get the next response from the generator
        return next(response_gen)
    
    # Replace the built-in input with our mock
    builtins.input = input_mock
    
    try:
        yield  # Control to the block inside 'with' statement
    finally:
        # Restore the original input function
        builtins.input = original_input
