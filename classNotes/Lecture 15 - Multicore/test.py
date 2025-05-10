# https://docs.python.org/3/library/multiprocessing.html - multiprocessing man page

import time
from multiprocessing import Process, Queue, current_process, freeze_support, Manager, Lock

# given function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def worker(highest_prime, lock, end_time):
  """Worker process to test numbers and update highest prime."""
  local_highest = highest_prime.value
  while time.time() < end_time:  # Time-based stop condition
    if is_prime(local_highest):
        local_highest = max(local_highest,highest_prime.value)
    with lock:
        highest_prime.value = max(highest_prime.value, local_highest)

def main(num_processes, run_time):
  """Main function to manage processes and calculate execution time."""
  manager = Manager()
  highest_prime = manager.Value('i', 0)
  lock = Lock()

  processes = []
  end_time = time.time() + run_time  # Calculate end time
  for _ in range(num_processes):
    p = Process(target=worker, args=( highest_prime, lock, end_time))
    processes.append(p)
    p.start()


  print(f"Highest prime found: {highest_prime.value}")

if __name__ == '__main__':
  freeze_support() # found in some multiprocessing examples 
  num_processes = 2  # Adjust the number of processes
  run_time = 3 * 60000   # Adjust the run time in seconds
  main(num_processes, run_time)