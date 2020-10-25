"""Pomodoro app main class"""

import sys
import os
import csv
import time
import record_keeper

class Pomodoro:
    def __init__(self):
        pass
        
    def exit_program(self):
        print("See you later!")    
        sys.exit()
        
    def run_timer(self):  #  Main loop for the program
        while True:
            #  Set how many minutes to count.
            self.set_minutes = input("Enter Minutes: ")
            if self.set_minutes.lower() == 'q':
                self.exit_program()    
            try:
                self.set_minutes = int(self.set_minutes)
            except:
                print("Must enter a number of minutes.\nEnter 'q' to quit.")
                continue

            self.begin_timer = input("Start(y/n): ")                        
            if self.begin_timer.lower() == 'n' or self.begin_timer.lower() == 'q':
                self.exit_program()
            
            self.timer(self.set_minutes, self.begin_timer)


    def timer(self, set_minutes, begin_timer):
        if begin_timer.lower() == 'y':
            time_set = set_minutes * 60
            start_time = time.time()
            local_start = time.localtime(start_time)
            end_time = start_time + time_set
            
            
            while time.time() < end_time:
                remaining_time = end_time - time.time()
                print(f"{remaining_time // 60:02.0f}:{round(remaining_time % 60):02}")
                time.sleep(0.99999)
                os.system("CLS")
                
                if remaining_time <= 1:
                    os.system("CLS")
                    date_stamp = time.strftime('%Y-%m-%d', local_start)
                    started_time = time.strftime('%I:%M %p', local_start)
                    record_keeper.saving_result(date_stamp, started_time, set_minutes)                
                    print(
                        f"Finished!\nCompleted {record_keeper.check_set_number(time.time())} pomodoro(s) today!"
                                                       )
                
        else:
            self.exit_program()
            
if __name__ == '__main__':
    pom = Pomodoro()
    pom.run_timer()
            