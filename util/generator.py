import string
import random
from faker import Faker
from random_username.generate import generate_username as gen_username

fake = Faker('nl_BE')


def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def generate_names():
    return fake.name().split(' ')[:2]


def generate_username():
    return gen_username(1)[0].lower()
