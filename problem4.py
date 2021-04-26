# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0
i = 100
while i < 999:
    j = 100
    while j < 999:
        num = i * j
        if num > largest:
            string = str(num)
            rev_string = ''
            k = len(string)-1
            while k >= 0:
                rev_string += string[k]
                k -= 1
            if rev_string == string:
                # print("string: ", string, " rev_string: ", rev_string )
                largest = num
        j +=1
    i += 1

print(largest)