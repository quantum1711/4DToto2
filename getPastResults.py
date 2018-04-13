import time
from itertools import islice
import collections
import os

# THIS SCRIPT ITERATE THE N PRIZE SCORE AND REMOVE DUPLICATES!


def iterateNumbers(readfile, column, prizetype):
    # for line in enumerate(f):
    prizelist = list()
    numberofdraws = 30

    it = reversed(list(open(readfile)))
    itlist = list(islice(it, numberofdraws))
    dict = {}

    for line in itlist:
        rowstrip = [rowStrip.strip() for rowStrip in line.split(',')]
        if column < 0:
            prizelist.append(rowstrip[0])
            prizelist.append(rowstrip[1])
            prizelist.append(rowstrip[2])
        else:
            prizelist.append(rowstrip[column])

    for l in prizelist:
        l = l[0]
        if l not in dict:
            dict[l] = 1
        else:
            dict[l] += 1

    dict2 = collections.OrderedDict(sorted(dict.items()))

    print("\n" + prizetype + " prize occurrence for the last "+ str(numberofdraws) + ": ")

    for k, v in dict2.items():
        print("number starts with " + k + ", appeared " + str(v) + " times")

######################################################################################
#######


def main():
    start = time.time()

    #fname = '4D.txt'
    #g = open('results.txt', 'w')

    iterateNumbers('results.txt', 0, "First")
    iterateNumbers('results.txt', 1, "Second")
    iterateNumbers('results.txt', 2, "Third")
    iterateNumbers('results.txt', -1, "All")

    end = time.time()
    print('\n' + str(end - start) + ' seconds')


if __name__ == "__main__":
    main()

######################################################################################
