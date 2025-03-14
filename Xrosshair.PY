import sys
import os

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtGui import QPainter, QPen
    from PyQt5.QtCore import Qt, QTimer
except ModuleNotFoundError as e:
    print("Error: PyQt5 is not installed. Please install it using 'pip install PyQt5' and try again.")
    sys.exit(0)

class CrosshairOverlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self.screens = QApplication.screens()
        self.current_screen_index = 0
        self.update_screen_geometry()

        # Initialize crosshair properties
        self.pen_width = 5  # Default to a thicker line for easier selection
        self.pen_color = Qt.red
        self.colors = [Qt.red, Qt.green, Qt.blue, Qt.yellow, Qt.black, Qt.white]
        self.current_color_index = 0

        self.show()

    def update_screen_geometry(self):
        screen_geometry = self.screens[self.current_screen_index].geometry()
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()
        self.setGeometry(
            screen_geometry.x(), screen_geometry.y(), self.screen_width, self.screen_height
        )
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(self.pen_color)
        pen.setWidth(self.pen_width)
        painter.setPen(pen)

        # Draw the crosshair: two diagonal lines
        painter.drawLine(0, 0, self.screen_width, self.screen_height)  # Top-left to bottom-right
        painter.drawLine(0, self.screen_height, self.screen_width, 0)  # Bottom-left to top-right

    def keyPressEvent(self, event):
        # Adjust line thickness with +/- keys
        if event.key() == Qt.Key_Plus or event.key() == Qt.Key_Equal:  # For + and = keys
            self.pen_width += 1
            self.update()
        elif event.key() == Qt.Key_Minus or event.key() == Qt.Key_Underscore:  # For - and _ keys
            self.pen_width = max(1, self.pen_width - 1)  # Minimum width of 1
            self.update()
        # Change color with Shift+C
        elif event.key() == Qt.Key_C and event.modifiers() == Qt.ShiftModifier:
            self.current_color_index = (self.current_color_index + 1) % len(self.colors)
            self.pen_color = self.colors[self.current_color_index]
            self.update()
        # Switch screen with Shift+A
        elif event.key() == Qt.Key_A and event.modifiers() == Qt.ShiftModifier:
            self.current_screen_index = (self.current_screen_index + 1) % len(self.screens)
            self.update_screen_geometry()
            self.correct_crosshair_position()

    def correct_crosshair_position(self):
        # Ensure the crosshair remains centered after switching screens
        screen_geometry = self.screens[self.current_screen_index].geometry()
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()
        self.setGeometry(
            screen_geometry.x(), screen_geometry.y(), self.screen_width, self.screen_height
        )
        self.update()

if __name__ == "__main__":
    try:
        # Hide the console window (Windows specific)
        if os.name == 'nt':
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

        app = QApplication(sys.argv)
        crosshair = CrosshairOverlay()

        # Ensure the mouse doesn't move unexpectedly by avoiding unnecessary raise calls
        def keep_on_top():
            if not crosshair.isActiveWindow():
                crosshair.raise_()

        # Add a timer to keep it responsive and always on top
        timer = QTimer()
        timer.timeout.connect(keep_on_top)
        timer.start(100)

        sys.exit(app.exec_())
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(0)
