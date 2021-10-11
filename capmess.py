from win32api import GetKeyState 
from win32con import VK_CAPITAL 
import random
import string
from pynput.keyboard import Key, Listener, Controller
keyboard = Controller()

pressing=[]

def on_press(key):
	global pressing
	try:
		if GetKeyState(VK_CAPITAL) > 0 and key.char in string.ascii_lowercase:
			print(key)
			if random.random() > 0.4:
				pressing.append(True)
				keyboard.press(Key.backspace)
				keyboard.release(Key.backspace)
				keyboard.press(Key.shift)
				keyboard.press(key)
				keyboard.release(key)
				keyboard.release(Key.shift)
	except:
		pass
			
def on_release(key):
	global pressing
	try:
		if len(pressing)!=0 and key.char in string.ascii_lowercase:
			pressing.pop(0)
	except:
		pass

# Collect events until released
with Listener(
		on_press=on_press,on_release=on_release) as listener:
	listener.join()
	