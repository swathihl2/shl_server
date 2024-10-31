import threading
import time

import requests
import schedule
health_status = {"status": "unknown"}


def check_health():
    global health_status
    try:
        response = requests.get('https://shl-server.onrender.com/health')
        if response.status_code == 200:
            health_status = {"status": "healthy", "data": response.json()}
        else:
            health_status = {"status": "unhealthy", "code": response.status_code}
    except Exception as e:
        health_status = {"status": "error", "message": str(e)}


def run_scheduler():
    schedule.every(30).seconds.do(check_health)
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_scheduler():
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
