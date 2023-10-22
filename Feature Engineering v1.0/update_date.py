import sys
import logging
import argparse
from datetime import datetime, timedelta
import yaml
import os
import time

def update_date(table_name):
    table_name = table_name
    date_file = table_name + ".yaml"
    with open(date_file, 'r') as f:
        params = yaml.load(f, Loader=yaml.FullLoader)

    date = params['Date']
    freq = params['Freq']
    print(type(date))
    print(date)

    #datetime_object = datetime.strptime(date, '%d-%m-%Y')
    #print(datetime_object.date())
    startdate = date + timedelta(days=freq)
    #startdate = datetime.now()
    #startdate = startdate.date()
    print('startdate:', startdate)
    
    currentdate = datetime.now().date()
    print('currentdate', currentdate)
    if currentdate ==  startdate:
        print("Job started")
        time.sleep(30)

        print("Job completed, updating date in yaml file")
    params['Date'] = datetime.now().date()

    with open(date_file, 'w') as f:
        yaml.dump(params, f)


if __name__ == "__main__":
    table_name = sys.argv[1]
    update_date(table_name)