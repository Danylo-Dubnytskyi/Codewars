"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
The binary number returned should be a string.
"""
#Code
def add_binary(a,b):
    return bin(a+b)[2:] # convert the sum of a and b to binary
# Test 1,2,3:
print(add_binary(1,1)) # 10
print(add_binary(0,1)) # 1
print(add_binary(1,0)) # 1
