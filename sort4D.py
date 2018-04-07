import shutil
import os
import time

start = time.time()

dirname = 'FINALRESULT'

if not os.path.exists(dirname):
    os.makedirs(dirname)

completeName = os.path.join(dirname, "mergedAllSorted.txt")

fname = 'MERGED/mergedALL.txt'
# fname2='results3rdprizeremoveduplicates.txt'
g = open(completeName, 'w')

# for line in enumerate(f):
fulllist = list()

with open(fname) as f:
    for val in f:
        val = val.rstrip()
        fulllist.append(val)

fulllist.sort()

for val1 in fulllist:
    g.write(val1 + '\n')

f.close()
g.close()

end = time.time()
print(str(end - start) + ' seconds')
