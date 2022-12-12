import time
def exo1():
    #while loop which parse a day1.txt file and print each line
    array = [0]
    with open('day1.txt') as f:
        i=0
        for line in f:
            if line != '\n':
                array[i]=array[i]+int(line)
            else:
                i+=1
                array.append(0)
    sorted_array=sorted(array)
    print(sorted_array.pop())
##print last 3 elements of the array

def exo2():
    #while loop which parse a day1.txt file and print each line
    array = [0]
    with open('day1.txt') as f:
        i=0
        for line in f:
            if line != '\n':
                array[i]=array[i]+int(line)
            else:
                i+=1
                array.append(0)
    sorted_array=sorted(array)
    print(sum(sorted_array[-3:]))
##print last 3 elements of the array

start_time = time.time()
exo1()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
exo2()
print("--- %s seconds ---" % (time.time() - start_time))
