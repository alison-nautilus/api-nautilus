#!/bin/python

from fastapi import FastAPI

from .packages import Error

class Main():
    def __init__(self) -> None:
        self.start()

    def start(self):
        try:
            self.__start()
        except Exception as e:
            Error(e).show()

    def __start(self):
        print("Hello World")

