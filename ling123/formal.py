from functools import lru_cache


def chunk_pattern(p):
  # Splits the pattern alternating literals (strings) and
  # variables (enclosed in braces {}).
  return tuple(y for x in p.split('}') if x for y in x.split('{'))


def split_string(s):
  # Returns all left/right pairs which combine to form the string s
  return [(s[:i], s[i:]) for i in range(len(s) + 1)]


@lru_cache(maxsize=10000)
def match(chunks, s, is_literal=True):
  # Recursively generates all values for variables matching
  # the input string s

  if not chunks:
    # End if there are no more pattern chunks to match
    return [] if s else [{}]

  # Otherwise, break off the next pattern chunk
  cur_chunk, chunks = chunks[0], chunks[1:]

  if is_literal:
    # The current chunk is a literal -- ensure it is the prefix of s
    return (
        # Return remaining matches, starting with a variable
        match(chunks, s[len(cur_chunk):], False)
        # But only if cur_chunk is a prefix of s
        if s.startswith(cur_chunk) else [])
  else:
    # The current chunk is a variable -- get all possible values
    return [
        # Combine the current value with the rest
        {
            cur_chunk: left,
            **rest
        }
        # for all left/right splits of s
        for left, right in split_string(s)
        # for all ways to match remaining variables
        for rest in match(chunks, right, True)
        # ignoring cases where the same var gets two diff values
        if cur_chunk not in rest or rest[cur_chunk] == left
    ]


def run_rule(input_pattern, output_pattern, s):
  # run one rule (input/output pattern) on string s
  return [
      output_pattern.format(**d)
      for d in match(chunk_pattern(input_pattern), s)
  ]


found = set()


def get_outputs(s, rules):
  # get all outputs of all rules, run on s
  return [(found.add(o) if o not in found else False) or o for ip, op in rules
          for o in run_rule(ip, op, s)]


def theorem_tree(s, rules, maxdepth=5, reset_found=True):
  global found
  if reset_found: found.clear()
  # generate a tree structure of branching thereom transformations
  return [s] + [
      theorem_tree(o, rules, maxdepth - 1, False) if maxdepth > 1 else o
      for o in get_outputs(s, rules)
  ]


def all_theorems():
  return found
