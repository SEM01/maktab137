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


task1 = Reminder("wake", "10.20")
print(task1)
task2 = Reminder("wake", "10.20")
print(task2)
