"""
Write a function that takes a string of braces, and determines
if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.
This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [],
and curly braces {}. Thanks to @arnedag for the idea!
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
"""
# Code
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s: # while there are braces in the string
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s=='' # if the string is empty, return True
# Test 1,2,3:
print(validBraces( "()" )) # True
print(validBraces( "[(])" )) # False
print(validBraces( "([{}])" )) # True