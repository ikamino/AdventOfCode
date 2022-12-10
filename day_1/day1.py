

with open('input.txt') as f:
    d1 = [[]]
    for line in f: 
        line = line.split()
        if line:
            line = int(line[0])
            d1[-1].append(line)
        else:
            d1.append([])


# def main(nums):
#     res = 0
#     curr = 0
#     for i in nums: 
#         curr = sum(i)
#         res = max(curr, res)
#     return res



def main(nums):

    for i in range(0,len(nums)): 
        nums[i] = sum(nums[i])

    nums.sort(reverse = True)
    return nums[:3]
        
print(main(d1))

        