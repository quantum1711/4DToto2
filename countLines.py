import time


def printresult(foldername):

    print('\n' + foldername + ' numbers series: -------------------------------------------')

    with open(foldername + '/0series.txt') as f:
        print("\n0 : " + str(len(f.readlines())))

    with open(foldername + '/1series.txt') as f:
        print("1 : " + str(len(f.readlines())))

    with open(foldername + '/2series.txt') as f:
        print("2 : " + str(len(f.readlines())))

    with open(foldername + '/3series.txt') as f:
        print("3 : " + str(len(f.readlines())))

    with open(foldername + '/4series.txt') as f:
        print("4 : " + str(len(f.readlines())))

    with open(foldername + '/5series.txt') as f:
        print("5 : " + str(len(f.readlines())))

    with open(foldername + '/6series.txt') as f:
        print("6 : " + str(len(f.readlines())))

    with open(foldername + '/7series.txt') as f:
        print("7 : " + str(len(f.readlines())))

    with open(foldername + '/8series.txt') as f:
        print("8 : " + str(len(f.readlines())))

    with open(foldername + '/9series.txt') as f:
        print("9 : " + str(len(f.readlines())))


start = time.time()

foldername = '1STPRIZE'
printresult(foldername)

foldername = '2NDPRIZE'
printresult(foldername)

foldername = '3RDPRIZE'
printresult(foldername)

end = time.time()
print('\n' + str(end - start) + ' seconds')