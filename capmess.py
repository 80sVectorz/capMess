import random
import string
import os,sys,time

print('''
*-------------*
####CAPmESs####
*-------------*
''')

#-----PARAMETERS-----
chance = 0.5 #how much chance there is that the letter will be lower case
#--------------------


def on_press(k):
    global pressing,chance,os,dev,keyboard 
    try: 
        if os == 'windows': 
            if GetKeyState(VK_CAPITAL) > 0 and k.char in string.ascii_lowercase:
                if random.random() < chance: 
                    pressing.append(True) 
                    keyboard.tap(Key.backspace)
                    keyboard.press(Key.shift)
                    keyboard.tap(k.char)
                    keyboard.release(Key.shift)
        elif os == 'linux':
            if 1 in dev.leds() and k.char in string.ascii_lowercase:
                if random.random() < chance:
                    pressing.append(True)
                    time.sleep(0.1)
                    keyboard.tap(Key.backspace)
                    keyboard.press(Key.shift)
                    keyboard.tap(k)
                    keyboard.release(Key.shift)
    except:
        pass
def on_release(k):
    global pressing,os  
    try:
        if os == "windows":
            if len(pressing)!=0 and k.char in string.ascii_lowercase:
                pressing.pop(0)
        elif os == "linux":
            if len(pressing)!=0 and k.char in string.ascii_lowercase:
                pressing.pop(0)
    except:
        pass
pressing=[]

os = None
#Check if os is linux or windows
if sys.platform == 'win32':
    print('Windows detected')
    os = 'windows'
    from win32api import GetKeyState 
    from win32con import VK_CAPITAL
    from pynput.keyboard import Key, Listener, Controller
    keyboard = Controller()

    # Collect events until released
    with Listener(
        on_press=on_press,on_release=on_release) as listener:
        listener.join()

elif sys.platform == 'linux':
    print('Linux detected')
    os = 'linux'
    from pynput.keyboard import Key, Listener, Controller
    from evdev import InputDevice, categorize, ecodes
    dev = InputDevice('/dev/input/event3')
    keyboard = Controller()
    with Listener(
        on_press=on_press,on_release=on_release) as listener:
        listener.join()
else:
    os = 'mac'
    print('MacOS is not supported')
    exit()
