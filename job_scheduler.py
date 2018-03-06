import schedule
import time
from datetime import datetime
from quickstart import main
from gmail_sender import send_mail

def job():
    title = "Data e Hora : " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = main()
    send_mail(title,message)


#schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)