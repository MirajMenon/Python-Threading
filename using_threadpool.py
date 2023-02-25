import time
import concurrent.futures


def run_sleep(seconds: int) -> None:
    print(f'Sleeping {seconds} second(s)..')
    time.sleep(seconds)
    return f'Done Sleeping {seconds}.'


start_time = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    results = [executor.submit(run_sleep, sec) for sec in secs]
    # prints the results in the order that they completed
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    results = executor.map(run_sleep, secs)
    # prints the results in the order that they started
    for r in results:
        print(r)

end_time = time.perf_counter()
print(f'Finished in {round(end_time - start_time, 2)} second(s)')
