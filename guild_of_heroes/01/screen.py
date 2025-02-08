import sys
import sqlite3
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from menu import MenuWindow
# from vstuplenie import Elder

# Создание базы данных
conn = sqlite3.connect('data/users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT)''')
conn.commit()

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Guild of Heroes")
        self.setGeometry(1200, 900, 500, 400)

        # Установка фона
        self.background_label = QLabel(self)
        self.background_pixmap = QPixmap("data/fon_1.jpg")
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 500, 400)

        # Надпись
        self.title_label = QLabel("Guild of Heroes", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(0, 0, 500, 400)

        # Обработчик нажатия
        self.mousePressEvent = self.on_mouse_press

    def on_mouse_press(self, event):
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.setGeometry(1200, 900, 500, 400)

        self.layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Имя пользователя")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Войти", self)
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.register_button = QPushButton("Зарегистрироваться", self)
        self.register_button.clicked.connect(self.register)
        self.layout.addWidget(self.register_button)

        self.setLayout(self.layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        if user:
            self.open_menu()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль!")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            QMessageBox.information(self, "Успех", "Регистрация успешна!")
            from vstuplenie import Elder  # Импортируем, чтобы двойной импорт не мешал
            self.menu_window = Elder()
            self.menu_window.show()
            self.close()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Ошибка", "Имя пользователя уже существует!")

    def open_menu(self):
        threading.Thread(target=self.run_menu).start()
        self.close()
    #
    # def open_vstuplenie(self):
    #     threading.Thread(target=self.run_vstuplenie).start()
    #     self.close()
    #
    # def run_vstuplenie(self):
    #     vst_window = Elder()
    #     vst_window.run()

    def run_menu(self):
        menu_window = MenuWindow()
        menu_window.run()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Screen()
    screen.show()
    sys.exit(app.exec_())


