import string

with open('input.txt') as f:
    d3 = []
    for line in f: 
        # line = line.split()
        d3.append(line)



lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

encoded = {}

for i in range(len(lower)):
    encoded[lower[i]] = i+1
for i in range(len(upper)):
    encoded[upper[i]] = i+27

def encode_sum(items):
    res = 0
    for i in items: 
        res += encoded[i]
    return res


def p1(lines):
    items = []
    for i in lines: 
        # mid is practically guaranteed to be even. 
        mid = len(i)//2
        hash = set()
        for n in range(mid):
            hash.add(i[n])
        for n in range(mid, len(i)): 
            if i[n] in hash:
                items.append(i[n])
                break
    return items

def p2(lines):
    # group into threes
    lines = [lines[i:i+3] for i in range(0, len(lines), 3)]
    items = []
    for i in lines: 
        res = set()
        pot = set()
        for n in i[0]: 
            res.add(n)
        for n in i[1]:
            if n in res:
                pot.add(n)
        for n in i[2]:
            if n in pot: 
                items.append(n)
                break
    return items

    
print(encode_sum(p1(d3)))
print(encode_sum(p2(d3)))  


