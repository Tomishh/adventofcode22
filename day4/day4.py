def exo1():
    total=0
    with open("day4.txt") as f:
        for line in f:
            line=line.strip()
            firstString, secondString = line.split(",")
            if checkContaining(firstString, secondString):
                total+=1
                print(f"{firstString} {secondString} containing")                
    print(f"\n{total}")

def checkContaining(firstString, secondString) -> bool:
    min1, max1 = firstString.split("-")
    min2, max2 = secondString.split("-")
    min1, max1, min2, max2 = int(min1), int(max1), int(min2), int(max2)
    return (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2)


def exo2():
    total=0
    with open("day4.txt") as f:
        for line in f:
            line=line.strip()
            firstString, secondString = line.split(",")
            min1, max1 = firstString.split("-")
            min2, max2 = secondString.split("-")
            if checkOverlaping(min1, max1, min2, max2):
                total+=1
    print(total)

def checkOverlaping(min1, max1, min2, max2) -> bool:
    min1, max1, min2, max2 = int(min1), int(max1), int(min2), int(max2)
    return (min2 <= max1 and min1 <= max2) or (min1 <= max2 and min2 <= max1)
                        
exo2()