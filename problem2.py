# # Javascript
# let fibArray = []
# sum = 0

# let num1 = 0
# let num2 = 1
# while(num1 < 100) {
#     let temp = num2 
#     num2 = num1 + num2
#     num1 = temp
#     if (num2%2 == 0) {
#         sum += num2
#     }
# }

#  Python


sum = 0
num1 =0
num2 =1
while num2 < 4000000:
    temp = num2
    num2 = num1 + num2
    num1 = temp
    if num2%2 == 0:
        sum += num2
print(sum)
