import random
import copy
from abc import ABCMeta, abstractmethod

"""kept for reference:


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
              
"""


class Block(object):
    """superclass to 9 specific types of block
    lists attributes and methods needed in each block type"""
    typeid = NotImplemented
    name = NotImplemented
    variations = NotImplemented
    numvariations = NotImplemented

    def __init__(self, location, idnumber):
        # choose one of the variations at random
        self.shape = self.variations[random.randint(numvariations)]
        self.coords = location + shape
        self.idnumber = idnumber


class Square(Block):
    typeid=1
    name = 'square'
    variations = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
    numvariations = len(variations)

    def __init__(self, location, idnumber):
        super().__init__(Block, location, idnumber)


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
