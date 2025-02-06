import sys
import os
import json
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import QCoreApplication
from configparser import ConfigParser
from PySide6.QtCore import Signal
from ui_signup import Ui_Examer  # Импортируем UI-класс окна регистрации
from main import MainWindow  # Импортируем класс основного окна



class RegistrationWindow(QWidget):
    registration_completed = Signal()


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: rgb(0, 29, 31); color: white;")
        self.init_ui()
        self.load_tests()

    def init_ui(self):
        layout = QVBoxLayout()
        self.name_label = QLabel("Введите ваше имя:")
        layout.addWidget(self.name_label)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя пользователя")
        layout.addWidget(self.name_input)
        self.test_label = QLabel("Выберите тест:")
        layout.addWidget(self.test_label)
        self.test_combobox = QComboBox()
        layout.addWidget(self.test_combobox)
        self.start_button = QPushButton("Перейти к тестированию")
        self.start_button.clicked.connect(self.start_test)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def load_tests(self):
        """Загрузка названий тестов из JSON-файлов."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_files = [f for f in os.listdir(current_dir) if f.endswith(".json")]

        self.tests = {}  # Словарь для хранения test_name и file_name
        for file in json_files:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    test_name = data.get("test_name", "Без названия")
                    file_name = data.get("file_name", file)  # Используем file_name для загрузки
                    self.tests[test_name] = file_name
                    self.test_combobox.addItem(test_name)
            except Exception as e:
                print(f"Ошибка при чтении файла {file}: {e}")

    def save_user_to_ini(self, user_name, test_name):
        """Сохранение данных пользователя в INI-файл."""
        config = ConfigParser()
        config.read("user_data.ini", encoding="utf-8")
        config["User"] = {"name": user_name, "test_name": test_name, "test_file": GLOBAL_FILE_NAME}
        with open("user_data.ini", "w", encoding="utf-8") as configfile:
            config.write(configfile)

    def start_test(self):
        """Обработка нажатия кнопки 'Перейти к тестированию'."""
        global GLOBAL_FILE_NAME  # Используем глобальную переменную
        user_name = self.name_input.text().strip()

        if not user_name:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Пожалуйста, введите ваше имя.")
            msg_box.exec()
            return

        selected_test_name = self.test_combobox.currentText()  # Получаем название выбранного теста
        selected_test_file = self.tests.get(selected_test_name)  # Получаем file_name из словаря tests

        if not selected_test_file or not os.path.exists(selected_test_file):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Выбранный тест не найден.")
            msg_box.exec()
            return

        # Устанавливаем глобальную переменную file_name
        GLOBAL_FILE_NAME = selected_test_file

        # Сохраняем данные пользователя в INI-файл
        self.save_user_to_ini(user_name, selected_test_name)
        print("Сигнал registration_completed испущен")  # Отладочное сообщение
        self.registration_completed.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создаем окно регистрации
    registration_window = RegistrationWindow()

    # Функция для открытия основного окна
    def open_main_window():
        """Открывает основное окно и закрывает окно регистрации."""
        print("Открываем основное окно...")  # Отладочное сообщение
        global main_window  # Делаем окно глобальным, чтобы оно не удалялось сборщиком мусора
        main_window = MainWindow()
        main_window.show()
        registration_window.close()
    # Подключаем сигнал завершения регистрации к функции open_main_window
    registration_window.registration_completed.connect(open_main_window)

    # Показываем окно регистрации
    registration_window.show()
    sys.exit(app.exec())