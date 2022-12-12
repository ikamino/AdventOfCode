
with open('input.txt') as f:
    d2 = []
    for line in f: 
        line = line.split()
        d2.append(line)


#cases: a b c = rock paper scissors
#cases: x y z = rock paper scissors
#if win + 6 + number of your hand. 
#if lose + 0 + number of your hand. 

#rock beat scissors, paper beat rock, scissors beat paper, 
# if a and x: same 
# if b and y: same 
# if c and z: same

# if b and x: lose
# if c and y: lose
# if a and z: lose

# if c and x: win
# if a and y: win
# if b and z: win
def switchp1(elf, me):
    if me == "X":
        if elf == "A":
            return 4
        elif elf  == "B":
            return 1
        elif elf  == "C":
            return 7
        
    elif me == "Y":
        if elf == "A":
            return 8
        elif elf  == "B":
            return 5
        elif elf  == "C":
            return 2
    
    elif me == "Z":
        if elf == "A":
            return 3
        elif elf  == "B":
            return 9
        elif elf  == "C":
            return 6



# x means lose, y means draw, z means win.
def switchp2(elf, me):
    if me == "X":
        if elf == "A":
            return 3
        elif elf  == "B":
            return 1
        elif elf  == "C":
            return 2
        
    elif me == "Y":
        if elf == "A":
            return 4
        elif elf  == "B":
            return 5
        elif elf  == "C":
            return 6
    
    elif me == "Z":
        if elf == "A":
            return 8
        elif elf  == "B":
            return 9
        elif elf  == "C":
            return 7



def main(rounds): 
    res = 0
    res2 = 0
    for i in rounds: 
        res += switchp1(i[0], i[1])
        res2 += switchp2(i[0], i[1])
    return ([res, res2])

print(main(d2))





    

