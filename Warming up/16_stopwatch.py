import time

class Stopwatch():
    def __init__(self):
        self.start_time = None
        self.stop_time = None
    
    def start(self):
        self.start_time = time.time()
    def stop(self):
        self.stop_time = time.time()
    
    def total_run_time(self):
        if self.stop_time ==None:
            return 0
        
        return self.stop_time - self.start_time
    
    def time_elapsed(self):
        return time.time() - self.start_time
            
    def show_result(self):
        print('경과 시간 : %.4f초'%(self.total_run_time()))
        
sw = Stopwatch()

input("Press Enter to start")
sw.start()
input("Press Enter to stop")
sw.stop()

sw.show_result()
