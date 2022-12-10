

with open('input.txt') as f:
    d1 = [[]]
    for index, line in enumerate(f): 
        line = line.split('\n')
        if line[0] != '':
            line = int(line[0])
            d1[-1].append(line)
        else:
            d1.append([])


def main(nums):
    res = 0
    curr = 0
    for i in nums: 
        curr = sum(i)
        res = max(curr, res)
    return res
        
print(main(d1))

        