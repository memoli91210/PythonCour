

import time
import threading

my_lock=threading.RLock()

class MyProcess(threading.Thread):
    def __init__(self) :
        threading.Thread.__init__(self)
        
    def run(self):
        i=0
        while i<3:
            with my_lock:
                letters="abc"
                for lt in letters:
                    print(lt)
                    time.sleep(0.3)
            i += 1

# def process1():
#     i=0
#     while i<3:
#         print("coucou1")
#         time.sleep(0.3)
#         i += 1
        
# def process2():
#     i=0
#     while i<3:
#         print("coucou2")
#         time.sleep(0.3)
#         i += 1
        
# th1 = threading.Thread(target=process1)
# th2 = threading.Thread(target=process2)

th1=MyProcess()
th2=MyProcess()

th1.start()
th2.start()

th1.join()
th2.join()

print("fin du prog")