import cleverbotfree.cbfree
import sys
cb1 = cleverbotfree.cbfree.Cleverbot()
cb2 = cleverbotfree.cbfree.Cleverbot()

def init_chat():
	try:
		cb1.get_form()
	except:
		sys.exit()
	cb1.send_input('Hi.')

def continue_check():
	userInp = input('Continue conversation? [Y/n]  ').lower()
	if userInp == 'y':
		return True
	elif userInp == 'n':
		return False
	else:
		continue_check()

def chat():
	try:
		cb1.browser.get(cb1.url)
		cb2.browser.get(cb2.url)
	except:
		cb1.browser.close()
		cb2.browser.close()
		sys.exit()
	init_chat()
	i = 0
	while True:
		try:
			cb1.get_form()
			cb2.get_form()
		except:
			sys.exit()
		if i != 0 and i % 5 == 0 and not continue_check():
			break
		i += 1
		bot1 = cb1.get_response()
		print('Alice: ', bot1)
		cb2.send_input(bot1)
		bot2 = cb2.get_response()
		print('Bob: ', bot2)
		cb1.send_input(bot2)
	cb1.browser.close()
	cb2.browser.close()

chat()