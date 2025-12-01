from dataclasses import dataclass, field
from typing import Any
import logging

logging.basicConfig(filename="reminder.log", filemode="a")


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

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> It is Time: {self.title}"


@dataclass
class MeetingReminder(Reminder):
    participants: list = Any

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> Meeting Reminder: {self.title}--->{self.participants}"


@dataclass
class DailyRoutineReminder(Reminder):
    repeat: bool = False


@dataclass
class ReminderManager: ...


task1 = MeetingReminder(title="Speaking", time="10", participants=["a", "b"])
print(task1)

task2 = SimpleReminder(title="Cooking", time="10")
print(task2)
