from dateutil.rrule import rrulestr
from dateutil import relativedelta, rrule
from datetime import datetime, timedelta, timezone


rule_string = "RRULE:FREQ=WEEKLY;BYDAY=TH"
# Use rrulestr to parse a RFC-formatted string
# Without a start time, it assumes the rule starts from now.
rule = rrulestr(rule_string)
# Get the next occurrence
rule.after(datetime.now())
# Get all the occurrences in December
dates = rule.between(after=datetime(2019, 12, 1),
                     before=datetime(2020, 5, 31))

# for date in dates:
#     print(date.isoformat())


def allmondays(year, yearsahead=1):
    '''Helper function to find all the mondays of a given year'''
    start_date = datetime(year, 1, 1)
    end_date = datetime(year+yearsahead, 12, 31)
    rr = rrule.rrule(rrule.WEEKLY, byweekday=relativedelta.MO,
                     dtstart=start_date)
    return rr.between(start_date, end_date, inc=True)


days = allmondays(2020)
for day in days:
    pass


def get_closest_dates(dates, basedate=None):
    '''Find the closest next and previous date from a basedate'''
    if not basedate:
        basedate = datetime.now()
    else:
        basedate = datetime.strptime(basedate, '%Y-%m-%d')
    closest_next = min(days, key=lambda x: (x < basedate, abs(x - basedate)))
    closest_prev = min(days, key=lambda x: (x > basedate, abs(x - basedate)))

    return (closest_next.date(), closest_prev.date(), "are closest to:", basedate.date())


get_closest_dates(days, '2020-01-09')


basedate = datetime.strptime('2020-05-09', '%Y-%m-%d')


# Set the two timeslots in UTC
timeslot1 = 'T120000Z'
timeslot2 = 'T200000Z'


today = datetime.now().date() + timedelta(days=2)
enddate = today + timedelta(days=7)

today = today.strftime('%Y-%m-%d')
enddate = enddate.strftime('%Y-%m-%d')

# print(today + timeslot1, today + timeslot2)
# print(enddate + timeslot1, enddate + timeslot2)


# Logic
# 1) Pick a start date - and use as 'Freeze_until'
# 1a) Odd weeks are early, even weeks are late
# -- if basedate % 2 > 0: # odd
# ---- start_time = 12
# -- else: # even
# ---- start_time = 20
# 2) Get the week boundaries
# 2a) DTSTART is max(Freeze_until, week_start)
# 2b) UNTIL is week_end at 00 + timedelta(days=1)
# 2c) Freeze_until is last_run + timedelta(days=2)
# 3) next week DTSTART is max(week_start, Freeze_until) at time early/late


def find_week_boundaries(basedate=None):
    '''Find the weekboundaries of a given date, defaults to today'''
    if not basedate:
        basedate = datetime.now().date()
    start = basedate - timedelta(days=basedate.weekday())
    end = start + timedelta(days=6)
    return(start, end)


def _get_start_time(weeknumber):
    '''Helper method to get the start time from the weeknumber'''
    if weeknumber % 2 > 0:
        # odd weeks
        return 12
    else:
        # even weeks
        return 20


def _generate_week(basedate, freeze=None):
    '''Helper method to generate a week's time slots'''
    week_num = basedate.isocalendar()[1]
    start_time = str(_get_start_time(week_num))

    week_start, week_end = find_week_boundaries(basedate)

    # convert basedate to be with timestamp and tzinfo like the freeze time is
    basedate = datetime.combine(basedate,
                                datetime.strptime(start_time, '%H').time().replace(tzinfo=timezone.utc))

    date_begin = basedate
    if freeze and max(basedate, freeze) > basedate:
        date_begin = freeze + timedelta(days=1)

    # date_str_begin = str(date_str_begin).replace('-', '')
    # dtstart = date_str_begin + time_str_begin

    # create begin and end strings, by adding the hour component. Hardcoded to UTC timezone to meet RRULE requirements
    date_begin = datetime.combine(date_begin,
                                  datetime.strptime(start_time, '%H').time().replace(tzinfo=timezone.utc))
    date_until = datetime.combine(week_end + timedelta(days=1),
                                  datetime.strptime('00', '%H').time().replace(tzinfo=timezone.utc))

    until = date_until.strftime(datetime_format)

    rule_string = f'RRULE:FREQ=DAILY;UNTIL={until};INTERVAL=2;WKST=MO'
    rule = rrulestr(rule_string, dtstart=date_begin)

    time_slots = rule.between(after=date_begin, before=date_until, inc=True)

    new_freeze = time_slots[-1] + timedelta(days=2)
    return(time_slots, new_freeze)


datetime_format = '%Y%m%dT%H%M%SZ'

start_date = datetime.strptime('2020-05-12', '%Y-%m-%d').date()
freeze_date = start_date + timedelta(days=2)
time_slots, new_freeze = _generate_week(start_date)

start_date = datetime.strptime('2020-05-18', '%Y-%m-%d').date()
time_slots2, new_freeze2 = _generate_week(start_date, new_freeze)

start_date = datetime.strptime('2020-05-25', '%Y-%m-%d').date()
time_slots3, new_freeze3 = _generate_week(start_date, new_freeze2)

start_date = datetime.strptime('2020-06-01', '%Y-%m-%d').date()
time_slots4, new_freeze4 = _generate_week(start_date, new_freeze3)

print(time_slots)
print(new_freeze)

print(time_slots2)
print(new_freeze2)

print(time_slots3)
print(new_freeze3)

print(time_slots4)
print(new_freeze4)
