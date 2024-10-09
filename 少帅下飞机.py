import cv2  # 导入 OpenCV 库

cap = cv2.VideoCapture(r"C:\Users\huangshaozheng\Desktop\major.mp4")  # 打开视频文件

import numpy as np  # 导入 NumPy 库
import time  # 导入时间库
import tkinter as tk  # 导入 Tkinter 库，用于创建 GUI
from tkinter import scrolledtext  # 从 Tkinter 导入滚动文本框

chars = ['#', 'S', '0', 'B', '+', '=', 'O', 'o', '8']  # 定义字符集

display_width = 450  # 设置显示宽度
display_height = 130  # 设置显示高度


def frame_to_ascii(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将帧转换为灰度图像
    small_frame = cv2.resize(gray, (display_width, display_height))  # 调整图像尺寸
    ascii_frame = ''.join(chars[min(pixel // (256 // len(chars)), len(chars) - 1)] for pixel in small_frame.flatten())
    return '\n'.join([ascii_frame[i:i + display_width] for i in range(0, len(ascii_frame), display_width)])


root = tk.Tk()  # 创建主窗口
root.title("少帅下飞机 Python 版")  # 设置窗口标题
root.configure(bg='white')  # 设置背景颜色

text_area = scrolledtext.ScrolledText(root, width=display_width, height=display_height, font=("Courier", 4), bg='white',
                                      fg='black')
text_area.pack()  # 添加文本框


def update_display():
    ret, frame = cap.read()  # 读取视频帧
    if not ret:
        cap.release()  # 释放视频对象
        return
    ascii_art = frame_to_ascii(frame)  # 转换为 ASCII 艺术
    text_area.delete(1.0, tk.END)  # 清空文本框
    text_area.insert(tk.END, ascii_art)  # 更新文本框
    root.after(int(1000 / 30.70), update_display)  # 更新显示


update_display()  # 启动更新
root.mainloop()  # 运行 Tkinter 循环