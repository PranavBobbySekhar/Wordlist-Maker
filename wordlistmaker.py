import os

digit_types = []
iteration = 0
indentation_count = 0
password = ""

passdigits = input('How many digits does the password have: ')

for i in range(int(passdigits)):
	digit_types.append(input(f'What is digit number {i + 1} (Uppercase, Lowercase, Symbol, Digit): ').lower())

with open('wordlistmaker_orig.py', 'w') as f:
	f.write('''import string\n
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digit = string.digits
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
passwords = 0\n\n
with open('wordlist.txt', 'w') as f:\n''')
indentation_count = 1

with open('wordlistmaker_orig.py', 'a') as g:
	for digit in digit_types:
		iteration += 1
		password += "{" + f"_{iteration}" + "}"
		indentation = "\t" * indentation_count
		g.write(f'{indentation}for _{iteration} in {digit}:\n')
		indentation_count += 1
	indentation = "\t" * indentation_count
	g.write(f'''{indentation}f.write(f"{password}\\n")
{indentation}passwords += 1
	print(f"{{passwords}} passwords written to wordlist.txt")''')

import wordlistmaker_orig
os.remove('wordlistmaker_orig.py')
