import time
largeNumber = 100000000

def generateSequence(arg):
    for x in range(1,arg+1):
        yield x**2-x+2

timeBefore= time.perf_counter()

for x in range(1,largeNumber+1):
         x**2-x+2
tmp1 = x/largeNumber

timeAfter= time.perf_counter()
print("Not as a function " + str(timeAfter - timeBefore))


timeBefore= time.perf_counter()

tmp2= sum(generateSequence(largeNumber))/largeNumber

timeAfter= time.perf_counter()

print("Generator Sequence " +str(timeAfter - timeBefore))