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


def main(lines):
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

print(encode_sum(main(d3)))
        
        