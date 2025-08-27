import subprocess
import sys

package_name = "pynput" # Replace with the package you want to install


try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
except subprocess.CalledProcessError as e:
            print(f"Error installing {package_name}: {e}")




from pynput import keyboard
import time

# Create a keyboard controller object
keyboard_controller = keyboard.Controller()

# windows key + R
keyboard_controller.press(keyboard.Key.cmd)   
keyboard_controller.press('r')               
time.sleep(0.1)                               
keyboard_controller.release('r')              
keyboard_controller.release(keyboard.Key.cmd) 

#deleats whats in it

keyboard_controller.press(keyboard.Key.ctrl_l)
keyboard_controller.press(keyboard.Key.backspace)
time.sleep(0.1)
keyboard_controller.release(keyboard.Key.backspace)
keyboard_controller.release(keyboard.Key.ctrl_l)

#opens notepad
keyboard_controller.type("notepad")
keyboard_controller.press(keyboard.Key.enter) 
time.sleep(0.5)

#makes new notepad
keyboard_controller.press(keyboard.Key.ctrl_l)
keyboard_controller.press('t')
time.sleep(0.1)
keyboard_controller.release(keyboard.Key.backspace)
keyboard_controller.release('t')
time.sleep(0.5)

#types "poop"
keyboard_controller.type("POOP!!!!")

#saves

keyboard_controller.press(keyboard.Key.ctrl_l)
keyboard_controller.press('s')
time.sleep(0.1)
keyboard_controller.release('s')
keyboard_controller.release(keyboard.Key.ctrl_l)
time.sleep(0.3)
keyboard_controller.press(keyboard.Key.enter)
keyboard_controller.release(keyboard.Key.enter)

