import math
import random

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if (x < 0):
        return False
    elif (x == 0):
        return True
    n = math.log10(x)
    n = int(math.floor(n))
    for i in range ((n+3) // 2):
        l = (x % 10**(n-i+1)) // 10**(n-i)
        r = (x % 10**(i+1)) // 10**i
        if (l != r):
            return "False"
    return "True"

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    unique = nums[0]
    for i in range(1, len(nums)):
        unique ^= nums[i]
    return unique

# for i in range(1, 21):
#     a = random.randint(0, 10**16)
#     if (a % 2 == 1):
#         f = open(f"./testcases/Bonus1/{i}.in", "w")
#         f.write(str(a))
#         f.close()
#     else :
#         print(i)
#         a = random.randint(0, 10**8)
#         a = int(str(a) + str(a)[::-1])
#         f = open(f"./testcases/Bonus1/{i}.in", "w")
#         f.write(str(a))
#         # f.write(str(a)[::-1])
#         f.close()

#     ans = isPalindrome(a)
#     f = open(f"./testcases/Bonus1/{i}.out", "w")
#     f.write(ans)
#     f.close()


for i in range(1, 11):
    arr = []
    length = random.randint(1, 100)
    for j in range(length):
        arr.append(random.randint(1, 100))
    id = random.randint(0, length-1)
    print(arr[id])
    for j in range(length):
        if (j != id):
            arr.append(arr[j])
    
    f = open(f"./testcases/Bonus2/{i}.in", "w")
    f.write(f"{len(arr)}\n")
    f.write(f"{arr[0]}")
    for j in range(1, len(arr)):
        f.write(f", {arr[j]}")
    f.close()

    f = open(f"./testcases/Bonus2/{i}.out", "w")
    ans = singleNumber(arr)
    f.write(str(ans))
    f.close()
