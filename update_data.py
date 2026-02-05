import subprocess
import schedule
import time

def update_prices():
    subprocess.run(["python", "fetch_prices.py"], capture_output=True)

schedule.every().day.at("06:00").do(update_prices)
print("Auto-update programado. Ctrl+C para parar.")
while True:
    schedule.run_pending()
    time.sleep(60)
