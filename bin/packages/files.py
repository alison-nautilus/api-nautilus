#!/bin/python3

import os

class SystemPaths:
    def __init__(self):
        self.base_path = self.__get_base_path()
        self.app_path = self.__check_folder(self, "/bin")
        self.packages_path = self.__check_folder(self, "/pacakages")
        self.artifacts_path = self.__check_folder(self, "/artifacts")
        self.config_path = self.__check_folder(self, "/config")
        self.sys_config_file_path = self.config_path + "/config.json" if (FileOperations(self.config_path + "/config.json").exists()) and (FileOperations.is_file(self.config_path + "/config.json")) else None

    def __get_base_path(self):
        final_char = str(os.path.abspath(os.path.dirname(__file__))).find("k8-navigator") + len("k8-navigator")
        return str(os.path.abspath(os.path.dirname(__file__)))[:final_char]

    def __check_folder(self, param):
        if FileOperations(self.get_base_path + param).exists():
            return self.base_path + param
        return None

class FileOperations:
    def __init__(self, path):
        self.path = path if (path is not None) and (self.exists(path)) else None
        self.file_handler = self.open() if self.exists() and self.is_file() else None    
    
    def exists(self):
        return os.path.exists(self.path)

    def is_file(self):
        return os.path.isfile(self.path)

    def open(self, write=False):
        if write: 
            open_param = "w" 
        else: 
            open_param = "r"
        if self.is_file(self.path):  
            return open(self.path, open_param)

    def write(self, content):
        if self.file_handler is not None:
            self.file_handler.write(content)
            self.file_handler.close()

        
