# X形准心程序 Xrosshair

## 概述
该程序在您的屏幕上创建一个准心覆盖，用于辅助 FPS（第一人称射击）游戏中的瞄准。准心由两条对角线交于屏幕中心组成。程序支持多种自定义功能，包括颜色、粗细调整和多显示器支持。

---

## 功能

### 1. **准心显示**
- 程序在屏幕上绘制两条交于中心的对角线。
- 准心始终显示在所有窗口的最前端。

### 2. **线条粗细调整**
- 使用 `+` 或 `=` 键增加准心线条的粗细。
- 使用 `-` 或 `_` 键减少线条粗细（最小粗细：1）。

### 3. **颜色自定义**
- 按 `Shift + C` 切换准心颜色，颜色选项包括：
  - 红色
  - 绿色
  - 蓝色
  - 黄色
  - 黑色
  - 白色

### 4. **多显示器支持**
- 如果连接了多个显示器，可以使用 `Shift + A` 快捷键在显示器之间切换准心。
- 切换显示器后，准心会保持居中并正确对齐。


### 5. **隐藏命令行窗口**
- 在 Windows 系统上运行时，程序启动后会隐藏命令行窗口。

---

## 环境要求
- Python 3.6+
- PyQt5 库

使用以下命令安装 PyQt5：
```
pip install PyQt5
```

---

## 如何运行
1. 确保已满足所有环境要求。
2. 将程序代码保存为文件（例如 `crosshair.py`）。
3. 运行程序：
   ```
   python crosshair.py
   ```

---

## 使用方法
1. 启动程序，准心会出现在主显示器上。
2. 使用以下快捷键来自定义准心：

   | 快捷键          | 功能                                 |
   |-----------------|-------------------------------------|
   | `+`       | 增加线条粗细                        |
   | `-`       | 减少线条粗细                        |
   | `Shift + C`     | 更改准心颜色                        |
   | `Shift + A`     | 切换准心到下一个显示器              |

3. 鼠标靠近准心线条时，准心会暂时隐藏。
4. 关闭覆盖窗口即可退出程序。

---

## 注意事项
- 请确保您的游戏或应用程序运行在窗口模式或无边框模式下以保证兼容性。
- 本程序仅供个人使用，请勿用于在竞争环境中获得不公平的优势。

---

## 常见问题

### 准心未显示
- 确保程序正在运行。
- 验证您的显示器设置是否被系统正确识别。

### 快捷键无效
- 确保程序窗口处于激活状态（如有必要，点击覆盖窗口区域）。
- 检查键盘布局，使用非标准键盘设置时请尝试替代键。

### 鼠标光标未隐藏准心
- 确保鼠标光标足够接近准心线条。
- 调整准心线条粗细以便更容易检测。

---

## 许可
该程序仅供个人使用。允许进行修改和再分发。作者不对因使用该软件造成的任何不当行为负责。



# Xrosshair: X-Shaped crosshair

## Overview
This program creates a crosshair overlay on your screen to assist with aiming in FPS (First-Person Shooter) games. The crosshair consists of two diagonal lines intersecting at the center of the screen. The program supports various customization features, including color adjustment, line thickness control, and multi-monitor support.

---

## Features

### 1. **Crosshair Display**
- Displays two diagonal lines crossing at the center of the screen.
- The crosshair remains on top of all windows.

### 2. **Line Thickness Adjustment**
- Use the `+` or `=` key to increase the crosshair line thickness.
- Use the `-` or `_` key to decrease the line thickness (minimum thickness: 1).

### 3. **Customizable Colors**
- Press `Shift + C` to cycle through crosshair colors. Available options are:
  - Red
  - Green
  - Blue
  - Yellow
  - Black
  - White

### 4. **Multi-Monitor Support**
- If multiple monitors are connected, use the `Shift + A` hotkey to switch the crosshair to a different monitor.
- The crosshair will remain centered and properly aligned on the new monitor.

### 5. **Auto-Hide on Cursor Hover**
- When the mouse cursor moves close to the crosshair, the crosshair will automatically hide.
- The crosshair will reappear when the mouse moves away.

### 6. **Hidden Command Prompt**
- On Windows, the program will hide the command prompt window upon startup.

---

## Requirements
- Python 3.6+
- PyQt5 library

Install PyQt5 with the following command:
```
pip install PyQt5
```

---

## How to Run
1. Ensure all requirements are met.
2. Save the program code as a file (e.g., `crosshair.py`).
3. Run the program:
   ```
   python crosshair.py
   ```

---

## Usage
1. Start the program, and the crosshair will appear on the primary monitor.
2. Use the following hotkeys to customize the crosshair:

   | Hotkey           | Function                              |
   |------------------|---------------------------------------|
   | `+` / `=`        | Increase line thickness               |
   | `-` / `_`        | Decrease line thickness               |
   | `Shift + C`      | Change crosshair color                |
   | `Shift + A`      | Switch crosshair to the next monitor  |


3. Close the overlay window to exit the program.

---

## Notes
- Ensure your game or application runs in windowed or borderless mode for compatibility.
- This program is intended for personal use. Avoid using it in competitive environments to gain an unfair advantage.

---

## FAQ

### Crosshair Not Displayed
- Ensure the program is running.
- Verify that your monitor setup is correctly recognized by the system.

### Hotkeys Not Working
- Make sure the program window is active (click the overlay area if necessary).
- Check your keyboard layout. If using a non-standard keyboard, try alternate keys.

### Cursor Does Not Hide Crosshair
- Ensure the mouse cursor is close enough to the crosshair lines.
- Adjust the crosshair line thickness to make it easier to detect.

---

## License
This program is provided for personal use. Modifications and redistribution are allowed. The author is not responsible for any misuse of this software.
