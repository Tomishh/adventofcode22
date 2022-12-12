#while loop which parse a day1.txt file and print each line
array = [0]
with open('day1.txt') as f:
    i=0
    for line in f:
        if line != '\n':
            print(line)
            array[i]=array[i]+int(line)
        else:
            i+=1
            array.append(0)
sorted_array=sorted(array)
##print last 3 elements of the array
print(sum(sorted_array[-3:]))