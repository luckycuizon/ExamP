import time
from datetime import datetime, timedelta
import subprocess

def my_app():
    # Call and run the app.py script
    print("Running app.py at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    subprocess.run(["python", "app.py"])

def main():
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=1)
    
    while datetime.now() < end_time:
        my_app()
        time.sleep(5) #run every 5 seconds

if __name__ == "__main__":
    main()