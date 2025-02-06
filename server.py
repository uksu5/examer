import socket
import threading
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class TCPServer:
    def __init__(self, port=12345):
        self.port = port  # Порт для прослушивания
        self.server_socket = None  # Сокет сервера
        self.clients = []  # Список подключенных клиентов
        self.running = True  # Флаг работы сервера

    def get_local_ip(self):
        """Получает IP-адрес хоста в локальной сети."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  # Подключаемся к внешнему адресу для определения локального IP
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception as e:
            logging.error(f"Не удалось получить локальный IP: {e}")
            return "127.0.0.1"

    def start(self):
        """Запускает сервер."""
        host = self.get_local_ip()
        logging.info(f"Запуск сервера на {host}:{self.port}")

        try:
            # Создаем сокет
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Разрешаем повторное использование порта
            self.server_socket.bind((host, self.port))
            self.server_socket.listen(5)  # Максимальное количество ожидающих подключений

            logging.info("Сервер запущен. Ожидание подключений...")
            self.accept_clients()
        except OSError as e:
            logging.error(f"Ошибка при запуске сервера: {e}")
        finally:
            self.stop()

    def accept_clients(self):
        """Принимает подключения от клиентов."""
        while self.running:
            try:
                client_socket, client_address = self.server_socket.accept()
                logging.info(f"Подключение от {client_address}")
                self.clients.append(client_socket)
                # Запускаем поток для обработки клиента
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address), daemon=True)
                client_thread.start()
            except socket.error as e:
                if self.running:
                    logging.error(f"Ошибка при принятии подключения: {e}")
                else:
                    logging.info("Сервер остановлен.")
                    break

    def handle_client(self, client_socket, client_address):
        """Обрабатывает клиента."""
        try:
            while self.running:
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break  # Клиент отключился
                logging.info(f"Получено от {client_address}: {data}")
                response = f"Сервер получил: {data}"
                client_socket.sendall(response.encode('utf-8'))
        except Exception as e:
            logging.error(f"Ошибка при обработке клиента {client_address}: {e}")
        finally:
            logging.info(f"Клиент {client_address} отключен.")
            client_socket.close()
            if client_socket in self.clients:
                self.clients.remove(client_socket)

    def stop(self):
        """Останавливает сервер."""
        self.running = False
        if self.server_socket:
            logging.info("Остановка сервера...")
            try:
                self.server_socket.shutdown(socket.SHUT_RDWR)
                self.server_socket.close()
            except Exception as e:
                logging.warning(f"Ошибка при закрытии сокета: {e}")
            finally:
                self.server_socket = None

if __name__ == "__main__":
    server = TCPServer(port=12345)
    try:
        server.start()
    except KeyboardInterrupt:
        logging.info("Прерывание работы сервера пользователем.")
    finally:
        server.stop()