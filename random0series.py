import time
import random

# THIS SCRIPT GIVES A RANDOM NUMBER FOR THE 0 SERIES


def randomseries(foldername ,filename, rangeStart, rangeEnd):
    fname = foldername + "/" + str(filename)

    # for line in enumerate(f):
    zerolist = list()

    with open(fname) as file:
        for row in file:
            row = row.rstrip()
            zerolist.append(row)

    numbers = ["%#04d" % num for num in range(rangeStart, rangeEnd)]

    validlist = list(set(numbers) - set(zerolist))

    #print('\nrandom number for ' + str(seriesText) + ' series is : ' + str(random.choice(validlist)))

    file.close()
    return validlist

######################################################################################


def printlist(list, seriesText):
    print('\nrandom number for ' + str(seriesText) + ' series is : ' + str(random.choice(list)))


def getfulllistprize(foldername):
    list0 = randomseries(foldername, '0series.txt', 0, 1000)

    list1 = randomseries(foldername, '1series.txt', 1000, 2000)

    list2 = randomseries(foldername, '2series.txt', 2000, 3000)

    list3 = randomseries(foldername, '3series.txt', 3000, 4000)

    list4 = randomseries(foldername, '4series.txt', 4000, 5000)

    list5 = randomseries(foldername, '5series.txt', 5000, 6000)

    list6 = randomseries(foldername, '6series.txt', 6000, 7000)

    list7 = randomseries(foldername, '7series.txt', 7000, 8000)

    list8 = randomseries(foldername, '8series.txt', 8000, 9000)

    list9 = randomseries(foldername, '9series.txt', 9000, 10000)

    fulllist = list0 + list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9
    return fulllist


def printresults(foldername, prize):
    print("\n" + prize + " Prize--------------------------------------------------------")

    list0 = randomseries(foldername, '0series.txt', 0, 1000)
    printlist(list0, 0)

    list1 = randomseries(foldername, '1series.txt', 1000, 2000)
    printlist(list1, 1)

    list2 = randomseries(foldername, '2series.txt', 2000, 3000)
    printlist(list2, 2)

    list3 = randomseries(foldername, '3series.txt', 3000, 4000)
    printlist(list3, 3)

    list4 = randomseries(foldername, '4series.txt', 4000, 5000)
    printlist(list4, 4)

    list5 = randomseries(foldername, '5series.txt', 5000, 6000)
    printlist(list5, 5)

    list6 = randomseries(foldername, '6series.txt', 6000, 7000)
    printlist(list6, 6)

    list7 = randomseries(foldername, '7series.txt', 7000, 8000)
    printlist(list7, 7)

    list8 = randomseries(foldername, '8series.txt', 8000, 9000)
    printlist(list8, 8)

    list9 = randomseries(foldername, '9series.txt', 9000, 10000)
    printlist(list9, 9)


def main():
    start = time.time()

    foldername = '1STPRIZE'
    printresults(foldername, '1st')

    foldername = '2NDPRIZE'
    printresults(foldername, '2nd')

    foldername = '3RDPRIZE'
    printresults(foldername, '3rd')

    print("\n-----------------------------------------------------------------")

    end = time.time()
    print('\n' + str(end - start) + ' seconds\n')


if __name__ == "__main__":
    main()

######################################################################################