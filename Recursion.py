# Python Recursion Programs

# Direct Recursion is when we call the function in the same function. Here's one example of direct recursion with a
# program of first 10 Natural numbers
def natural(n):
    if n <= 0:
        return
    print(n, end=' ')
    natural(n-1)
    return ''
print(natural(10))


# Indirect Recursion is when we call first function into another function and another function into the first function.
# Here's the example of indirect recursion with a program of first 10 Natural numbers
def natural(n):
    if n <= 0:
        return
    print(n, end=' ')
    natural_new(n-1)
    return ''
def natural_new(n):
    print(n, end=' ')
    natural(n-1)
    return ''
print(natural(10))


# Factorial of n numbers
def fact(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return x * fact(x-1)
print(fact(5))


# Sum of n natural numbers
def sum(x):
    if x == 0:
        return 0
    else:
        return x + sum(x-1)
print('The Sum of natural numbers: ', sum(10))


# Multiplication of two numbers
def mul(a, b):
    if b == 1:
        return a
    else:
        return a + mul(a, b-1)
print(mul(4, 12))


# Find the power of a number using recursion.
def power(a, b):
    if b == 1:
        return a
    return a * power(a, b-1)
print(power(9, 2))


# Find the length of a list using Recursion.
def len_list(list):
    if list == []:
        return 0
    return 1 + len_list(list[1:])

list = [1, 2, 3, 4, 5]
print(len_list(list))


# Find the sum of a list using Recursion.
def sum_list(list):
    if len(list) == 0:
        return 0
    return list[0] + sum_list(list[1:])

list = [1, 2, 3, 4, 5, 6]
print(sum_list(list))


# Count the number of digits in a number.
def count(n):
    if n < 10:
        return 1
    return 1 + count(n//10)
n = 12123
print('The number of digits in ', n, 'is', count(n))


# Find the sum of digits of a number recursively.
def sum_digits(n):
    if n < 10:  # We compare it to less than 10 because sum of digits cant be find out if there is only single digit.
        return n
    return int(n % 10) + sum_digits(n//10)
n = int(input('Enter the number of digits to find their sum: '))
print('Sum of digits: ', sum_digits(n))


# Print a string backwards using Recursion.
def string(text):
    try:
        print(text[-1], end='')
        return string(text[:-1])
    except IndexError:
        return ''
print(string("new york"))


# Find the first uppercase letter in a string.
def first_upper(str, i):
    l = len(str)
    if i >= l:
        return -1
    if str[i].isupper():
        return i
    if i < l:
        return first_upper(str, i+1)
str = input('Enter the length of the string: ')
index = first_upper(str, 0)
if index != -1:
    print('Found at index', index)
    print('And the character that is found is', str[index])
else:
    print('Not Found')


# Find the maximum element in an array.
def max_num(arr, l, maximum):
    if l == len(arr)-1:
        return maximum
    if l > 0:
        if arr[l] > maximum:
            maximum = arr[l]
    return max_num(arr, l+1, maximum)

arr = [10, 9, 15, 18, 7, 20, 12, 16]
l = 0
maximum = arr[0]
print(max_num(arr, l, maximum))


# Find the minimum element in an array.
def min_num(arr, l, minimum):
    if l == len(arr)-1:
        return minimum
    if l > 0:
        if arr[l] < minimum:
            minimum = arr[l]
    return min_num(arr, l+1, minimum)

arr = [10, 9, 15, 18, 7, 20, 12, 16]
l = 0
minimum = arr[0]
print(min_num(arr, l, minimum))


# Check whether the entered number is prime or not.
def prime(num, i):
    if i >= num:
        return 0
    if (num % i) == 0:
        return -1
    else:
        return prime(num, i+1)

num = int(input('Enter the number whether its prime or not: '))
n = prime(num, 2)
if n == 0:
    print(num, 'is a prime number')
elif n == -1:
    print(num, 'is not a prime number')


# Palindrome string using Recursion.
def palindrome(text):
    if len(text) <= 1:
        print('Palindrome')
    else:
        if text[0] == text[-1]:
            palindrome(text[1:-1])
        else:
            print('Not Palindrome')
    return ''
print(palindrome('malayalam'))
print(palindrome('racecar'))
print(palindrome('car'))


# Armstrong number using Recursion.
def armstrong(num):
    if num < 10:
        return num*num*num
    return (num % 10)*(num % 10)*(num % 10) + armstrong(num//10)
num = 153
sum = armstrong(num)
if sum == num:
    print(num, 'is an armstrong number')
else:
    print(num, 'is not an armstrong number')


