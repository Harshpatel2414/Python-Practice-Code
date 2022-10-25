letter = '''
Hello <|Name|>, 
\tGood Morning.
\tHow can i help you!
'''
name = input("Enter your name : ")
letter = letter.replace("<|Name|>",name)
print(letter)