import os
import subprocess
import time
from PIL import Image
import io
import pyperclip
import win32clipboard
import pyautogui


def paste_image_to_typora(typora_path=r'E:\MyDown\Typora\Typora.exe', image_path=r'img.jpg'):
    def copy_image_to_clipboard(image_path):
        try:
            image = Image.open(image_path)
            output = io.BytesIO()
            image.convert('RGB').save(output, 'BMP')
            data = output.getvalue()[14:]
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
            win32clipboard.CloseClipboard()
            print("Image copied to clipboard.")
        except Exception as e:
            print(f"Error: {e}")

    try:
        typora_process = subprocess.Popen([typora_path])
        print("Typora opened.")
        time.sleep(2)
        copy_image_to_clipboard(image_path)
        pyautogui.hotkey('ctrl', 'v')
        print("Image pasted in Typora.")

        # Close Typora window
        time.sleep(5)

        os.system("taskkill /f /im Typora.exe")
        print("Typora closed.")
    except Exception as e:
        print(f"Error: {e}")


# 调用函数
# if __name__ == "__main__":
paste_image_to_typora()
