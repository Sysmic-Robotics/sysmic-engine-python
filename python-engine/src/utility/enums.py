from enum import Enum

# class syntax
class TaskState(Enum):
    IN_PROCESS = 1
    FAILED = 2
    SUCCESS = 3