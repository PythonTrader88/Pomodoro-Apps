"""Pomodoro app main class"""

import sys
import os
import csv
import time
import record_keeper
import timer

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
            
            timer.timer(self.set_minutes, self.begin_timer)
            print(
                f"Finished!\nCompleted {record_keeper.check_set_number(time.time())} pomodoro(s) today!"
                )

            if record_keeper.check_set_number(time.time()) % 4 != 0:
                timer.short_rest()
            else:
                timer.long_rest()

        else:
            self.exit_program()
            
if __name__ == '__main__':
    pom = Pomodoro()
    pom.run_timer()
            