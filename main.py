import sys
import json
import os
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QBrush, QColor, QStandardItemModel, QStandardItem  # Добавлены QStandardItemModel и QStandardItem
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QCheckBox, QRadioButton, QPushButton, QLineEdit, QVBoxLayout, QWidget, QTableView,
    QMessageBox
)
from PySide6.QtCore import QCoreApplication
from ui_main2 import Ui_MainWindow  # Импортируем UI-класс
from configparser import ConfigParser
class MainWindow(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            print("Создан экземпляр MainWindow")  # Отладочное сообщение
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            ...
        except Exception as e:
            print(f"Ошибка при инициализации MainWindow: {e}")
            sys.exit(1)
        # Чтение данных из INI-файла
        config = ConfigParser()
        config.read("user_data.ini", encoding="utf-8")
        self.selected_test_name = config.get("User", "test_name", fallback="test 0")
        self.selected_test_file = config.get("User", "test_file")

        # Загрузка вопросов из выбранного JSON-файла
        self.questions = self.load_questions(self.selected_test_file)
        self.answered_questions = set()  # Множество для хранения индексов пройденных вопросов
        self.correct_answers_count = 0  # Счетчик правильных ответов

        # Настройка таймера
        self.timer_duration = self.questions.get("timer", 10) * 60  # Время в секундах
        self.remaining_time = self.timer_duration
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Обновление каждую секунду

        # Настройка таблицы с вопросами
        self.setup_question_table()

        # Подключение обработчиков событий
        self.ui.tableView.clicked.connect(self.select_question)
        self.ui.EnterAnswer.clicked.connect(self.submit_answer)  # Общая кнопка для отправки ответа

        # Автоматический запуск первого вопроса
        self.current_question_index = 0
        self.display_question()

    def load_questions(self, filename):
        """Загрузка вопросов из JSON-файла."""
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def setup_question_table(self):
        """Настройка таблицы с вопросами."""
        model = QStandardItemModel(len(self.questions["questions"]), 1)  # Строки и столбцы
        model.setHorizontalHeaderLabels([QCoreApplication.translate("MainWindow", "Вопросы")])

        for idx, question in enumerate(self.questions["questions"]):
            item = QStandardItem(f"○ {question.get('question_name', '')}")
            item.setData(idx, Qt.UserRole)  # Сохраняем индекс вопроса
            item.setEditable(False)  # Запрещаем редактирование
            model.setItem(idx, 0, item)

        self.ui.tableView.setModel(model)
        self.ui.tableView.resizeColumnsToContents()

    def update_question_symbols(self):
        """Обновление символов вопросов в таблице."""
        model = self.ui.tableView.model()
        for row in range(model.rowCount()):
            index = model.index(row, 0)
            question_index = model.data(index, Qt.UserRole)
            if question_index in self.answered_questions:
                # Пройденные вопросы помечаем галочкой
                model.setData(index, f"✔ {self.questions['questions'][question_index].get('question_name', '')}", Qt.DisplayRole)
            else:
                # Неотвеченные вопросы оставляем кружком
                model.setData(index, f"○ {self.questions['questions'][question_index].get('question_name', '')}", Qt.DisplayRole)

    def select_question(self, index):
        """Обработка выбора вопроса из таблицы."""
        row = index.row()
        question_index = self.ui.tableView.model().item(row, 0).data(Qt.UserRole)

        if question_index in self.answered_questions:
            # Показываем диалоговое окно
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("Информация")
            msg_box.setText("Этот вопрос уже пройден.")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
        else:
            self.current_question_index = question_index
            self.display_question()

    def display_question(self):
        """Отображение текущего вопроса."""
        if self.current_question_index >= len(self.questions["questions"]):
            self.show_results()
            return

        question = self.questions["questions"][self.current_question_index]

        # Обновление названия вопроса
        self.ui.QuestionName_label.setText(question.get("question_name", ""))

        # Обновление текста вопроса
        self.ui.QuestionText_Label.setText(question.get("question_text", ""))

        # Очистка предыдущих вариантов ответов
        self.clear_options()

        # Настройка типа вопроса
        if question["type"] == "radio":
            self.setup_radio_buttons(question.get("options", []))
            self.ui.RadioBox_Frame.setVisible(True)
            self.ui.CheckBox_Frame.setVisible(False)
            self.ui.TextInput_Frame.setVisible(False)

        elif question["type"] == "checkbox":
            self.setup_checkboxes(question.get("options", []))
            self.ui.CheckBox_Frame.setVisible(True)
            self.ui.RadioBox_Frame.setVisible(False)
            self.ui.TextInput_Frame.setVisible(False)

        elif question["type"] == "text":
            self.ui.TIF_Edit.setEnabled(True)  # Разблокировка текстового поля
            self.ui.TextInput_Frame.setVisible(True)
            self.ui.RadioBox_Frame.setVisible(False)
            self.ui.CheckBox_Frame.setVisible(False)

        # Кнопка отправки ответа всегда доступна
        self.ui.EnterAnswer.setEnabled(True)

    def clear_options(self):
        """Очистка всех вариантов ответов."""
        for i in reversed(range(self.ui.verticalLayout_2.count())):
            widget = self.ui.verticalLayout_2.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        for i in reversed(range(self.ui.verticalLayout_3.count())):
            widget = self.ui.verticalLayout_3.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Очистка текстового поля
        self.ui.TIF_Edit.clear()

    def setup_radio_buttons(self, options):
        """Настройка радио-кнопок."""
        for option in options:
            radio_button = QRadioButton(option)
            self.ui.verticalLayout_3.addWidget(radio_button)

    def setup_checkboxes(self, options):
        """Настройка чекбоксов."""
        for option in options:
            checkbox = QCheckBox(option)
            self.ui.verticalLayout_2.addWidget(checkbox)

    def submit_answer(self):
        """Обработка отправки ответа."""
        if self.current_question_index >= len(self.questions["questions"]):
            return

        question = self.questions["questions"][self.current_question_index]

        if question["type"] == "radio":
            self.submit_radio_answer()
        elif question["type"] == "checkbox":
            self.submit_checkbox_answer()
        elif question["type"] == "text":
            self.submit_text_answer()

    def submit_text_answer(self):
        """Обработка текстового ответа."""
        answer = self.ui.TIF_Edit.text().strip()
        correct_answer = self.questions["questions"][self.current_question_index].get("correct_answer", "")
        if answer.lower() == correct_answer.lower():
            self.correct_answers_count += 1
        print(f"Ответ на текстовый вопрос: {answer}")
        self.mark_question_as_answered()

    def submit_checkbox_answer(self):
        """Обработка ответов чекбоксов."""
        answers = []
        for i in range(self.ui.verticalLayout_2.count()):
            checkbox = self.ui.verticalLayout_2.itemAt(i).widget()
            if isinstance(checkbox, QCheckBox) and checkbox.isChecked():
                answers.append(checkbox.text())
        correct_answers = self.questions["questions"][self.current_question_index].get("correct_answers", [])
        if set(answers) == set(correct_answers):
            self.correct_answers_count += 1
        print(f"Ответы на вопрос с чекбоксами: {answers}")
        self.mark_question_as_answered()

    def submit_radio_answer(self):
        """Обработка ответов радио-кнопок."""
        for i in range(self.ui.verticalLayout_3.count()):
            radio_button = self.ui.verticalLayout_3.itemAt(i).widget()
            if isinstance(radio_button, QRadioButton) and radio_button.isChecked():
                answer = radio_button.text()
                correct_answer = self.questions["questions"][self.current_question_index].get("correct_answer", "")
                if answer == correct_answer:
                    self.correct_answers_count += 1
                print(f"Ответ на вопрос с радио-кнопками: {answer}")
                self.mark_question_as_answered()
                break

    def mark_question_as_answered(self):
        """Метка вопроса как пройденного."""
        self.answered_questions.add(self.current_question_index)
        self.update_question_symbols()  # Обновляем символы вопросов
        self.next_question()

    def next_question(self):
        """Переход к следующему вопросу."""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions["questions"]):
            self.display_question()
        else:
            self.show_results()

    def update_timer(self):
        """Обновление таймера."""
        if self.remaining_time > 0:
            self.remaining_time -= 1
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.ui.Timer_Label.setText(f"{minutes:02}:{seconds:02}")
        else:
            self.timer.stop()
            self.show_results()

    def show_results(self):
        """Показ результатов после завершения теста."""
        result_text = (
            f"Тест завершен!\nПравильных ответов: {self.correct_answers_count}/{len(self.questions['questions'])}"
        )
        self.ui.QuestionText_Label.setText(result_text)
        self.ui.EnterAnswer.setEnabled(False)

        # Сохранение результатов в INI-файл
        self.save_results_to_ini()

    def save_results_to_ini(self):
        """Сохранение результатов теста в INI-файл."""
        config = ConfigParser()

        # Чтение имени пользователя и названия теста из INI-файла
        config.read("user_data.ini", encoding="utf-8")
        user_name = config.get("User", "name", fallback="Неизвестный пользователь")
        test_name = config.get("User", "test_name", fallback="Неизвестный тест")

        # Создание секции Results
        config["Results"] = {
            "user_name": user_name,
            "test_name": test_name,
            "correct_answers": str(self.correct_answers_count),
            "total_questions": str(len(self.questions["questions"]))
        }

        # Сохранение данных в файл
        with open("user_data.ini", "w", encoding="utf-8") as configfile:
            config.write(configfile)

