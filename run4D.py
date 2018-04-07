import time
import os

# THIS SCRIPT ITERATE THE N PRIZE SCORE AND REMOVE DUPLICATES!


def iterateNumbers(readfile, writefile, column):
    fname = readfile
    g = open(writefile, 'w')

    # for line in enumerate(f):
    duplicatelist = list()
    allList = list()

    with open(fname) as file:
        for row in file:
            allList.append(row)

    for row1 in allList:
        val = [rowStrip.strip() for rowStrip in row1.split(',')][column]
        counter = 0

        for row2 in allList:
            val1 = [rowStrip1.strip() for rowStrip1 in row2.split(',')][column]
            if val == val1:
                counter += 1

        if counter < 2:
            string1 = val.rstrip() + '\n'
            g.write(string1)
        else:
            if val not in duplicatelist:
                duplicatelist.append(val)

    for val2 in duplicatelist:
        string2 = val2.rstrip() + '\n'
        g.write(string2)

    file.close()
    g.close()

######################################################################################


def mergeResults(readfile1, readfile2, mergefile):
    fname = readfile1
    fname2 = readfile2
    writetofile = open(mergefile, 'w')

    # for line in enumerate(f):
    allList1 = list()
    allList2 = list()

    with open(fname) as file:
        for row in file:
            allList1.append(row)

    with open(fname2) as file:
        for row in file:
            allList2.append(row)

    for val in allList1:
        counter = 0

        for val1 in allList2:
            if val == val1:
                counter += 1

        if counter < 1:
            string2 = val.rstrip() + '\n'
            writetofile.write(string2)

    for val2 in allList2:
        string4 = val2.rstrip() + '\n'
        writetofile.write(string4)

    file.close()
    writetofile.close()

######################################################################################


def main():
    start = time.time()

    fname = '4D.txt'
    g = open('results.txt', 'w')

    # for line in enumerate(f):

    with open(fname) as f:
        next(f)
        for x in f:
            x = x.rstrip()
            if not x: break
            # [y.strip() for y in x.split(',')]
            # print ([y.strip() for y in x.split(',')][2])
            g.write([y.strip() for y in x.split(',')][2] + ',' + [y.strip() for y in x.split(',')][3] + ',' +
                    [y.strip() for y in x.split(',')][4] + '\n')  # 2 for 1st prize, 3 for 2nd prize, 4 for 3rd prize

    f.close()
    g.close()

    dirname = 'MERGED'

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    firstPrize = os.path.join(dirname, "results1stprizeremoveduplicates.txt")
    secondPrize = os.path.join(dirname, "results2ndprizeremoveduplicates.txt")
    thirdPrize = os.path.join(dirname, "results3rdprizeremoveduplicates.txt")

    mergefirstsecond = os.path.join(dirname, "merged1st2nd.txt")
    mergeAll = os.path.join(dirname, "mergedALL.txt")

    iterateNumbers('results.txt', firstPrize, 0)
    iterateNumbers('results.txt', secondPrize, 1)
    iterateNumbers('results.txt', thirdPrize, 2)

    mergeResults(firstPrize, secondPrize, mergefirstsecond)
    mergeResults(mergefirstsecond, thirdPrize, mergeAll)

    end = time.time()
    print(str(end - start) + ' seconds')


if __name__ == "__main__":
    main()

######################################################################################





