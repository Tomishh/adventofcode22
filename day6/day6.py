import time
def exo1():
    with open('day6.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            print(loop_4_last_char(line,4))

def loop_4_last_char(line,nbChar):

    for i in range(0, len(line)):
        if len(set(line[i:i+nbChar])) == nbChar:
            return i+nbChar

def exo2():
    with open('day6.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            print(loop_4_last_char(line,14))


start_time = time.time()
exo1()
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
exo2()
print("--- %s seconds ---" % (time.time() - start_time))