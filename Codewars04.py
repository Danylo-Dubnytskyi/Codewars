"""
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.
"""
#Code
def pig_it(text):
    new_list = []
    for i in text.split():
        if i.isalpha(): # if the word is a letter
            new_list.append(i[1:] + i[0] + "ay")
        else: # if the word is a punctuation mark
            new_list.append(i)
    return " ".join(new_list)
# Test 1,2,3:
print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
print(pig_it('This is my string')) # hisTay siay ymay tringsay
print(pig_it('Hello world !')) # elloHay orldway !
