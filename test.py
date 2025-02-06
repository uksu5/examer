import subprocess


def shutdown_remote_computer(ip_address, username, password):
    try:
        command = [
            "shutdown",
            "/m", f"\\\\{ip_address}",  # Указываем целевой компьютер
            "/u", username,  # Имя пользователя
            "/p", password,  # Пароль
            "/s",  # Флаг для выключения
            "/f",  # Принудительное закрытие приложений
            "/t", "0",  # Время задержки перед выключением (в секундах)
            "/d", "p:2:4"  # Причина завершения работы
        ]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print(f"Компьютер {ip_address} успешно выключен.")
        else:
            print(f"Ошибка при выключении компьютера {ip_address}: {result.stderr}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    target_ip = "192.168.50.189"  # IP-адрес целевого компьютера
    admin_username = "Admin"  # Имя пользователя с правами администратора
    admin_password = "1"  # Пароль

    shutdown_remote_computer(target_ip, admin_username, admin_password)