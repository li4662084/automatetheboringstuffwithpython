import re

numberRegex = re.compile(r'[0-9]')
letterRegex = re.compile(r'^[a-zA-Z]')
upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
specialRegex = re.compile(r'[.^$*+?{}\[\]\|()\s]')

def checkStrong(password):
	if len(password) > 7 and len(password) < 16:
		if numberRegex.search(password) and letterRegex.search(password) \
		and upperRegex.search(password) and lowerRegex.search(password) \
		and specialRegex.search(password) == None:
			print('The password is strong!')
		else:
			print('''The password is not strong!It needs both uppercase and 
lowercase characters, and has at least one digit.
You need use letter in the first place, and no special characters.''')
	elif len(password) > 16:
		print("The password can't overtake 16 characters.")
	else:
		print('''The password needs 8 characters at least!It needs both uppercase and 
lowercase characters, and has at least one digit.
You need use letter in the first place, and no special characters.''')

checkStrong('Ily0426.')