# from passlib.hash import sha256_crypt as crypt
from os import urandom
from _hashlib import pbkdf2_hmac as crypt

class User:
    __users = {}

    def __new__(cls, *args, **kwargs):
        user = cls.__users.get(args[0])
        if user:
            return user
        else:
            return super().__new__(cls)

    def __init__(self,nickname,password,age):
        if User.__users.get(nickname):
            return

        self.nickname = nickname
        self.password = self.hash(password)
        self.age = age
        User.__users[nickname] = self

    @classmethod
    def get_users(cls):
        return [user for user in cls.__users.values()]

    def __str__(self):
        return f'Nickname: {self.nickname}, Age: {self.age}'

    @staticmethod
    def hash(password:str):
        salt = urandom(32)
        key = crypt('sha256', password.encode('utf-8'), salt, 10_000)
        # print('Salt:', salt)
        # print('Key:', key)
        storage = salt + key
        return storage


    def check_password(self,password:str):
        salt = self.password[:32]
        key = self.password[32:]
        key_for_check = crypt('sha256', password.encode('utf-8'), salt, 10_000)
        # print(f'Salt: {salt}, key: {key}, key_for_check: {key_for_check}')
        return key == key_for_check