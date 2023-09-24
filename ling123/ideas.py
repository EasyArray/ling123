from itertools import islice, tee, count

class TupleGen:
  def __init__(self, g):
    self.g = g

  def __iter__(self):
    return iter(self.g)

  def __getitem__(self, key):
    if isinstance(key, int):
      self.g, newg = tee(self.g)
      return tuple(islice(newg,key))
    if isinstance(key, slice):
      self.g, newg = tee(self.g)
      return tuple(islice(newg, key.start, key.stop, key.step))

    raise KeyError(f"Incorrect index or slice: {key}")

ranger = TupleGen(count())

print(ranger[10])
print(ranger[2:10:3])
