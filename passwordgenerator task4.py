import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit, QWidget


class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Enter the desired password length:")
        self.layout.addWidget(self.label)

        self.length_input = QLineEdit(self)
        self.layout.addWidget(self.length_input)

        self.generate_button = QPushButton("Generate Password", self)
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.result_label = QLabel("", self)
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def generate_password(self):
        try:
            length = int(self.length_input.text())
            if length <= 0:
                raise ValueError("Password length must be greater than 0")
        except ValueError as e:
            self.result_label.setText(str(e))
            return

        # Characters to choose from for password generation
        password_characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password
        password = ''.join(random.choice(password_characters) for _ in range(length))

        self.result_label.setText(f"Generated Password: {password}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())