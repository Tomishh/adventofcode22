import os
import time
def read_crate():
    with open('day5_crates.txt', 'r') as f:
        array=[]
        for line in f:
            arrayline=[]
            line=line.strip()
            for letter in line:
                arrayline.append(letter)
            array.append(arrayline)
    return array

def read_order(text):
    number_of_box, array_start, array_end = text.split(" ")
    return number_of_box, array_start, array_end

def move_crates(number_of_box, array_start, array_end):
    temp_crates=array_start[-number_of_box:]
    temp_crates.reverse()
    array_end.extend(temp_crates)
    array_start=array_start[:-number_of_box]
    return array_start, array_end
    
def move_crates_boosted(number_of_box, array_start, array_end):
    temp_crates=array_start[-number_of_box:]
    array_end.extend(temp_crates)
    array_start=array_start[:-number_of_box]
    return array_start, array_end

def printArr(array):
    # time.sleep(1)
    # os.system('cls')
    for i in array:
        for j in i:
            print(f"[{j}]", end="")
        print()
    

def exo1():
    crates_list=read_crate()
    print(crates_list)
    # os.system('cls')
    with open('day5_instructions.txt', 'r') as k:
        for line in k:
            number_of_box, array_start, array_end = read_order(line)
            # print(f"Move {number_of_box} from {array_start} to {array_end}")
            temp_array_start, temp_array_end=move_crates(int(number_of_box), crates_list[int(array_start)-1], crates_list[int(array_end)-1])
            crates_list[int(array_start)-1]=temp_array_start
            crates_list[int(array_end)-1]=temp_array_end
        printArr(crates_list)
 

def exo2():
    crates_list=read_crate()
    # print(crates_list)
    # os.system('cls')
    with open('day5_instructions.txt', 'r') as k:
        # print(len(crates_list))
        for line in k:
            number_of_box, array_start, array_end = read_order(line)
            # print(f"Move {number_of_box} from {array_start} to {array_end}")
            temp_array_start, temp_array_end=move_crates_boosted(int(number_of_box), crates_list[int(array_start)-1], crates_list[int(array_end)-1])
            crates_list[int(array_start)-1]=temp_array_start
            crates_list[int(array_end)-1]=temp_array_end
            
        printArr(crates_list)
# time the execution of the function
start_time = time.time()
exo1()
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
exo2()
print("--- %s seconds ---" % (time.time() - start_time))