"""Module for reading and writing records."""

import csv
import time
import os

def check_set_number(date):
    filename = 'records.csv'
    with open(filename, mode='r') as f:
        count_today = 0
        current_date = time.strftime('%Y-%m-%d', time.localtime(date))
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            if row['Date'] == current_date:
                count_today += 1
        
        return count_today

def saving_result(date, began_time, minutes):
    filename = 'records.csv'
    if not os.path.exists(filename):
        with open(filename, mode='w') as f:
            csv_writer = csv.DictWriter(f, fieldnames=['Date', 'Time_Finished', 'Minutes'], lineterminator='\n')
            csv_writer.writeheader()
            
    with open(filename, mode='a') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['Date', 'Time_Finished', 'Minutes'], lineterminator = '\n')
        csv_writer.writerow({
            'Date': date,
            'Time_Finished': began_time,
            'Minutes': minutes})


# def check_set_number():
#     filename = 'records.csv'
#     with open(filename, mode='r') as f:
#         values = defaultdict(int)
#         current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#         reader = csv.DictReader(f, delimiter=',')
#         for row in reader:
#             date = datetime.strptime(row['Date'], '%Y-%m-%d')
#             values[date.strftime('%Y-%m-%d')] += 1
#             if row['Date'] == current_date:
#                 count_today += 1
        
#         print(count_today)