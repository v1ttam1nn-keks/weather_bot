import time
N = 5
DELAY = 0.5


def func1(n):
   for i in range(n):
       time.sleep(DELAY)
       print(f'--- line #{i} from {n} is completed')


def func2(n):
   for i in range(n):
       time.sleep(DELAY)
       print(f'=== line #{i} from {n} is completed')


def main():
   func1(N)
   func2(N)


if __name__ == '__main__':
   start = time.time()
   main()
   print(f'Total time: {time.time() - start}')