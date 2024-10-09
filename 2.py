import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取视频
cap = cv2.VideoCapture(r"C:\Users\huangshaozheng\Desktop\major.mp4")  # 打开视频文件
fps = cap.get(cv2.CAP_PROP_FPS)
frames = []

# 提取每一帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# 使用 Canny 边缘检测和提取轮廓
key_data = []

for frame in frames:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)  # 应用高斯模糊
    edges = cv2.Canny(gray, 50, 150)  # 调整Canny边缘检测的阈值
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 提取所有轮廓
    key_data.append(contours)

# 使用 Matplotlib 动态绘制边缘轮廓
plt.ion()  # 开启交互模式
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('white')  # 白色背景

# 计算图像的范围
height, width = frames[0].shape[:2]

for contours in key_data:
    ax.clear()  # 清除当前图形
    ax.set_facecolor('white')  # 设置背景为白色

    # 绘制所有轮廓，设置较小的点大小
    for contour in contours:
        ax.plot(contour[:, 0, 0], contour[:, 0, 1], 'ko', markersize=1)  # 黑色轮廓点，点大小设置为1

    ax.set_xlim(0, width)  # 设置x轴范围
    ax.set_ylim(height, 0)  # 设置y轴范围，y轴反转

    plt.pause(1 / fps)  # 等待相应的时间以保持帧率

plt.ioff()  # 关闭交互模式
plt.show()  # 显示最后一帧
