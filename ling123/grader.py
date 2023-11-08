import pickle
from IPython.display import HTML
from unittest import TestCase

class Grader:
  def __init__(self, pkl=None):
    self.results = {}
    self.answers = {}
    if pkl:
      self.key = pickle.loads(pkl)
    else:
      self.key = pkl

  def check(self, ex, answer, test='assertEqual', msg=None):
    from . import pp
    self.answers[ex] = answer
    result = f'<h2>Exercise {ex} Results</h2>\n'
    result += f'<pre>{pp(answer,True)}</pre>\n'
    if self.key and ex in self.key:
      try:
        getattr(TestCase(),test)(answer, self.key[ex], msg)
        result += '<h3 style="color:green;">Correct!</h3>'
      except Exception as e:
        result += '<h3 style="color:red;">Incorrect!</h3>\n'
        result += f'{e}'.replace('\n', '\n<br/>')
    else:
      result += '<h3>No key provided</h3>'

    result = HTML(result)
    self.results[ex] = result
    display(result)

  def __call__(self):
    if not self.key:
      display(HTML('<h2>Answer Key Code</h3>'))
      display(pickle.dumps(self.answers))
    else:
      for ex in self.results:
        display(self.results[ex])
