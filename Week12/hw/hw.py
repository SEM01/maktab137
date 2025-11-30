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
    time: str
    reminder_id: int = field(default_factory=lambda: next(id))


@dataclass
class SimpleReminder(Reminder):
    def __repr__(self):
        return f"It is Time: {Reminder.title}"


@dataclass
class MeetingReminder(Reminder):
    participants: list


@dataclass
class DailyRoutineReminder(Reminder):
    repeat: bool


@dataclass
class ReminderManager: ...
