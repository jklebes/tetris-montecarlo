from tetris import *

def maxAllTypes(timestep, nsteps):
    print("running")
    goalnumbers = {1: 5000, 2: 5000, 3: 5000, 5: 5000, 6: 5000, 8: 5000, 9: 5000}
    testgrid = Grid(100, 100, goalnumbers)
    print("created testgrid:", testgrid, sep='\n')
    testgrid.populate(tries=10000)
    print("populated testgrid")
    print("counts: ", [(i, testgrid.blockcollections[i].getCount()) for i in goalnumbers])
    print(testgrid)
    countsvstime = []
    for n in range(nsteps):
        testgrid.run(timestep)
        countsvstime.append((n*timestep, [(i, testgrid.blockcollections[i].getCount()) for i in goalnumbers]))
        print(testgrid)
    print("final counts: ", [(i, testgrid.blockcollections[i].getCount()) for i in goalnumbers])
    return countsvstime

countsvstime = maxAllTypes(100, 100)
print(countsvstime)