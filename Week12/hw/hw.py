from dataclasses import dataclass, field
from typing import Any, List, Dict
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

All_Reminders: List[Dict[str, Any]] = []


@dataclass
class Reminder:
    reminder_id: int = field(default_factory=lambda: next(id))
    title: str = "Untiteld"
    time: str = "00:00"


@dataclass
class SimpleReminder(Reminder):
    reminder: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.title == "" or self.time == "":
            logger.error("Empty")
        else:
            for key, value in self.__dict__.items():
                if key != "reminder":
                    self.reminder[key] = value
        All_Reminders.append(self.reminder.copy())

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> It is Time: {self.title}"


@dataclass
class MeetingReminder(Reminder):
    participants: list = Any
    reminder: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.title == "" or self.time == "":
            logger.error("Empty")
        else:
            for key, value in self.__dict__.items():
                if key != "reminder":
                    self.reminder[key] = value
        All_Reminders.append(self.reminder.copy())

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> Meeting Reminder: {self.title}--->{self.participants}"


@dataclass
class DailyRoutineReminder(Reminder):
    repeat: bool = True
    reminder_list = []
    reminder: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.title == "" or self.time == "":
            logger.error("Empty")
        else:
            for key, value in self.__dict__.items():
                if key != "reminder":
                    self.reminder[key] = value
        All_Reminders.append(self.reminder.copy())

    def __repr__(self):
        return f"<Task ID:{self.reminder_id}> Daily Routine: {self.title} <Daily Reminder Active>"


@dataclass
class ReminderManager:
    def add_reminder():
        logger.info("Reminder add")

    def list_reminders():
        print("All Reminders")
        for record in All_Reminders:
            print(f"{record}")


task1 = MeetingReminder(title="Speaking", time="10", participants=["a", "b"])
# # ReminderManager.add_reminder()

task2 = SimpleReminder(title="a", time="10")
task3 = SimpleReminder(title="b", time="10")
ReminderManager.list_reminders()
