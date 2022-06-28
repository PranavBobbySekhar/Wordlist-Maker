import os

def makepasslist():
	
	allowed_digit_types = ['uppercase', 'lowercase', 'number', 'symbol']
	digit_types = []
	iteration = 0
	indentation_count = 0
	password = ""
	
	passdigits = input('How many digits does the password have: ')
	
	try:
		if int(passdigits) >= 7:
			print('\nWarning: May take some time because the password is longer than 6 digits\n')
			
		if int(passdigits) < 1:
			print('\nValue must be greater than 0\n')
			return
			
	except ValueError:
		print("\nValue must be an integer\n")
		return

	for i in range(int(passdigits)):
		digit = input(f'What is digit number {i + 1} (Uppercase, Lowercase, Symbol, Digit): ')
		if digit.lower() in allowed_digit_types:
				digit_types.append(digit.lower())
		else:
			print('\nThe available digit types are - Uppercase(A, B, C), Lowercase(a, b, c), Symbol(!, @, #), and Number(1, 2, 3). Please choose from these.\n')
			return

	with open('passlistmaker.py', 'w') as f:
		f.write('''import string\n
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
number = string.digits
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
passwords = 0\n\n
with open('wordlist.txt', 'w') as f:\n''')
	indentation_count = 1

	with open('passlistmaker.py', 'a') as g:
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

	import passlistmaker
	os.remove('passlistmaker.py')

def makenumlist():
	startnum = input('Enter number to start from: ')
	endnum = input('Enter number to end with: ')
	try:
		numstowrite = (int(endnum) - int(startnum)) + 1
	except ValueError:
		print('Please enter an Integer')
		return
	currentnum = int(startnum)
	numswritten = 0
	with open('wordlist.txt', 'w') as f:
		for i in range(numstowrite):
			f.write(f'{currentnum}\n')
			currentnum += 1
			numswritten += 1
	print(f'{numswritten} numbers wrote to wordlist.txt')
