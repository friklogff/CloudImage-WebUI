import os
import subprocess
import time
from PIL import Image
import io
import pyperclip
import win32clipboard
import pyautogui


def copy_image_to_clipboard(image_path):
    try:
        # 打开图片
        image = Image.open(image_path)
        # 将图片转换为二进制数据
        output = io.BytesIO()
        image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]  # BMP文件头14字节需要被移除
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        print("Image copied to clipboard.")
    except Exception as e:
        print(f"Error: {e}")


def open_typora(typora_path):
    try:
        # 启动 Typora
        subprocess.Popen([typora_path])
        print("Typora opened.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Typora 路径
    typora_path = r'E:\MyDown\Typora\Typora.exe'
    # 图片路径
    image_path = r'img.png'

    # 打开 Typora
    open_typora(typora_path)
    # 等待 Typora 打开
    time.sleep(5)  # 等待时间可以根据实际情况调整
    # 复制图片到剪贴板
    copy_image_to_clipboard(image_path)
    # 等待图片复制完成
    time.sleep(1)  # 等待时间可以根据实际情况调整
    # 在 Typora 中粘贴图片
    pyautogui.hotkey('ctrl', 'v')
    print("Image pasted in Typora.")


if __name__ == "__main__":
    main()