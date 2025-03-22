import time  
from apscheduler.schedulers.background import BackgroundScheduler
from motivator import send_message, client, quote

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

# 
job = scheduler.add_job(send_message, 'cron', hour=19, minute=42, args=[client, quote])

print(job)

while True:
    time.sleep(1)  # Keep the script running
