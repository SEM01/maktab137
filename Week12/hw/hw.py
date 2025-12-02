from dataclasses import dataclass, field
from typing import Any
import logging
from logging.handlers import RotatingFileHandler


logger_format = logging.Formatter(
    "%(name)s - %(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("Reminder LOG")
handler = RotatingFileHandler(
    filename="reminder.log",
    maxBytes=1000,
    backupCount=5,
)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
handler.setFormatter(logger_format)


def id_gen():
    i = 1
    while True:
        yield i
        i += 1


id = id_gen()


@dataclass
class Reminder:
    title: str
    time: str = "00:00"
    reminder_id: int = field(default_factory=lambda: next(id))


@dataclass
class SimpleReminder(Reminder):
    reminder_list = []

    def __post_init__(self):
        if self.title == "" or self.time == "":
            logger.error("Empty")
        else:
            SimpleReminder.reminder_list.append(self.reminder_id)
            SimpleReminder.reminder_list.append(self.title)
            SimpleReminder.reminder_list.append(self.time)
            print(SimpleReminder.reminder_list)

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> It is Time: {self.title}"


@dataclass
class MeetingReminder(Reminder):
    participants: list = Any
    reminder_list = []

    def __post_init__(self):
        if self.title == "" or self.time == "":
            logger.error("Empty")
        else:
            MeetingReminder.reminder_list.append(self.reminder_id)
            MeetingReminder.reminder_list.append(self.title)
            MeetingReminder.reminder_list.append(self.time)
            print(MeetingReminder.reminder_list)

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> Meeting Reminder: {self.title}--->{self.participants}"


@dataclass
class DailyRoutineReminder(Reminder):
    repeat: bool = True
    reminder_list = []

    def __post_init__(self):
        if self.title == "" or self.time == "":
            logger.error("Empty")
        else:
            DailyRoutineReminder.reminder_list.append(self.reminder_id)
            DailyRoutineReminder.reminder_list.append(self.title)
            DailyRoutineReminder.reminder_list.append(self.time)
            print(DailyRoutineReminder.reminder_list)

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> Daily Routine: {self.title} <Daily Reminder Active>"


@dataclass
class ReminderManager:
    def add_reminder():
        logger.info("Reminder add")

    def list_reminders():
        print("Simple Reminder")
        print(f"{SimpleReminder.reminder_list}", end="\n")
        print("Meeting")
        print(f"{MeetingReminder.reminder_list}", end="\n")
        print("Daily")
        print(f"{DailyRoutineReminder.reminder_list}", end="\n")


# task1 = MeetingReminder(title="Speaking", time="10", participants=["a", "b"])
# # ReminderManager.add_reminder()


# task2 = SimpleReminder(title="a", time="10")
# task3 = SimpleReminder(title="b", time="10")
# ReminderManager.list_reminders()
