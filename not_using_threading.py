import time


def run_sleep(seconds: int) -> None:
    print(f'Sleeping {seconds} second(s)..')
    time.sleep(seconds)
    print(f'Done Sleeping {seconds}.')


start_time = time.perf_counter()

for _ in range(10):
    run_sleep(1)

end_time = time.perf_counter()

print(f'Finished in {round(end_time - start_time, 2)} second(s)')
