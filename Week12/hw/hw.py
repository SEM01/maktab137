from dataclasses import dataclass, field
from typing import Any


def id_gen():
    i = 1
    while True:
        yield i
        i += 1


id = id_gen()


@dataclass
class Reminder:
    title: str
    time: str = "0"
    reminder_id: int = field(default_factory=lambda: next(id))


@dataclass(init=False)
class SimpleReminder(Reminder):
    def __init__(self, title, time):
        self.title = title
        self.time = time

    def __repr__(self):
        return f"It is Time: {self.title}"


@dataclass(init=False)
class MeetingReminder(Reminder):
    def __init__(self, title, time, participants):
        self.title = title
        self.time = time
        self.participants = participants

    def __repr__(self):
        return f"Meeting Reminder: {self.title}--->{self.participants}"


@dataclass
class DailyRoutineReminder(Reminder):
    repeat: bool = False


@dataclass
class ReminderManager: ...


task1 = MeetingReminder("Speaking", "10", ["A", "b"])
print(task1)
