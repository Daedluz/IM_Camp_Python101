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

x = int(input())
print(isPalindrome(x))



# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     unique = nums[0]
#     for i in range(1, len(nums)):
#         unique ^= nums[i]
#     return unique


# a = input()
# a = input() 
# a = a.split(",")

# for i in range(len(a)):
#     a[i] = int(a[i])

# print(singleNumber(a))

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


# for i in range(1, 11):
#     arr = []
#     length = random.randint(1, 100)
#     for j in range(length):
#         arr.append(random.randint(1, 100))
#     id = random.randint(0, length-1)
#     print(arr[id])
#     for j in range(length):
#         if (j != id):
#             arr.append(arr[j])
    
#     f = open(f"./testcases/Bonus2/{i}.in", "w")
#     f.write(f"{len(arr)}\n")
#     f.write(f"{arr[0]}")
#     for j in range(1, len(arr)):
#         f.write(f", {arr[j]}")
#     f.close()

#     f = open(f"./testcases/Bonus2/{i}.out", "w")
#     ans = singleNumber(arr)
#     f.write(str(ans))
#     f.close()

# score = []
# for i in range(5):
#     score.append(int(input()))
# a = input()

# def check(score, a):
#     if (a == "會計系"):
#         summ = score[0] + score[1] + score[2] + score[3]
#         if (summ >= 57 and score[0] >= 15):
#             return 1
#         return 0
#     elif (a == "公衛系"):
#         summ = score[1] + score[2] + score[4]
#         if (summ >= 38):
#             return 1
#         return 0
#     elif (a == "經濟系"):
#         summ = score[3] + score[4]
#         if (summ >= 26 and score[2] >= 15):
#             return 1
#         return 0

#     elif (a == "資管系"):
#         summ = score[1] + score[4]
#         if (summ >= 27 and score[2] >= 15 ):
#             return 1
#         return 0

# print(check(score, a))

# for i in range(2, 11):
#     f = open(f"./testcases/Q1/{i}.in", "w", encoding='utf-8')
#     score = []
#     for j in range(5):
#         score.append(random.randint(1, 15))
#         f.write(f"{score[j]}\n")
#     a = random.randint(1, 4)
#     if (a == 1):
#         a = "會計系"
#         f.write("會計系")
#     elif (a == 2):
#         a = "公衛系"
#         f.write("公衛系")
#     elif (a == 3):
#         a = "經濟系"
#         f.write("經濟系")
#     elif (a == 4):
#         a = "資管系"
#         f.write("資管系")
#     f.close()

#     f = open(f"./testcases/Q1/{i}.out", "w")
#     ans = check(score, a)
#     f.write(f"{ans}")
#     f.close()

# print(check([4, 14, 15, 15, 14], "經濟系"))
# print(check([8, 15, 15, 13, 12], "資管系"))