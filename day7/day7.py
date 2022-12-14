import re

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele+"/"
    return str1

def exo1():
    Path= dict()
    onlyNumber = re.compile(r"[0-9]+")
    array = []
    pwdArr= []
    Sum=0
    with open("day7.txt") as f:
        lines = f.readlines()
        for line in lines:
            line=line.strip()
            if "$" in line:
                # print(f"{line} : instruction")
                if "cd /" in line:
                    pwdArr=[]
                elif "cd .." in line:
                    print(f"popping :{pwdArr}")
                    print(f"popping :{pwdArr[-1]}")
                    pwdArr.pop()
                    print(f"popping :{pwdArr}")
                elif "cd" in line and "$ ls" not in line:
                    line=line.strip()
                    directory = line.split("$ cd ")[1]
                    pwdArr.append(directory)
            elif onlyNumber.match(line.split(" ")[0]):
                # print(f"{line} : regex")
                if listToString(pwdArr) not in Path:
                    Path[listToString(pwdArr)]=int(line.split(" ")[0])
                else:
                    Path[listToString(pwdArr)]=int(Path[listToString(pwdArr)])+int(line.split(" ")[0])

            
            
            
    for ele in Path:
        print(Path[ele])
        # if int(Path[ele]) <= 100000:
        #     Sum+=int(Path[ele])
        #     print(f"{Path[ele]}\t {ele}")
        
    # for ele in Path:
    #     print(f"{Path[ele]}\t {ele}")
    
    print(Sum)
exo1()