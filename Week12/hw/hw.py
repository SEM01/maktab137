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
    reminder_type:str = "Simple"

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
    
    def remind():
        print("All Simple Reminders")
        reminders = [reminder for reminder in All_Reminders if reminder.get("reminder_type")=='Simple']
        for item in reminders:
            print(f"{item}")
            logger.info("Remind Running")


@dataclass
class MeetingReminder(Reminder):
    participants: list = Any
    reminder: dict = field(default_factory=dict)
    reminder_type :str = 'Meeting'

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

    def remind():
        print("All Meeting Reminders")
        reminders = [reminder for reminder in All_Reminders if reminder.get("reminder_type")=='Meeting']
        for item in reminders:
            print(f"{item}")
            logger.info("Remind Running")

@dataclass
class DailyRoutineReminder(Reminder):
    repeat: bool = True
    reminder_list = []
    reminder: dict = field(default_factory=dict)
    reminder_type:str = 'Daily'

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

    def remind():
        print("All Daily Reminders")
        reminders = [reminder for reminder in All_Reminders if reminder.get("reminder_type")=='Daily']
        for item in reminders:
            print(f"{item}")
            logger.info("Remind Running")

@dataclass
class ReminderManager:
    def add_reminder():
        logger.info("Reminder add")

    def list_reminders():
        print("All Reminders")
        for reminder in All_Reminders:
            print(f"{reminder}")

    def remove_reminder(id):
        for i,reminder in enumerate(All_Reminders):
            if reminder.get('reminder_id') == id:
                All_Reminders.pop(i)
                logger.warning("Reminder removed")

    def search(id):
        for i,reminder in enumerate(All_Reminders):
            if reminder.get('reminder_id') == id:
                print(reminder)



# task1 = MeetingReminder(title="Speaking", time="10", participants=["a", "b"])
# task2 = SimpleReminder(title="a", time="10")
# task3 = SimpleReminder(title="b", time="10")
# SimpleReminder.remind()
# ReminderManager.remove_reminder(1)
# ReminderManager.list_reminders()
# ReminderManager.search(2)
