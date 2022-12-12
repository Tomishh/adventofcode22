with open('day2.txt') as f:
    score_lui=0
    score_moi=0
    for line in f:
        if line[0]=='A' and line[2]=='X':
            score_lui+=1+3
            score_moi+=1+3
        if line[0]=='B' and line[2]=='Y':
            score_lui+=2+3
            score_moi+=2+3
        if line[0]=='C' and line[2]=='Z':
            score_lui+=3+3
            score_moi+=3+3
        if line[0]=='A':
            if line[2]=='Y':
                score_lui+=1
                score_moi+=2+6
            if line[2]=='Z':
                score_lui+=1+6
                score_moi+=3
        if line[0]=='B':
            if line[2]=='X':
                score_lui+=2+6
                score_moi+=1
            if line[2]=='Z':
                score_lui+=2
                score_moi+=3+6
        if line[0]=='C':
            if line[2]=='X':
                score_lui+=1
                score_moi+=1+6
            if line[2]=='Y':
                score_lui+=3+6
                score_moi+=2
print(score_lui)
print(score_moi)


### exo 2 :

with open('day2.txt') as f:
    score_lui=0
    score_moi=0
    for line in f:
        if line[2]=='X':
            # need to lose
            if line[0]=='A':
                score_moi+=3
            if line[0]=='B':
                score_moi+=1
            if line[0]=='C':
                score_moi+=2
        if line[2]=='Y':
            #need to draw:
            if line[0]=='A':
                score_moi+=1+3
            if line[0]=='B':
                score_moi+=2+3
            if line[0]=='C':
                score_moi+=3+3
        if line[2]=='Z':
            #need to win:
            if line[0]=='A':
                score_moi+=2+6
            if line[0]=='B':
                score_moi+=3+6
            if line[0]=='C':
                score_moi+=1+6

print(score_lui)
print(score_moi)