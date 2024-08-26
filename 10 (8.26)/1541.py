s = input()
ops = []
nums = []
num = ''
for c in s:
    if c == '+' or c == '-':
        nums.append(int(num))
        num = ''
        ops.append(c)
    else:
        num += c
nums.append(int(num))

idx = 0
while(idx < len(ops)):
    if ops[idx] == '+':
        a = nums[idx]
        b = nums[idx+1]
        del(ops[idx])
        del(nums[idx])
        del(nums[idx])
        nums.insert(idx, a+b)
    else:
        idx += 1
        
answer = nums[0]
for i in range(1, len(nums)):
    answer -= nums[i]
print(answer)
