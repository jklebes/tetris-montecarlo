def maxAllTypes():
    print("running")
    goalnumbers = {1: 100, 2: 100, 3: 100, 5: 100, 6: 100, 8: 100, 9: 100}
    testgrid = Grid(100, 100, goalnumbers)
    print("created testgrid:", testgrid, sep='\n')
    testgrid.populate(tries=10000)
    print("populated testgrid")
    print("counts: ", [(i, testgrid.blockcollections[i].getCount()) for i in goalnumbers])
    print(testgrid)
    testgrid.run(1000)
    print(testgrid)
    print("final counts: ", [(i, testgrid.blockcollections[i].getCount()) for i in goalnumbers])