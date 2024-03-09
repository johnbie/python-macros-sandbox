import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog

def main():
    root = tk.Tk()
    num_repeats = simpledialog.askinteger("Number of repeats", "How many times do you want to repeat the input?", parent=root, minvalue=1)
    message = simpledialog.askstring("Message", "What is the message you want to type?", parent=root)
    root.destroy()

    for i in range(num_repeats):
        pyautogui.press('f2')
        time.sleep(1/8)
        pyautogui.press('right')
        pyautogui.keyDown('ctrl')
        pyautogui.press('left')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')
        pyautogui.press('backspace')
        time.sleep(1/8)
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(1/8)
    print("Finished typing the message.")

if __name__ == '__main__':
    main()