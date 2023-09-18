from datetime import datetime

"""
Decorator used to determine calculation time for a function
"""
def runtime_calc(func):
    def wrapper():
        step_time_start = datetime.now()
        func()
        step_time_end = datetime.now()
        step_time_interval = step_time_end - step_time_start
        s = step_time_interval.seconds
        ms = f'{int(step_time_interval.microseconds) / 1000000}'
        step_time_string = f'{s % 60}.{ms}'
        print(f"Total runtime for {func}: {ms} seconds\n")
    return wrapper
