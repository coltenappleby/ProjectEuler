# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 10

# while i > 0:
#     print(2520//i)
#     i-=1

go = True
i = 0
while(go):
    num = 20
    while num > 0:
        # print("inside second while: ", num)
        if num == 1:
            go = False
        elif(i%num):
            num -= 1
            continue
        else:
            print('in else; i: ', i)
            break
    i +=1
print(i)

    