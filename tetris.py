import random

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



class Grid(object):
  """
  main object
  """

  def __init__(self, xsize, ysize, blocks):
    self.xsize = xsize
    self.ysize = ysize
    self.blockstypes = blocks.types
    self.occupancies = [[0] * self.xsize] * self.ysize

    #should be in blocks object maybe
    self.goals = dict([(blocknumber,5) for blocknumber in self.blockstypes]) #hard coaded goal for testing
    #should be passed in blocks object
    self.blockcounts = dict([(blocknumber,0) for blocknumber in self.blockstypes])

  def initiate(self):
    done=False
    while not done:
      for blocknumber in self.blockstypes:
        done = True
        if self.blockcounts[blocknumber]< self.goals[blocknumber]:
          self.add(blocknumber)
          done = False
        elif self.blockcounts[blocknumber] > self.goals[blocknumber]:
          print("oops, too many blocks of type ", blocknumber, " were added")

  def step(self, temperature=0):
    """
    fixed number simulation
    :param temperature:
    :return:
    """
    for i in blocks:
      self.remove(i)
      self.add(i)

  def getOccupancy(self, x, y):
    """
    handle boundary conditions here
    :param x:
    :param y:
    :return:
    """
    if x < 0: x+=self.xsize
    elif x >=self.xsize : x -= self.xsize
    if y < 0: y+=self.ysize
    elif y >=self.ysize : y -= self.ysize
    return self.occupancies[x][y]

  def setOccupancy(self, x, y, blocknumber):
    pass

  def add(self, blocknumber):
    randx = random.randrange(self.xsize)
    randy = random.randrange(self.ysize)
    free=True
    for field in Blocks.coords[blocknumber]:
      locationx = randx+field[0]
      locationy = randy + field[1]
      if self.getOccupancy(locationx, locationy):
        free=False
    if free:
      for field in Blocks.coords[blocknumber]:
        self.setOccupancy(locationx, locationy, blocknumber)



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
  testgrid.initiate()
  print("added to testgrid")
