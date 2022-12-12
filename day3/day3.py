def exo1():
    array=[]
    value=0
    with open('day3.txt', 'r') as f:

        line= iter(f)
        for line in f:
            right= set(line[:len(line)//2])
            left = set(line[len(line)//2:])
            intersect=(right.intersection(left)).pop()
            array.append(intersect)
    print(array)
    for letter in array:
        if letter.isupper():
            value+= ord(letter) - ord('A') + 27
        else:
            value+= ord(letter) - ord('a') + 1

    print(value)

def exo2():
    array=[]
    value=0
    with open('day3.txt', 'r') as f:
        sacks = f.read().strip().split("\n")

        for i in range(0, len(sacks), 3):
            line1= set(sacks[i])
            line2= set(sacks[i+1])
            line3= set(sacks[i+2])
            array.append((line1.intersection(line2)).intersection(line3).pop())

    print(array)

    for letter in array:
        if letter.isupper():
            value+= ord(letter) - ord('A') + 27
        else:
            value+= ord(letter) - ord('a') + 1

    print(value)

exo2()