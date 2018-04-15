import time
from itertools import islice
import random0series
import operator
import collections
import os

# THIS SCRIPT ITERATE THE N PRIZE SCORE AND REMOVE DUPLICATES!

numberofdraws = 20
validlist = []


def iterateNumbers(readfile, column, digit):
    # for line in enumerate(f):
    prizelist = list()

    it = reversed(list(open(readfile)))
    itlist = list(islice(it, numberofdraws))
    dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for line in itlist:
        rowstrip = [rowStrip.strip() for rowStrip in line.split(',')]
        if column < 0:
            prizelist.append(rowstrip[0])
            prizelist.append(rowstrip[1])
            prizelist.append(rowstrip[2])
        else:
            prizelist.append(rowstrip[column])

    #dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    for l in prizelist:
        l = l[digit]
        dict[int(l)] += 1
        #if l not in dict:
            #dict[l] = 1
        #else:
            #dict[l] += 1

    #dict2 = collections.OrderedDict(sorted(dict.items()))

    #print("\n" + prizetype + " prize occurrence for the last "+ str(numberofdraws) + ": ")

    dictsort = sorted(dict.items(), key=lambda x: x[1])

    #for k, v in dict2.items():
    #   print("number starts with " + k + ", appeared " + str(v) + " times")
    #print("Least occurence numbers: " + dictsort[0][0] + ", " + dictsort[1][0] + ", " + dictsort[2][0])

    return dictsort

######################################################################################
#######


def display(prizetype, dictsort):
    print("\n" + prizetype + " prize occurrence for the last " + str(numberofdraws) + ": ")
    print("Least occurence numbers: " + str(dictsort[0][0]) + ", " + str(dictsort[1][0]) + ", " + str(dictsort[2][0]))


def getBestNumber(digit1, digit2, digit3, digit4, prize):
    print("Best number for " + prize + " Prize : " + str(digit1) + str(digit2) + str(digit3) + str(digit4))


def filterresults(validlist, foldername):
    print('\nOccurence in '+ foldername + ' --------------------------------------------------')
    print('\nThere are ' + str(len(validlist)) + ' possible numbers in the initial list')

    prizelist2nd = random0series.getfulllistprize(foldername)
    validlist = list(set(validlist) - set(prizelist2nd))

    print('\nAfter filtering, there are ' + str(len(validlist)) + ' possible numbers in the filtered list for ' + foldername + ' prize.\n')

    validlist = sorted(validlist)

    count = 1
    for v in validlist:
        print(str(count) + ' - ' + str(v))
        count += 1

    return validlist


def main():
    start = time.time()

    #fname = '4D.txt'
    #g = open('results.txt', 'w')
    readfile = 'results.txt'

    print("\nFirst Digit -----------------------------------------------------------")

    dict11 = iterateNumbers(readfile, 0, 0)
    dict12 = iterateNumbers(readfile, 1, 0)
    dict13 = iterateNumbers(readfile, 2, 0)
    dict1all = iterateNumbers(readfile, -1, 0)

    display('First', dict11)
    display('Second', dict12)
    display('Third', dict13)
    display('All', dict1all)

    print("\nSecond Digit -----------------------------------------------------------")

    dict21 = iterateNumbers(readfile, 0, 1)
    dict22 = iterateNumbers(readfile, 1, 1)
    dict23 = iterateNumbers(readfile, 2, 1)
    dict2all = iterateNumbers(readfile, -1, 1)

    display('First', dict21)
    display('Second', dict22)
    display('Third', dict23)
    display('All', dict2all)

    print("\nThird Digit -----------------------------------------------------------")

    dict31 = iterateNumbers(readfile, 0, 2)
    dict32 = iterateNumbers(readfile, 1, 2)
    dict33 = iterateNumbers(readfile, 2, 2)
    dict3all = iterateNumbers(readfile, -1, 2)

    display('First', dict31)
    display('Second', dict32)
    display('Third', dict33)
    display('All', dict3all)

    print("\nFourth Digit -----------------------------------------------------------")

    dict41 = iterateNumbers(readfile, 0, 3)
    dict42 = iterateNumbers(readfile, 1, 3)
    dict43 = iterateNumbers(readfile, 2, 3)
    dict4all = iterateNumbers(readfile, -1, 3)

    display('First', dict41)
    display('Second', dict42)
    display('Third', dict43)
    display('All', dict4all)

    print("\n -----------------------------------------------------------------------")
    print("\n -----------------------------------------------------------------------")


    for a in range(0, 3):
        for b in range(0, 3):
            for c in range(0, 3):
                for d in range(0, 3):
                    #getBestNumber(dict11[a][0], dict21[b][0], dict31[c][0], dict41[d][0], 'First')
                    validlist.append(str(dict11[a][0]) + str(dict21[b][0]) + str(dict31[c][0]) + str(dict41[d][0]))

    list = filterresults(validlist, '1STPRIZE')
    list = filterresults(list, '2NDPRIZE')
    filterresults(list, '3RDPRIZE')

    end = time.time()
    print('\n' + str(end - start) + ' seconds')


if __name__ == "__main__":
    main()

######################################################################################
