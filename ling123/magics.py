from IPython.lib.pretty import pretty
from IPython.core.display import HTML
from IPython.core.magic import register_cell_magic
from re import split


class Statement():
  """Class to represent statements"""


def eval_or_exec(s):
  ns = get_ipython().user_ns
  try:
    return eval(s, ns)
  except:
    exec(s, ns)


TEMPLATE = """\
<hr style="width: {width}pt; margin-left: 0;"/><b><pre>{x}</pre></b>
<div style="display: flex; justify-content: space-between; width: {width}pt;">
  <span style="text-align:left"> <b style="padding-right: 10pt">⇒</b>
    <code style="background-color: #e0f0ff">{v}</code></span>
  <span style="text-align: right;">
    <span style="background-color: #e0ffe0">{t}</span>
  </span></div>
"""


@register_cell_magic
def print123(args, cell):
  stms = split(r'(?<!\\)\n(?=[^\s])', cell)
  values = [(line, pretty(v := eval_or_exec(line)),
             pretty(type(v)) if v is not None else '') for line in stms
            if line.split('#')[0]]
  if (width := max(len(value[1] + value[2])
                   for value in values) * 6 + 30) > 450:
    width = 450

  out = [TEMPLATE.format(width=width, x=x, v=v, t=t) for x, v, t in values]
  return HTML('\n'.join(out))
