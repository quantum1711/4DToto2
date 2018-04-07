import time

start = time.time()

with open('FINALRESULT/0series.txt') as f:
    print("\n0 : " + str(len(f.readlines())))

with open('FINALRESULT/1series.txt') as f:
    print("1 : " + str(len(f.readlines())))

with open('FINALRESULT/2series.txt') as f:
    print("2 : " + str(len(f.readlines())))

with open('FINALRESULT/3series.txt') as f:
    print("3 : " + str(len(f.readlines())))

with open('FINALRESULT/4series.txt') as f:
    print("4 : " + str(len(f.readlines())))

with open('FINALRESULT/5series.txt') as f:
    print("5 : " + str(len(f.readlines())))

with open('FINALRESULT/6series.txt') as f:
    print("6 : " + str(len(f.readlines())))

with open('FINALRESULT/7series.txt') as f:
    print("7 : " + str(len(f.readlines())))

with open('FINALRESULT/8series.txt') as f:
    print("8 : " + str(len(f.readlines())))

with open('FINALRESULT/9series.txt') as f:
    print("9 : " + str(len(f.readlines())))

end = time.time()
print('\n' + str(end - start) + ' seconds')