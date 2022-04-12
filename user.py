from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    height: float
    weight: float
    age: int
    gender: str
