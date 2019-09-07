import copy
import random

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

    def __init__(self, typeid):  # with no further arguments: init empty collection
        self.typeid = typeid
        self.blocks = set([])

    def getCount(self):
        return len(self.blocks)

    def addBlock(self, block):
        # do checks
        self.blocks.add(block)


class Block(object):
    """superclass to 7 specific types of block
    lists attributes and methods needed in each block type"""

    # the user should instantiate specific subclass objects, not Block objects
    typeid = NotImplemented
    name = NotImplemented
    shapes = NotImplemented

    def __init__(self, location, idnumber):
        """
        create a block object
        :param location: (x,y) location of upper left part of block on grid
        :param idnumber: number of this block object in the list of blocks of one type
        """
        self.location = location
        self.idnumber = idnumber
        self.shape = random.choice(self.shapes)
        # print(self.shape, location)
        self.coords = [(x + location[0], y + location[1]) for (x, y) in self.shape]
        self.idnumber = idnumber

    @staticmethod
    def createBlock(location, typeid, idnumber):
        """
        return a new block object of the desired type
        by using __init__ method from dict
        :param typeid:
        :return:
        """
        createMethodsDict = {1: (lambda loc, number: SquareBlock(loc, number)),
                             2: (lambda loc, number: LineBlock(loc, number)),
                             3: (lambda loc, number: TBlock(loc, number)),
                             4: (lambda loc, number: LBlock(loc, number)),
                             5: (lambda loc, number: LeftLBlock(loc, number)),
                             6: (lambda loc, number: RightLBlock(loc, number)),
                             7: (lambda loc, number: ZBlock(loc, number)),
                             8: (lambda loc, number: LeftZBlock(loc, number)),
                             9: (lambda loc, number: RightZBlock(loc, number)),
                             }
        # print(createMethodsDict[typeid])
        block = createMethodsDict[typeid](location, idnumber)
        return block

    def getCoords(self):
        return self.coords

    def getTypeid(self):
        return self.typeid


class SquareBlock(Block):
    typeid = 1
    name = 'square'
    shapes = [[(0, 0), (0, 1), (1, 0), (1, 1)]]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class TBlock(Block):
    typeid = 3
    name = 'T'
    shapes = [[(0, 0), (1, 0), (2, 0), (1, 1)],
              [(0, 0), (0, 1), (0, 2), (1, 1)],
              [(0, 1), (1, 1), (2, 1), (1, 0)],
              [(1, 0), (1, 1), (1, 2), (0, 1)],
              ]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class LineBlock(Block):
    typeid = 2
    name = 'line'
    shapes = [[(0, 0), (0, 1), (0, 2), (0, 3)],
              [(0, 0), (1, 0), (2, 0), (3, 0)]]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class LBlock(Block):
    typeid = 4
    name = 'L'
    """leftL and rightL shapes"""
    shapes = [[(0, 0), (0, 1), (0, 2), (1, 2)],
              [(0, 1), (1, 1), (2, 1), (2, 0)],
              [(0, 0), (1, 0), (1, 1), (1, 2)],
              [(0, 0), (1, 0), (2, 0), (0, 1)],
              [(1, 0), (1, 1), (1, 2), (0, 2)],
              [(0, 0), (0, 1), (1, 1), (2, 1)],
              [(0, 0), (1, 0), (0, 1), (0, 2)],
              [(0, 0), (1, 0), (2, 0), (2, 1)]]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class LeftLBlock(Block):
    typeid = 5
    name = 'leftL'
    """
    
    (0,0)  (1,0)  (2,0)
     
    (0,1)  (1,1)  (2,1)
    
    (0,2)  (1,2)
    
    shape:
    1. XO  2. 00X  3. XX  4. XXX
       XO     XXX     OX     XOO
       XX             OX
    
    """
    shapes = [[(0, 0), (0, 1), (0, 2), (1, 2)],
              [(0, 1), (1, 1), (2, 1), (2, 0)],
              [(0, 0), (1, 0), (1, 1), (1, 2)],
              [(0, 0), (1, 0), (2, 0), (0, 1)]]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class RightLBlock(Block):
    typeid = 6
    name = 'rightL'
    """
    shape:
    1. OX  2. XOO  3. XX  4. XXX
       OX     XXX     XO     OOX
       XX             XO

    """
    shapes = [[(1, 0), (1, 1), (1, 2), (0, 2)],
              [(0, 0), (0, 1), (1, 1), (2, 1)],
              [(0, 0), (1, 0), (0, 1), (0, 2)],
              [(0, 0), (1, 0), (2, 0), (2, 1)]]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class ZBlock(Block):
    typeid = 7
    name = 'Z'
    shapes = [[(0, 0), (0, 1), (1, 1), (1, 2)],
              [(0, 1), (1, 1), (1, 0), (2, 0)],
              [(1, 0), (1, 1), (0, 1), (0, 2)],
              [(0, 0), (1, 0), (1, 1), (2, 1)]]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class LeftZBlock(Block):
    typeid = 8
    name = 'leftZ'
    """
    shape:
    1.& 3. XO  2. & 4.  OXX  
           XX           XXO  
           OX             
    """
    shapes = [[(0, 0), (0, 1), (1, 1), (1, 2)],
              [(0, 1), (1, 1), (1, 0), (2, 0)]]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class RightZBlock(Block):
    typeid = 9
    name = 'rightZ'
    """
        shape:
        1.& 3. OX  2. & 4.  XXO  
               XX           OXX  
               XO             
    """
    shapes = [[(1, 0), (1, 1), (0, 1), (0, 2)],
              [(0, 0), (1, 0), (1, 1), (2, 1)]]

    def __init__(self, location, idnumber):
        super().__init__(location, idnumber)


