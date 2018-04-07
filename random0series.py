import time
import random

# THIS SCRIPT GIVES A RANDOM NUMBER FOR THE 0 SERIES


def randomseries(filename, rangeStart, rangeEnd, seriesText):
    fname = "FINALRESULT/" + str(filename)

    # for line in enumerate(f):
    zerolist = list()

    with open(fname) as file:
        for row in file:
            row = row.rstrip()
            zerolist.append(row)

    numbers = ["%#04d" % num for num in range(rangeStart, rangeEnd)]

    validlist = list(set(numbers) - set(zerolist))

    print('\nrandom number for ' + str(seriesText) + ' series is : ' + str(random.choice(validlist)))

    file.close()

######################################################################################


def main():
    start = time.time()

    randomseries('0series.txt', 0, 999, 0)
    randomseries('1series.txt', 1000, 1999, 1)
    randomseries('2series.txt', 2000, 2999, 2)
    randomseries('3series.txt', 3000, 3999, 3)
    randomseries('4series.txt', 4000, 4999, 4)
    randomseries('5series.txt', 5000, 5999, 5)
    randomseries('6series.txt', 6000, 6999, 6)
    randomseries('7series.txt', 7000, 7999, 7)
    randomseries('8series.txt', 8000, 8999, 8)
    randomseries('9series.txt', 9000, 9999, 9)

    end = time.time()
    print('\n' + str(end - start) + ' seconds\n')


if __name__ == "__main__":
    main()

######################################################################################