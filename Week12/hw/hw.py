from dataclasses import dataclass, field
from typing import Any
import logging
from logging.handlers import RotatingFileHandler

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
#     filename="reminder.log",
#     filemode="a",
# )
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
    def __post_init__(self):
        if self.title == "" or self.time == "":
            logger.error("Empty")
        else:
            reminder_list = []
            reminder_list.append(self.reminder_id)
            reminder_list.append(self.title)
            reminder_list.append(self.time)
            print(reminder_list)

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> It is Time: {self.title}"


@dataclass
class MeetingReminder(Reminder):
    participants: list = Any

    def __post_init__(self):
        if self.title == "" or self.time == "":
            logger.error("Empty")
        else:
            reminder_list = []
            reminder_list.append(self.reminder_id)
            reminder_list.append(self.title)
            reminder_list.append(self.time)
            print(reminder_list)

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> Meeting Reminder: {self.title}--->{self.participants}"


@dataclass
class DailyRoutineReminder(Reminder):
    repeat: bool = False


@dataclass
class ReminderManager:
    def add_reminder():
        logger.info("Reminder add")


task1 = MeetingReminder(title="Speaking", time="10", participants=["a", "b"])
ReminderManager.add_reminder()


task2 = SimpleReminder(title="", time="10")
