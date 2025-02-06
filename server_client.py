import socket
import configparser
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class TCPClient:
    def __init__(self):
        self.server_ip = None  # IP-адрес сервера
        self.server_port = 12345  # Порт сервера
        self.client_socket = None  # Сокет клиента

    def load_server_ip(self):
        """Загружает IP-адрес сервера из ip_config.ini."""
        config = configparser.ConfigParser()
        try:
            if not config.read("ip_config.ini"):
                raise FileNotFoundError("Файл ip_config.ini не найден.")
            self.server_ip = config.get("Server", "ip")
            logging.info(f"Загружен IP-адрес сервера: {self.server_ip}")
        except Exception as e:
            logging.error(f"Ошибка при загрузке IP-адреса сервера: {e}")
            self.server_ip = None

    def connect_to_server(self):
        """Подключается к серверу."""
        if not self.server_ip:
            logging.error("IP-адрес сервера не задан. Подключение невозможно.")
            return

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logging.info(f"Попытка подключения к {self.server_ip}:{self.server_port}...")
            self.client_socket.connect((self.server_ip, self.server_port))
            logging.info("Подключение успешно установлено.")
            return True
        except socket.error as e:
            logging.error(f"Ошибка при подключении к серверу: {e}")
            return False

    def send_data(self, data):
        """Отправляет данные на сервер и получает ответ."""
        if not self.client_socket:
            logging.error("Сокет не инициализирован. Отправка данных невозможна.")
            return

        try:
            logging.info(f"Отправка данных на сервер: {data}")
            self.client_socket.sendall(data.encode('utf-8'))

            # Получаем ответ от сервера
            response = self.client_socket.recv(1024).decode('utf-8')
            logging.info(f"Получен ответ от сервера: {response}")
            return response
        except socket.error as e:
            logging.error(f"Ошибка при отправке данных: {e}")

    def close_connection(self):
        """Закрывает соединение с сервером."""
        if self.client_socket:
            logging.info("Закрытие соединения с сервером...")
            try:
                self.client_socket.close()
            except Exception as e:
                logging.warning(f"Ошибка при закрытии соединения: {e}")
            finally:
                self.client_socket = None

if __name__ == "__main__":
    client = TCPClient()

    # Загружаем IP-адрес сервера
    client.load_server_ip()

    # Проверяем, удалось ли загрузить IP
    if not client.server_ip:
        logging.error("Работа клиента завершена из-за ошибки загрузки IP-адреса сервера.")
        exit(1)

    # Подключаемся к серверу
    if not client.connect_to_server():
        logging.error("Не удалось подключиться к серверу. Работа клиента завершена.")
        exit(1)

    try:
        while True:
            # Ввод данных для отправки
            message = input("Введите сообщение для сервера (или 'exit' для выхода): ").strip()
            if message.lower() == "exit":
                break

            # Отправляем данные на сервер
            response = client.send_data(message)
            if response:
                print(f"Ответ сервера: {response}")
    except KeyboardInterrupt:
        logging.info("Прерывание работы клиента пользователем.")
    finally:
        # Закрываем соединение
        client.close_connection()