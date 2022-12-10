
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
def main(rounds): 
    zero = ['X', 'Y', 'Z']
    for i in rounds: 
        