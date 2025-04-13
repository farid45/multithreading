import threading
import time

class Pharmacy:
    def __init__(self):
        self.semaphore = threading.Semaphore(value = 3)
        self.lock = threading.Lock()

    def customer(self, customer_id):
        self.semaphore.acquire()
        print(f"Клиент {customer_id} заходит в аптеку и берет талон.")
        print(f"Клиент {customer_id} ждет своей очереди.")

        with self.lock:
            print(f"Аптекарь начинает обслуживать клиента {customer_id}.")
            time.sleep(5)
            print(f"Аптекарь заканчивает обслуживание клиента {customer_id}.")

            self.semaphore.release()

    def start(self, num_customers):
        for customer_i in range(1, num_customers + 1):
            customer_thread = threading.Thread(target=self.customer, args=[customer_i])
            customer_thread.start()