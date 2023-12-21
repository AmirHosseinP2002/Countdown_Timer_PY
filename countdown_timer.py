import time

def countdown(time_second):
    while time_second:
        mins, secs = divmod(time_second, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        time_second -= 1

    print("stop")

countdown(80)
