from FluentPython.chapter19.osconfeed import load
from FluentPython.chapter19.explore0 import FrozenJSON

raw_feed = load()   # dict type

feed = FrozenJSON(raw_feed)
# l_val = len(feed.Schedule.speakers)
# print(l_val)

# sorted_val = sorted(feed.Schedule.keys())
# print(sorted_val)

'''attr_data = feed.items
print(attr_data)
print(type(attr_data))'''

schedule_data = feed.Schedule
# print(schedule_data)

speaker_data = schedule_data.speakers
# print(speaker_data)




