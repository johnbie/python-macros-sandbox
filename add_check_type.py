import pyautogui
import time
import winsound
import tkinter as tk
from tkinter import simpledialog

def get_inputs():
    root = tk.Tk()
    root.withdraw()
    
    num_repeats = simpledialog.askinteger("Number of repeats", "How many times do you want to repeat the input?", parent=root, minvalue=1)
    num_skips = simpledialog.askinteger("Number of repeats", "How many times do you want to go down?", parent=root, minvalue=1)
    #message = simpledialog.askstring("Message", "What is the message you want to type?", parent=root) + ' '
    return (num_repeats, num_skips)

def main():
    num_repeats, num_skips = get_inputs()
    
    for i in range(num_repeats):
        pyautogui.press('f2')
        time.sleep(1/2)
        pyautogui.press('left')
        pyautogui.typewrite('Pass ')
        pyautogui.press('enter')
        time.sleep(1/4)
        pyautogui.press('f2')
        time.sleep(1/2)
        pyautogui.press('left')
        pyautogui.typewrite('Fail ')
        pyautogui.press('enter')
        time.sleep(1/4)
    
    winsound.Beep(440, 1000)
    print("Finished typing the message.")

if __name__ == '__main__':
    main()