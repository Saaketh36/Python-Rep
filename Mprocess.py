import multiprocessing
import time

def task(name):
    for i in range(5):
        print(f"{name} running")
        time.sleep(5)
if __name__ == "__main__": 
    proc1 = multiprocessing.Process(target = task, args= ("Process_1",))
    proc2 = multiprocessing.Process(target = task, args= ("Process_2",))

    proc1.start()
    proc2.start()

    proc1.join()    
    proc2.join()