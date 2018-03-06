import schedule
import time
from datetime import datetime
from quickstart import main

def job():
    print("Data e Hora : " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    main()
    print("                     --------------                     ")

schedule.every(30).minutes.do(job)
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)