from datetime import datetime, timedelta
from typing import List, Dict, Tuple

busy: List[Dict[str, str]] = [
    {'start': '10:30',
     'stop': '10:50'},
    {'start': '18:40',
     'stop': '18:50'},
    {'start': '14:40',
     'stop': '15:50'},
    {'start': '16:40',
     'stop': '17:20'},
    {'start': '20:05',
     'stop': '20:20'}
]

work_begins: str = '09:00'
work_ends: str = '21:00'


def working_time(
    work_start: datetime,
    work_end: datetime,
    breaks: List[Dict[str, str]]
) -> List[Tuple[datetime, datetime]]:
    """
    Creates a list of working time periods. Excluding the breaks.
    1. Converts breaks into datetime format
    2. Sorts the breaks ascending
    3. Creates a list of working time periods
    """
    working_periods: List = []
    breaks_datetime: List = []
    previous_stop: datetime = work_start

    for break_period in breaks:
        break_start = datetime.strptime(break_period['start'], '%H:%M')
        break_stop = datetime.strptime(break_period['stop'], '%H:%M')
        breaks_datetime.append((break_start, break_stop))

    breaks_datetime.sort()

    for period in breaks_datetime:
        break_start = period[0]
        break_stop = period[1]
        if break_start > previous_stop:
            working_periods.append((previous_stop, break_start))
        previous_stop = break_stop

    if previous_stop < work_end:
        working_periods.append((previous_stop, work_end))

    return working_periods


def break_into_intervals(
    working_periods: List[Tuple[datetime, datetime]],
    minutes: int = 30
) -> List[Tuple[datetime, datetime]]:
    """
    Divides the provided working time into periods according to the interval.
    Default interval is minutes 30.
    """
    time_interval: timedelta = timedelta(minutes=minutes)
    working_periods_divided: List = []

    for period in working_periods:
        start_time = period[0]
        stop_time = period[1]

        current_time = start_time
        while current_time + time_interval <= stop_time:
            working_periods_divided.append(
                (current_time, current_time + time_interval)
            )
            current_time += time_interval

    return working_periods_divided


def print_results(working_periods_divided) -> None:
    for period in working_periods_divided:
        start_time = period[0].strftime("%H:%M")
        stop_time = period[1].strftime("%H:%M")
        print(f'Working period: {start_time} - {stop_time}')


if __name__ == '__main__':
    start: datetime = datetime.strptime(work_begins, '%H:%M')
    stop: datetime = datetime.strptime(work_ends, '%H:%M')
    undivided_worktime = working_time(start, stop, busy)
    divided_worktime = break_into_intervals(undivided_worktime)
    print_results(divided_worktime)
