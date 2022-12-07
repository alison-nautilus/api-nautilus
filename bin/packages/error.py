#!/bin/python3

import inspect
import traceback

from .files import SystemPaths

class Error:
    def __init__(self, ex):
        try:
            self.error_type = str(type(ex).__name__)
            self.error_args = self.__format_args(str(ex.args))
            self.error_traceback = self.__format_stack()
        except Exception as e:
            self.__print_class_exception(e)

    def __format_stack(self):
        stack_list = traceback.extract_stack()
        stack_text = ""
        paths = SystemPaths()
        for line in stack_list:
            if paths.base_path in line.filename:
                stack_text = stack_text + line.filename + " at line " + str(line.lineno) + "\n"
        return stack_text[:-1]

    def __format_type(self, type_str):
        return type_str.split(":")[1].replace(" ", "")

    def __format_args(self, args_str):
        return args_str.replace('", "', ", ").replace('","', ", ")[2:-3]
            
    def __print_class_exception(self, e):
        raise(str(e))

    def show(self, item=None):
        case = ["type", "args", "traceback"]
        if item in case and item is not None:
            case = list(filter(lambda x: x == item, case))

        for c in case:
            for i in inspect.getmembers(self):
                if not i[0].startswith('_') and not inspect.ismethod(i[1]) and c in i[0]:
                            print('{}: {}'.format(i[0], self.__select_atribute(c)))
    
    def __select_atribute(self, item):
        switch = {
            "type": self.error_type,
            "args": self.error_args,
            "traceback": self.error_traceback
        }
        return switch.get(item)


