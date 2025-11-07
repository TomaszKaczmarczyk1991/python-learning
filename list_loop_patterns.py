scores = [6, 9, 1, 4, 7, 3, 9, 8, 8, 7, 6, 2, 5]

total = 0
for score in scores:
    total += score

avg = total/len(scores)

print(avg) # 5.769230769230769

def avg(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)
    
print(avg(scores)) # 5.769230769230769


min = scores[0]
for score in scores:
    if score < min:
        min = score
        
print(min) # 1


def max(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    return max
    
print(max(scores)) # 9