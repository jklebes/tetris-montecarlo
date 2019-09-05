class Blocks(object):
    pass

class Grid(object):
    def __init__(self, xsize, ysize):
        self.xsize=xsize
        self.ysize=ysize
        self.occupancies = [[0]* self.xsize]* self.ysize

    def step(self, temperature=0):
        pass

    def run(self, nsteps):
        pass

    def equilibrate(self):
        pass





if __name__ == "__main__":
    print("running")
    testgrid = Grid(10,10)
    print("created testgrid:", testgrid)


