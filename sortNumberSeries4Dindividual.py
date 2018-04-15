import os
import time

# THIS SCRIPT ITERATE THE 1ST PRIZE SCORE AND REMOVE DUPLICATES!


def iterateNumbers(f, dirname):

    fname = os.path.join('MERGED', f)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    zerowrite = open(dirname + "/0series.txt", 'w')
    onewrite = open(dirname + "/1series.txt", 'w')
    twowrite = open(dirname + "/2series.txt", 'w')
    threewrite = open(dirname + "/3series.txt", 'w')
    fourwrite = open(dirname + "/4series.txt", 'w')
    fivewrite = open(dirname + "/5series.txt", 'w')
    sixwrite = open(dirname + "/6series.txt", 'w')
    sevenwrite = open(dirname + "/7series.txt", 'w')
    eightwrite = open(dirname + "/8series.txt", 'w')
    ninewrite = open(dirname + "/9series.txt", 'w')

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

    zerolist.sort()
    onelist.sort()
    twolist.sort()
    threelist.sort()
    fourlist.sort()
    fivelist.sort()
    sixlist.sort()
    sevenlist.sort()
    eightlist.sort()
    ninelist.sort()

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

    iterateNumbers('results1stprizeremoveduplicates.txt', '1STPRIZE')
    iterateNumbers('results2ndprizeremoveduplicates.txt', '2NDPRIZE')
    iterateNumbers('results3rdprizeremoveduplicates.txt', '3RDPRIZE')

    end = time.time()
    print(str(end - start) + ' seconds')


if __name__ == "__main__":
    main()

######################################################################################