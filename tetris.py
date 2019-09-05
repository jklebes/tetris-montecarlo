class Blocks(object):

    #number - name associations hardcoded
    names={1:'square'}

    def __init__(self):
        pass
        print(self.names)

    def getName(self, number):
        assert number<= max(self.names)
        return(self.names[number])

class Grid(object):
    """
    main object
    """
    def __init__(self, xsize, ysize, blocks):
        self.xsize=xsize
        self.ysize=ysize
        self.blocks=blocks
        self.occupancies = [[0]* self.xsize]* self.ysize

    def step(self, temperature=0):
        pass

    def run(self, nsteps):
        pass

    def equilibrate(self):
        pass





if __name__ == "__main__":
    '''tests'''
    print("running")
    testgrid = Grid(10,10)
    print("created testgrid:", testgrid)


