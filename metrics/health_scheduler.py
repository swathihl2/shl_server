import threading

import requests

health_status = {"status": "unknown"}


def start_scheduler():
    check_health()


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

    # Schedule the next health check
    threading.Timer(30, check_health).start()
