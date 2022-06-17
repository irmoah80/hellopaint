from typing import Any

class Stack:
    array = None
    def __init__(self):
        self.array = []

    def push(s, value: Any) -> None:
        s.array.append(value)

    def pop(s) -> Any:  # Time Complexity: O(1)
        return s.array.pop()

    def size(self) -> int:
        return len(self.array)
    
    def top(self):  # Time Complexity: O(1)
        if self.is_empty():
            return False
        else:
            return self.array[-1]

    def down(self):
        if self.is_empty():
            return False
        else:
            return self.array[0]

    def clear(self) -> bool:
        self.array = []

    def is_empty(self) -> bool:  # Time Complexity: O(1)
        return len(self.array) == 0
