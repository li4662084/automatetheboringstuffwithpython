from pyinputplus import *

message = ''

def sandwich_maker():
	global message
	print('Choose a bread type')
	bread_type = inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
	print('Choose a protein type')
	protein_type = inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
	cheese_choice = inputYesNo('Do you want cheese?')
	if cheese_choice == 'yes':
		print('Choose a cheese type')
		cheese_type = inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
		message = 'Your sandwiches cost :' + '\n' + bread_type + '\n' + \
			protein_type + '\n' + cheese_type + '\n'
	elif cheese_choice == 'no':
		message = 'Your sandwiches cost' + '\n' + bread_type + '\n' + \
		protein_type + '\n'

	def choice(items):
		for item in items:
			global message

			choose = inputYesNo(f'Do you want {item}?')
			if choose == 'yes':
				message = message + item + '\n'

	choice(['mayo', 'mustard', 'lettuce', 'tomato'])

	numberOfSandwiches = inputInt('How many sandwiches do you want?', min=1)

	message = message + 'You want ' + str(numberOfSandwiches) + ' sandweiches.'

	print(message)

sandwich_maker()