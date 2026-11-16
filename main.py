import random
import sys
from PyQt6.QtCore import QRect
from PyQt6.QtGui import QBrush, QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setWindowTitle("Случайные окружности")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(220, 20, 160, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Нарисовать")

        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 150)
        max_x = max(0, self.width() - diameter)
        max_y = max(70, self.height() - diameter)
        x = random.randint(0, max_x)
        y = random.randint(70, max_y) if max_y > 70 else 0
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.circles:
            return
        qp = QPainter(self)
        for x, y, diameter, color in self.circles:
            qp.setBrush(QBrush(color))
            qp.drawEllipse(x, y, diameter, diameter)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())