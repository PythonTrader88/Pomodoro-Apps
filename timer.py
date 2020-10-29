"""Module to set timer running."""

import time
import record_keeper
import os


class TimeVariables:
    def __init__(self, minutes):
        self.seconds = minutes * 60  #  Convert to seconds
        self.start_time = time.time()  #  Capture starting point.
        self.local_start = time.localtime(self.start_time)  #  Capture local time.
        self.end_time = self.start_time + self.seconds  #  Capture end point.

def timer(minutes, begin_timer):
    if begin_timer.lower() == 'y':  #  Check to begin.
        attributes = TimeVariables(minutes)
        
        while time.time() < attributes.end_time:
            remaining_time = attributes.end_time - time.time()
            print(f"Remaining time to completion:\n{remaining_time // 60:02.0f}:{round(remaining_time % 60):02}")
            time.sleep(0.99999)
            os.system("CLS")
            
            if remaining_time <= 1:
                os.system("CLS")
                date_stamp = time.strftime('%Y-%m-%d', attributes.local_start)
                started_time = time.strftime('%I:%M %p', attributes.local_start)
                record_keeper.saving_result(date_stamp, started_time, minutes)

def short_rest(minutes=5):
    attribute = TimeVariables(minutes)
    
    while time.time() < attribute.end_time:
        remaining_time = attribute.end_time - time.time()
        print(f"Taking a short break - {remaining_time // 60:02.0f}:{round(remaining_time % 60):02}")
        time.sleep(0.99999)
        os.system("CLS")

def long_rest(minutes=30):
    attribute = TimeVariables(minutes)

    while time.time() < attribute.end_time:
        remaining_time = attribute.end_time - time.time()
        print(f"Taking a long break - {remaining_time // 60:02.0f}:{round(remaining_time % 60):02}")
        time.sleep(0.99999)
        os.system("CLS")