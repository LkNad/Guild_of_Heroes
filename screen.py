import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Создание базы данных
conn = sqlite3.connect('users.db')
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
        self.background_pixmap = QPixmap("фон для проекта.jpg")
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
        self.setWindowTitle("Заметки")
        self.setGeometry(1200, 900, 500, 400)



        self.layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Никнейм")
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
            QMessageBox.warning(self, "Ошибка", "Неверный никнейм или пароль!")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            QMessageBox.information(self, "Успех", "Регистрация успешна!")
            self.open_menu()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Ошибка", "Никнейм уже существует!")

    def open_menu(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()  # Закрыть главное окно


class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Меню")
        self.setGeometry(1200, 900, 400, 300)

        self.layout = QVBoxLayout()

        # Кнопки
        self.button1 = QPushButton("правила игры", self)
        self.button1.clicked.connect(self.button1_run)
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("выбор персонажа", self)
        self.button2.clicked.connect(self.button2_run)
        self.layout.addWidget(self.button2)

        self.button3 = QPushButton("мои результаты", self)
        self.button3.clicked.connect(self.button3_run)
        self.layout.addWidget(self.button3)

        self.setLayout(self.layout)

    def button1_run(self):
        QMessageBox.information(self, "правила игры", "Здесь будут правила игры!")

    def button2_run(self):
        QMessageBox.information(self, "выбор персонажа", "Здесь вы сможете выбрать персонажа!")

    def button3_run(self):
        QMessageBox.information(self, "мои результаты", "Здесь вы сможете посмотреть свои результаты!!!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = Screen()
    screen.show()
    sys.exit(app.exec_())
conn.close()

