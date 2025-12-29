import threading
import time


def send_notification(user: str, delay: int):
    print(f"Начинаю отправку уведомления для {user}...")
    time.sleep(delay)
    print(f"Уведомление для {user} отправлено!")


def main():
    users = [("Alice", 2), ("Bob", 3), ("Charlie", 1), ("Diana", 4)]

    threads = []

    for user, delay in users:
        thread = threading.Thread(target=send_notification, args=(user, delay))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nВсе уведомления отправлены!")


if __name__ == "__main__":
    main()
