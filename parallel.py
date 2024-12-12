import threading
import time

def tulosta_viesti(viesti, kesto):
    for i in range(5):
        time.sleep(kesto)
        print(viesti)

thread1 = threading.Thread(target=tulosta_viesti, args=("Säie 1: Hei!", 1))
thread2 = threading.Thread(target=tulosta_viesti, args=("Säie 2: Moi!", 5))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Kaikki säikeet ovat valmiita.")

