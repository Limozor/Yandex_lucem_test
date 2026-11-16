import random
import sys
from PyQt6 import uic
from PyQt6.QtGui import QBrush, QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 150)
        max_x = max(0, self.width() - diameter)
        max_y = max(70, self.height() - diameter)
        x = random.randint(0, max_x)
        y = random.randint(70, max_y) if max_y > 70 else 0
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.circles:
            return
        qp = QPainter(self)
        qp.setBrush(QBrush(QColor(255, 255, 0)))
        for x, y, diameter in self.circles:
            qp.drawEllipse(x, y, diameter, diameter)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())