class Grid(object):
    """
    main object
    """

    def __init__(self, xsize, ysize, goalnumbers):
        self.xsize = xsize
        self.ysize = ysize
        self.goalnumbers = goalnumbers
        print('goalnumbers: ', self.goalnumbers)
        self.blockcollections = {i: BlockCollection(i) for i in goalnumbers}
        self.createEmptyGrid()

    def createEmptyGrid(self):
        row1 = [0] * self.xsize
        self.occupancies = [row1]
        for i in range(1, self.ysize):  # needed to avoid pointer to same object for all rows
            row = copy.copy(row1)  # should switch to numpy
            self.occupancies.append(row)
        self.blocklist = []

    def __str__(self):  # do something with extra args later?
        outstr_list = [' .']
        for i in range(self.xsize):
            outstr_list.append('-')
        outstr_list.append('.\n')
        for row in self.occupancies:
            outstr_list.append('|')
            for i in row:
                outstr_list.append(str(i))
            outstr_list.append('|\n')
        outstr_list.append('.')
        for i in range(self.xsize):
            outstr_list.append('-')
        outstr_list.append('.\n')
        return ' '.join(outstr_list)

    def populate(self):
        done = False
        counter = 0
        limit = 10000
        while not done and counter < limit:
            # print('initiating loop', counter)
            # print(self)
            counter += 1
            for typeid in self.goalnumbers:
                done = True
                if self.blockcollections[typeid].getCount() < goalnumbers[typeid]:
                    self.add(typeid)
                    done = False
                elif self.blockcollections[typeid].getCount() < goalnumbers[typeid]:
                    print("oops, too many blocks of type ", typeid, " were added: ",
                          self.counts[typeid],
                          ' (goal: ', goal, ' )')
                    break

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

    def setOccupancy(self, x, y, typeid):
        if x < 0:
            x += self.xsize
        elif x >= self.xsize:
            x -= self.xsize
        if y < 0:
            y += self.ysize
        elif y >= self.ysize:
            y -= self.ysize
        self.occupancies[x][y] = typeid

    def setOccupied(self, block):
        for (x, y) in block.getCoords():
            self.setOccupancy(x, y, block.getTypeid())

    def checkFree(self, block):
        for (x, y) in block.getCoords():
            if self.getOccupancy(x, y) != 0:
                return False
        return True

    def add(self, typeid):
        randx = random.randrange(self.xsize)
        randy = random.randrange(self.ysize)
        location = (randy, randx)
        proposedBlock = Block.createBlock(location, typeid, self.blockcollections[typeid].getCount() + 1)

        if self.checkFree(proposedBlock):
            self.blockcollections[typeid].addBlock(proposedBlock)
            self.setOccupied(proposedBlock)

    def run(self, nsteps):
        pass

    def equilibrate(self):
        pass


if __name__ == "__main__":
    '''tests'''
    print("running")
    goalnumbers = {8:2, 9: 2}
    testgrid = Grid(10, 10, goalnumbers)
    print("created testgrid:", testgrid, sep='\n')
    testgrid.populate()
    print("populated testgrid")
    print(testgrid)
    print('blocks:', testgrid.blockcollections)
