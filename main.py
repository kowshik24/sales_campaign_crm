import schedule
import time
from supervisor_agent import assign_tasks

schedule.every(10).minutes.do(assign_tasks)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(600)