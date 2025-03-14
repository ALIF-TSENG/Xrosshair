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

