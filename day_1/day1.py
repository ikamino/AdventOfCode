

with open('input.txt') as f:
    d1 = [[]]
    for line in f: 
        line = line.split()
        if line:
            line = int(line[0])
            d1[-1].append(line)
        else:
            d1.append([])


def p1(nums):
    res = 0
    curr = 0
    for i in nums: 
        curr = sum(i)
        res = max(curr, res)
    return res



def p2(nums):
    for i in range(0,len(nums)): 
        nums[i] = sum(nums[i])
    nums.sort(reverse = True)
    return sum(nums[:3])
        
print(p1(d1))
print(p2(d1))