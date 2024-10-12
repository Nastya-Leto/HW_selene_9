from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    subjects: str
    current_address: str
    birthday: dict[str, int]


student = User('Анастасия', 'З', 'test@mail.ru', '7927000000', 'Arts', "Samara", birthday={
    "day": 20,
    "month": 6,
    "year": 1995
})
