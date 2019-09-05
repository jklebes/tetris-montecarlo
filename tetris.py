class Blocks(object):
  # number - name associations hardcoded
  names = {1: 'square', 5: 'leftL', 6: 'rightL', 4: 'L', 3: 'T', 2: 'line', 8: 'leftZ', 9: 'rightZ', 7: 'Z'}
  inversenames = {v: k for k, v in names.items()}
  # number - shape associations hardcoded
  coords = {1: [(0, 0), (0, 1), (1, 0), (1, 1)],
            2: [(0, 0), (0, 1), (0, 2), (0, 3)],
            3: [(0, 0), (1, 0), (2, 0), (1, 1)],
            4: [(0, 0), (0, 1), (0, 2), (1, 2)],
            5: [(0, 0), (0, 1), (0, 2), (1, 2)],
            6: [(0, 0), (1, 0), (1, 1), (1, 2)],
            7: [(0, 0), (0, 1), (1, 1), (1, 2)],
            8: [(0, 0), (0, 1), (1, 1), (1, 2)],
            9: [(1, 0), (1, 1), (0, 1), (0, 2)]
            }
  # include random rotating?
  rotatable = {1: False, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}
  # include random flips?
  flippable = {1: False, 2: False, 3: False, 4: True, 5: False, 6: False, 7: True, 8: False, 9: False}


  def __init__(self, types, chempots=None):
    self.types = []
    for i in types:
      if isinstance(i, int):
        self.types.append(i)
      elif isinstance(i, str):
        try:
          self.types.append(self.inversenames[i])
        except KeyError:
          print("Shape name: '", i,"' not found.  Choose shape names from: ",
                set(self.inversenames), sep='')
          raise
    print(self.types)

  def step(self):
    randx=8
    randy=8


class Grid(object):
  """
  main object
  """

  def __init__(self, xsize, ysize, blocks):
    self.xsize = xsize
    self.ysize = ysize
    self.blocks = blocks
    self.occupancies = [[0] * self.xsize] * self.ysize

  def step(self, temperature=0):
    pass

  def run(self, nsteps):
    pass

  def equilibrate(self):
    pass


if __name__ == "__main__":
  '''tests'''
  print("running")
  squares = Blocks(types=['square'])
  testgrid = Grid(10, 10, squares)
  print("created testgrid:", testgrid)
