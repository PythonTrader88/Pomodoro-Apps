"""Pomodoro app main class"""
import sys
import os
import csv
from datetime import datetime
import time
import pytz

class Pomodoro:
    def __init__(self):
        pass
        
    def run_timer(self):  #  Main loop for the program
        while True:
            #  Set how many minutes to count.
            self.set_minutes = int(input("Enter Minutes: "))
            self.begin_timer = input("Start(y/n): ")
            
            if self.begin_timer == 'n':
                sys.exit()
            
            self.timer(self.set_minutes, self.begin_timer)

    # def saving_open(self, start_time):
    #     filename = 'records.csv'
    #     with open(filename, mode='a') as f:
    #         f.write(time.strftime('%Y-%m-%d %H:%M', time.localtime(start_time)))
        

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
                
            if time_set == 0:
                os.system("CLS")
                print("Complete!")
        else:
            print('See you later!')
            sys.exit()

            
if __name__ == '__main__':
    pom = Pomodoro()
    pom.run_timer()
            

def time_zone():
    
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    current_time = datetime_NY.strftime("%I:%M %p")

    tz_Seoul = pytz.timezone('Asia/Seoul')
    datetime_Seoul = datetime.now(tz_Seoul)
    seoul_time = datetime_Seoul.strftime("%I:%M %p")

    pass