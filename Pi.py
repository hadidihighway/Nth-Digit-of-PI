import mpmath
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

def nth_digit_of_pi(n):
    mpmath.mp.dps = n + 1
    pi_string = str(mpmath.pi)
    return pi_string[n]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Nth Digit Of Pi")
        
        layout = QVBoxLayout()
        label = QLabel("Enter the Positive Nth Digit of Pi")
        layout.addWidget(label,alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.position_input = QLineEdit()
        self.position_input.setPlaceholderText("Enter Position")

        self.calculate_button = QPushButton("Find digit")
        self.calculate_button.clicked.connect(self.on_calculate_clicked) 

        self.result_label = QLabel("Result will appear here")
        
        layout.addWidget(self.position_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label, alignment=Qt.AlignmentFlag.AlignHCenter)
      
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.calculate_button.setFont(font)
        font.setPointSize(12)
        self.result_label.setFont(font)
        font.setPointSize(20)
        label.setFont(font)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)
        self.setMinimumSize(400, 200)

    def on_calculate_clicked(self):
        
        text = self.position_input.text().strip()
        try:
            n = int(text)
        except ValueError:
            self.result_label.setText("Enter a valid whole number")
            return
        digit = nth_digit_of_pi(n)
        self.result_label.setText(f"Digit {n} of Pi is: {digit} ")







if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()