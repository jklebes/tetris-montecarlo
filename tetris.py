import random
import copy
from abc import ABCMeta, abstractmethod

class Blocks(object):
    """
    Blocks object is just a list of dictionaries
    from each blockid, we should be able to look up
    (hardcoded) name, shape, symmetries
    (chosen) desired number, volume fraction, or chemical potential
    (dynamic) counter
    """
    # hardcoded characteristics of the blocks
    names = {1: 'square', 5: 'leftL', 6: 'rightL', 4: 'L', 3: 'T', 2: 'line', 8: 'leftZ', 9: 'rightZ', 7: 'Z'}
    inversenames = {v: k for k, v in names.items()}
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
    rotatable = {1: False, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}
    flippable = {1: False, 2: False, 3: False, 4: True, 5: False, 6: False, 7: True, 8: False, 9: False}

    def __init__(self, types, goalnumbers):
        self.types = []
        for i in types:
            if isinstance(i, int):
                self.types.append(i)
            elif isinstance(i, str):
                try:
                    self.types.append(self.inversenames[i])
                except KeyError:
                    print("Shape name: '", i, "' not found.  Choose shape names from: ",
                          set(self.inversenames), sep='')
                    raise
        print(self.types)
        self.numbergoals = dict(zip(self.types, goalnumbers))
        print('numbergoals:', self.numbergoals)
        self.blockcounts = dict([(blocknumber, 0) for blocknumber in self.types])


class Block(object, metaclass=ABCmeta):
    """abstract superclass to 9 types of block
    lists attributes and methods needed in each block type"""
    @abstractmethod
    def method1(self):
      pass


class Square(Block):
    pass


class Grid(object):
    """
    main object
    """

    def __init__(self, xsize, ysize, blocks):
        self.xsize = xsize
        self.ysize = ysize
        self.blocks = blocks
        row1 = [0] * self.xsize
        self.occupancies = [row1]
        for i in range(1, ysize):  # needed to avoid pointer to same object for all rows
            row = copy.copy(row1)  # should switch to numpy
            self.occupancies.append(row)
        self.blocklist = []

    def __str__(self):  # do something with extra args later?
        outstr_list = []
        for row in self.occupancies:
            outstr_list.append('|')
            for i in row:
                outstr_list.append(str(i))
            outstr_list.append('|\n')
        return ' '.join(outstr_list)

    def initiate(self):
        done = False
        counter = 0
        limit = 10000
        while not done and counter < limit:
            # print('initiating loop', counter)
            # print(self)
            counter += 1
            for blocknumber in self.blocks.types:
                done = True
                if self.blocks.blockcounts[blocknumber] < self.blocks.numbergoals[blocknumber]:
                    self.add(blocknumber)
                    done = False
                elif self.blocks.blockcounts[blocknumber] > self.blocks.numbergoals[blocknumber]:
                    print("oops, too many blocks of type ", blocknumber, " were added: ",
                          self.blocks.blockcounts[blocknumber],
                          ' (goal: ', self.blocks.numbergoals[blocknumber], ' )')

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
        if x < 0:
            x += self.xsize
        elif x >= self.xsize:
            x -= self.xsize
        if y < 0:
            y += self.ysize
        elif y >= self.ysize:
            y -= self.ysize
        return self.occupancies[x][y]

    def setOccupancy(self, x, y, blocknumber):
        if x < 0:
            x += self.xsize
        elif x >= self.xsize:
            x -= self.xsize
        if y < 0:
            y += self.ysize
        elif y >= self.ysize:
            y -= self.ysize
        self.occupancies[x][y] = blocknumber

    def add(self, blocknumber):
        randx = random.randrange(self.xsize)
        randy = random.randrange(self.ysize)
        free = True
        for field in Blocks.coords[blocknumber]:
            locationx = randx + field[0]
            locationy = randy + field[1]
            # print('checking ', locationx, locationy, ': ')
            if self.getOccupancy(locationx, locationy):
                # print('not free')
                free = False
            else:
                # print('free')
                pass
        if free:
            # print('adding at: ')
            for field in Blocks.coords[blocknumber]:
                locationx = randx + field[0]
                locationy = randy + field[1]
                # print(locationx, locationy)
                self.setOccupancy(locationx, locationy, blocknumber)
                self.blocks.blockcounts[blocknumber] += 1
                self.blocklist.append(Block(id_, typenumber, location))

    def run(self, nsteps):
        pass

    def equilibrate(self):
        pass


if __name__ == "__main__":
    '''tests'''
    print("running")
    squares = Blocks(types=['square', 'L'], goalnumbers=[8, 2])
    testgrid = Grid(10, 10, squares)
    print("created testgrid:", testgrid, sep='\n')
    testgrid.initiate()
    print("populated testgrid")
    print(testgrid)
    print('counts:', testgrid.blocks.blockcounts)
