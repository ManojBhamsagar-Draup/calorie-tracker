from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    height: float
    weight: float
    age: int
    gender: str
    bmi: float = 0.0

    def __post_init__(self):
        self.bmi = round((self.weight / (self.height ** 2)), 2)
