#!/usr/bin/python3
"""
Class Student that defines a student by: (based on 10-student.py)
"""


class Student():
    """
    Public Instance Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with first name, last name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
        If attrs is a list of strings, only attributes name contain in this list must be retrieved.
        Otherwise, all attributes must be retrieved

        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dic[attr] = self.__dict__[attr]
            return dic

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for i, j in json.items():
            setattr(self, i, j)
