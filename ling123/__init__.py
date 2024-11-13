from .magics import print123
from .formal import all_theorems, theorem_tree, get_outputs
from .grader import Grader
from .genai import ask_gpt

import pprint
import textwrap
def pp(x, tostring=False):
  if type(x) == str:
    out = textwrap.fill(x, replace_whitespace=False)
  else:
    out = pprint.pformat(x, compact=True)

  if tostring: return out
  else: print(out)

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

import base64

def encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    return base64.b64encode(data)

def decode(encoded_data, decode_to_str=True):
    decoded_data = base64.b64decode(encoded_data)
    if decode_to_str:
        return decoded_data.decode('utf-8')
    return decoded_data
