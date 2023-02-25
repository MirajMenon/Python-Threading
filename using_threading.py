import time
import threading


def run_sleep(seconds: int) -> None:
    print(f'Sleeping {seconds} second(s)..')
    time.sleep(seconds)
    print(f'Done Sleeping {seconds}.')


start_time = time.perf_counter()
threads = []
for _ in range(10):
    t = threading.Thread(target=run_sleep, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end_time = time.perf_counter()
print(f'Finished in {round(end_time - start_time, 2)} second(s)')
