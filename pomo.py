"""Pomodoro app main class"""
import sys
import os
import json
from datetime import datetime
import time

class Pomodoro:
    def __init__(self):
        pass
        
    def run_timer(self):  #  Main loop for the program
        while True:
            #  Set how many minutes to count.
            self.set_minutes = int(input("Enter Minutes: "))
            self.begin_timer = input("Start(y/n): ")
            
            if self.begin_timer == 'n':
                print('See you later!')
                sys.exit()
            
            self.timer(self.set_minutes, self.begin_timer)

    def saving_result(self, result):
        filename = 'records.json'
        with open(filename, mode='a') as f:
            
            f.write(result)
        

    def timer(self, set_minutes, begin_timer):
        if begin_timer.lower() == 'y':
            time_set = set_minutes * 60
            start_time = time.time()
            end_time = start_time + time_set
            
            while time.time() < end_time:
                remaining_time = end_time - time.time()
                print(f"{remaining_time // 60:.0f}:{round(remaining_time % 60):02}")
                time.sleep(0.99999)
                os.system("CLS")
                
                if remaining_time <= 1:
                    os.system("CLS")
                    print("Complete!")
                    date_stamp = time.strftime('%Y-%m-%d', time.localtime(start_time))
                    start_time_literal = time.strftime('%I:%M %p')
                    result = {date_stamp: (start_time_literal, set_minutes)}
                    self.saving_result(str(result))
                
        else:
            print('See you later!')
            sys.exit()

            
if __name__ == '__main__':
    pom = Pomodoro()
    pom.run_timer()
            