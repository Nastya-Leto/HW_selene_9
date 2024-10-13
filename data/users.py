from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    female: str
    phone_number: str
    birthday: dict[str, int]
    subjects: str
    hobbies: str
    file_name_download: str
    current_address: str
    state: str


student = User(
    'Анастасия',
    'З',
    'test@mail.ru',
    'Female',
    '7927000000',
    {"day": 20, "month": 6, "year": 1995},
    'Arts',
    'Music',
    'image.jpg',
    'Samara',
    'Haryana Karnal'
)
