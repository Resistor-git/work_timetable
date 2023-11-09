from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional

busy = [
    {'start' : '10:30',
    'stop' : '10:50'
    },
    {'start' : '18:40',
    'stop' : '18:50'
    },
    {'start' : '14:40',
    'stop' : '15:50'
    },
    {'start' : '16:40',
    'stop' : '17:20'
    },
    {'start' : '20:05',
    'stop' : '20:20'
    }
]

work_begins: str = '09:00'
work_ends: str = '21:00'
default_interval: int = 30


# tdelta = timedelta(minutes=30)
start: datetime = datetime.strptime(work_begins, '%H:%M')
stop: datetime = datetime.strptime(work_ends, '%H:%M')


def working_time(work_start: datetime, work_end: datetime, breaks: List[Dict[str, str]]) -> List[Tuple[datetime, datetime]]:
    working_periods: List[Optional[Tuple[datetime, datetime]]] = []  # pretty sure the type hint is wrong...
    break_periods: List = []
    previous_stop: datetime = start

    for break_period in breaks:
        break_start = datetime.strptime(break_period['start'], '%H:%M')
        break_stop = datetime.strptime(break_period['stop'], '%H:%M')
        break_periods.append((break_start, break_stop))

    for period in break_periods:
        start_time = period[0]
        stop_time = period[1]
        if start_time > previous_stop:
            working_periods.append((previous_stop, start_time))
        previous_stop = stop_time
    
    if previous_stop < work_end:
        working_periods.append((previous_stop, work_end))

    # for period in working_periods:
    #     start_time = period[0].strftime("%H:%M")
    #     stop_time = period[1].strftime("%H:%M")
    #     print(f'Working period: {start_time} - {stop_time}')
    return working_periods


def break_into_intervals(periods: List[Tuple[datetime, datetime]], interval) -> List[Tuple[datetime, datetime]]:
    interval = timedelta(minutes=interval)
    ...


working_time(start, stop, busy)
