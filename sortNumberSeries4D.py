import os
import time

# THIS SCRIPT ITERATE THE 1ST PRIZE SCORE AND REMOVE DUPLICATES!


def iterateNumbers():
    fname = 'FINALRESULT/mergedAllSorted.txt'

    zerowrite = open("FINALRESULT/0series.txt", 'w')
    onewrite = open("FINALRESULT/1series.txt", 'w')
    twowrite = open("FINALRESULT/2series.txt", 'w')
    threewrite = open("FINALRESULT/3series.txt", 'w')
    fourwrite = open("FINALRESULT/4series.txt", 'w')
    fivewrite = open("FINALRESULT/5series.txt", 'w')
    sixwrite = open("FINALRESULT/6series.txt", 'w')
    sevenwrite = open("FINALRESULT/7series.txt", 'w')
    eightwrite = open("FINALRESULT/8series.txt", 'w')
    ninewrite = open("FINALRESULT/9series.txt", 'w')

    # for line in enumerate(f):
    zerolist = list()
    onelist = list()
    twolist = list()
    threelist = list()
    fourlist = list()
    fivelist = list()
    sixlist = list()
    sevenlist = list()
    eightlist = list()
    ninelist = list()

    with open(fname) as file:
        for row in file:
            row = row.rstrip()
            if int(row[:1]) == 0:
                zerolist.append(row)
            elif int(row[:1]) == 1:
                onelist.append(row)
            elif int(row[:1]) == 2:
                twolist.append(row)
            elif int(row[:1]) == 3:
                threelist.append(row)
            elif int(row[:1]) == 4:
                fourlist.append(row)
            elif int(row[:1]) == 5:
                fivelist.append(row)
            elif int(row[:1]) == 6:
                sixlist.append(row)
            elif int(row[:1]) == 7:
                sevenlist.append(row)
            elif int(row[:1]) == 8:
                eightlist.append(row)
            elif int(row[:1]) == 9:
                ninelist.append(row)

    for val in zerolist:
        zerowrite.write(val + '\n')
    for val in onelist:
        onewrite.write(val + '\n')
    for val in twolist:
        twowrite.write(val + '\n')
    for val in threelist:
        threewrite.write(val + '\n')
    for val in fourlist:
        fourwrite.write(val + '\n')
    for val in fivelist:
        fivewrite.write(val + '\n')
    for val in sixlist:
        sixwrite.write(val + '\n')
    for val in sevenlist:
        sevenwrite.write(val + '\n')
    for val in eightlist:
        eightwrite.write(val + '\n')
    for val in ninelist:
        ninewrite.write(val + '\n')

    file.close()
    zerowrite.close()
    onewrite.close()
    twowrite.close()
    threewrite.close()
    fourwrite.close()
    fivewrite.close()
    sixwrite.close()
    sevenwrite.close()
    eightwrite.close()
    ninewrite.close()

######################################################################################


def main():
    start = time.time()

    iterateNumbers()

    end = time.time()
    print(str(end - start) + ' seconds')


if __name__ == "__main__":
    main()

######################################################################################