import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from examer_code import Ui_MainWindow  # Главный интерфейс
from settings_code import Ui_Dialog        # Интерфейс настроек
import socket
import psutil
class SettingsDialog(QDialog):
    """Класс для диалогового окна настроек"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Создаем экземпляр UI для диалога
        self.ui.setupUi(self)  # Настройка интерфейса

        # Получаем IP-адрес в локальной сети
        ip_address = self.get_local_ip()
        if ip_address:
            self.ui.label.setText(f"IP: {ip_address}")
        else:
            self.ui.label.setText("IP: Локальная сеть не обнаружена")

    def get_local_ip(self):
        """Получает IP-адрес в локальной сети"""
        try:
            # Получаем список всех сетевых интерфейсов
            addrs = psutil.net_if_addrs()
            for interface, addresses in addrs.items():
                for addr in addresses:
                    # Ищем IPv4 адрес, который не является localhost (127.0.0.1)
                    if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                        return addr.address
            return None  # Если не найден подходящий IP
        except Exception as e:
            print(f"Ошибка при получении IP-адреса: {e}")
            return None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем экземпляр UI и настраиваем интерфейс
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clients = []  # Список подключенных клиентов
        self.server_thread = None  # Поток сервера
        self.start_server()  # Запускаем сервер при инициализации
        self.load_ip_config()  # Загружаем IP-адрес из конфига
        self.update_clients_timer = QTimer(self)  # Таймер для обновления списка клиентов
        self.update_clients_timer.timeout.connect(self.update_clients_table)
        self.update_clients_timer.start(1000)  # Обновляем каждую секунду
        # Подключение сигналов к слотам (логика кнопок)
        self.ui.load_test.clicked.connect(self.on_load_test_clicked)
        self.ui.settings_button.clicked.connect(self.on_settings_button_clicked)
        self.ui.save_table.clicked.connect(self.on_save_table_clicked)

    def on_load_test_clicked(self):
        """Логика для кнопки 'Запустить тест'"""
        print("Кнопка 'Запустить тест' нажата")

    def on_settings_button_clicked(self):
        """Логика для кнопки 'Настройки'"""
        print("Кнопка 'Настройки' нажата")
        # Создаем и показываем диалоговое окно настроек
        settings_dialog = SettingsDialog()
        settings_dialog.exec()  # Открываем диалог в модальном режиме

    def on_save_table_clicked(self):
        """Логика для кнопки 'Сохранить в *.XLS'"""
        print("Кнопка 'Сохранить в *.XLS' нажата")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())