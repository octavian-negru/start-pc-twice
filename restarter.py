import os
from datetime import datetime

LAST_RESTART_TIME = "last_restart_time.txt"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


def restart():
    print("Restarting...")
    os.system("shutdown /r /t 1")


def was_restarted_in_last(minutes: int) -> bool:
    if os.path.exists(LAST_RESTART_TIME):
        with open(LAST_RESTART_TIME, "r") as last_restart_file:
            last_restart_time = last_restart_file.readlines()[0]
            difference = datetime.now() - datetime.strptime(last_restart_time, TIME_FORMAT)
            return difference.total_seconds() < 60 * minutes
    else:
        raise FileNotFoundError(f"[ERROR]: {LAST_RESTART_TIME} does not exist! Exiting...")


def save_restart_time():
    with open(LAST_RESTART_TIME, "w") as last_restart_file:
        last_restart_file.write(datetime.now().strftime(TIME_FORMAT))


if __name__ == "__main__":
    minutes = 5
    if not was_restarted_in_last(minutes):
        save_restart_time()
        restart()
    else:
        print(f"Not restarting, was restarted in last {minutes} minute/s")
