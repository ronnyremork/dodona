# def diff21(n):
#     if n>21:
#         return (21-n)*2
#     else:
#         return (21-n)
# # main
#
# n = int(input('Number: '))
#
# def parrot_trouble(talking, hour):
#   for hour in range (23):
#     if hour < 7 and hour > 20 and talking == True:
#       return True
#     else:
#       return False

# def makes10(a, b):
#   if a+b==10 or a==10 or b==10:
#     return True
#   else:
#     return False

# def near_hundred(n=-110):
#     if abs(n) in range(90,111) or abs(n) in range (190,211 ):
#         return True
#     else:
#         return False
#
# print(near_hundred())

# def missing_char(str='hoi', n=0):
#    new_str = str[:n] + str[(n+1):]
#    return new_str
#
# print(missing_char())

# def front_back(str='code'):
#    if len(str)< 1 :
#        return str
#    mid = str[1:len(str)-1]
#    new_str = str[len(str)-1]+mid+str[0]
#    return new_str
#
# print(front_back())

# def front3(str='hallo'):
#   if len(str)-1 < 3:
#     return str
#   else:
#     str_new = str[0:3]+str[0:3]+str[0:3]
#   return str_new
#
# print(front3())

# def string_times(str='Hi', n=3):
#     new_str = str
#     for i in range(n):
#         new_str+=str
#     return new_str
#
# print(string_times())

# def string_splosion(str='code'):
#   i=len(str)
#   str_2=''
#   while i >=0:
#     str_2 += str[0:(len(str)-i)]
#     i-=1
#   return str_2
#
# print(string_splosion())

# def last2(str='hixxhi'):
#
#         c = 0
#         i = 0
#         while i < len(str) - 2:
#             a = 'str[i]'
#             if a == str[i + 1]:
#                 str_1 = str[i] + str[i + 1]
#                 if str.find(str_1,0,len(str)-1):
#                     c+=1
#             i += 1
#
#         return c
# print(last2())

# c = 0
# i = 0
# while i < len(str) - 2:
#     a = 'str[i]'
#     if a == str[i + 1]:
#         str_1 = str[i] + str[i + 1]
#         str.find
# a = str[i]
# i += 1
# return c


# def last2(str):
#     if len(str) < 2
#         return 0
#     last2 = str[len(str) - 1:]
#     count = 0
#
#     for i in range(len(str) - 2):
#         sub = str[i:i + 2]
#         if sub == last2:
#             count += 1
#     return count

# def array123(nums):
#     for i in range(len(nums)-2):
#       if nums[i]==1:
#         if nums[i+1] == 2:
#           if nums[i+2] == 3:
#             return True
#     return False
#
# nums  = [1,1,2,1,2,3]
# print(array123(nums))
# def string_match(a='aabbccdd',b='abbbxxd'):
#     count=0
#     for i in range(len(a)-1):
#         sub_str = a[i]+a[i+1]
#         print(sub_str)
#         if sub_str in b:
#             count+=1
#
#     return count

# def front_times(str='Choco', n=3):
#   c = 0
#   result=''
#   if len(str)<3:
#     front = len(str)+1
#     output=str[0:front]
#   else:
#     output=str[0:3]
#   while c < n :
#     result+=output
#     c+=1
#   return result

# def make_bricks(small=3, big=1, goal=9):
#     i = 0
#     lb = 5
#     ls = 1
#     tb = lb*big
#     ts = ls*small
#     total = tb + ts
#     if goal > total or goal < ts:
#         return False
#     if (tb < goal and total+ts>= goal)  or ts==goal or tb == goal:
#         return True
#     elif (tb> goal):
#         while i < (big-1):
#             if (lb*i)+ts==goal:
#                 return True
#             i+=1

# def make_bricks(small=2, big=1000000, goal=100003):
#     i = 0
#     lb = 5
#     ls = 1
#     tb = lb*big
#     ts = ls*small
#     total = tb + ts
#     if goal > total or goal < ts:
#         return False
#     if (tb < goal and total >= goal)  or ts==goal or tb == goal:
#         return True
#     elif (tb> goal):
#         while i <= (big-1):
#             if (lb*i)<=goal and (goal-(lb*i))<=ts:
#                 return True
#             i+=1
#
#     return False

# def lone_sum(a=3,b=2,c=2):
#     sum = 0
#     if a != b != c != a:
#         sum = a+b+c
#     elif a == b == c:
#         sum = 0
#     elif a == b and b != c:
#         sum == c
#     elif a != b and b == c:
#         sum == b
#     elif a == c and c != b:
#         sum = b
#     return sum
#
# print(lone_sum())
 print(abs(5-3))
