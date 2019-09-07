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

class BlockCollection(object):
    """holds many blocks of one type"""
    def __init__(self, typeid): #with no further arguments: init empty collection
        self.typeid=typeid

class Block(object):
    """superclass to 7 specific types of block
    lists attributes and methods needed in each block type"""

    #the user should instantiate specific subclass objects, not Block objects
    typeid = NotImplemented
    name = NotImplemented
    baseShape = NotImplemented #coords, starting from (0,0), defining the shape of the block
    rotates = NotImplemented
    chiral = NotImplemented

    def __init__(self, location, idnumber):
        """
        create a block object
        :param location: (x,y) location of upper left part of block on grid
        :param idnumber: number of this block object in the list of blocks of one type
        """
        self.location=location
        self.idnumber=idnumber
        # populate self.variations from base shape, information on symmetries
        # put this somewhere else to avoid doing it for each new block ?
        self.shape = self.baseShape
        # flip or rotate at random, if applicable
        if self.rotates:
            self.shape=self.randomRotate(self.shape)
        if self.chiral:
            self.shape = self.randomFlip(self.shape)
        self.coords = location + self.shape
        self.idnumber = idnumber



class SquareBlock(Block):
    typeid=1
    name = 'square'
    baseshape = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
    chiral=False
    rotates = False

    def __init__(self, location, idnumber):
        super().__init__(Block, location, idnumber)

class TBlock(Block):
    pass

class LineBlock(Block):
    pass

class LBlock(Block):
    pass

class LeftLBlock(Block):
    pass

class RightLBlock(Block):
    pass

class ZBlocK(Block):
    pass

class LeftZBlock(Block):
    pass

class RightZBlock(Block):
    pass


class Grid(object):
    """
    main object
    """

    def __init__(self, xsize, ysize, goalnumbers):
        self.xsize = xsize
        self.ysize = ysize
        self.goalnumbers=goalnumbers
        self.blockcollection={i, BlockCollection() for i in goalnumbers}
        self.createEmptyGrid()

    def createEmptyGrid(self):
        row1 = [0] * self.xsize
        self.occupancies = [row1]
        for i in range(1, self.ysize):  # needed to avoid pointer to same object for all rows
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

    def populate(self):
        done = False
        counter = 0
        limit = 10000
        while not done and counter < limit:
            # print('initiating loop', counter)
            # print(self)
            counter += 1
            for (typeid, goal) in self.goalnumbers:
                done = True
                if self.counts[typeid] < goal:
                    self.add(typeid)
                    done = False
                elif self.counts[typeid] < goal
                    print("oops, too many blocks of type ", typeid, " were added: ",
                          self.counts[typeid] ,
                          ' (goal: ', goal, ' )')

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
    goalnumbers = {1: 5} #specify the simulation should contain 5 squares
    testgrid = Grid(10, 10, goalnumbers)
    print("created testgrid:", testgrid, sep='\n')
    testgrid.populate()
    print("populated testgrid")
    print(testgrid)
    print('counts:', testgrid.blocks.blockcounts)
