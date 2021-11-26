import pyautogui

def take_screenshot():
    s_s = pyautogui.screenshot()
    s_s.save('C:\\Users\\hp\\Videos\\Captures')

if __name__ == "__main__":
    take_screenshot()