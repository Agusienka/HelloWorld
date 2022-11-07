def max_num(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


print(max_num(10, 15, 17))


def mult_list(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(mult_list((8, 2, 3, -3, 9, 20)))


# Function to reverse a string
def rev_string(string):
    return string[::-1]  # negative step argument to reverse the sequence using extended slice syntax


s = "Hello how are you doing today?"

print("The original string is: ", end="")  # end parameter to sort of concatenate both print statements on one line
print(s)

print("The reversed string is: ", end="")
print(rev_string(s))


def num_within(a, b, c):
    return a in range(b, c + 1)


print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))


# Print Pascal's Triangle in Python

def pascal(num_rows):
    for i in range(num_rows):
        print(""*(num_rows - i), end='')
        print(' '.join(str(11 ** i)))


pascal(5)
pascal(7)
