class DeskHuman(object):

    _genders = ('m', 'w')

    def __init__(self, **kwargs):
        self.__name = kwargs['name']
        self.__surname = kwargs['surname']
        self.__patronymic = kwargs['patronymic']
        gender = kwargs['gender'].lower()
        if gender not in DeskHuman._genders:
            raise ValueError("Unknown gender: {}".format(gender))
        self.__gender = gender

    def name(self):
        return self.__name

    def surname(self):
        return self.__surname

    def patronymic(self):
        return self.__patronymic

    def gender(self):
        return self.__gender

    def __str__(self):
        return "{0} {1} {2}, gen = {3}".format(self.__surname, self.__name, self.__patronymic, self.__gender)

    def __repr__(self):
        return "DeskHuman: [{}]".format(self.__str__())

    @staticmethod
    def to_desk(obj: dict):
        return DeskHuman(name=obj['name'], surname=obj['surname'], patronymic=obj['patronymic'], gender=obj['gender'])


class Student(object):

    def __init__(self, **kwargs):
        self.__desk = kwargs['desk']
        self.__course = kwargs['course']
        self.__mark = kwargs['mark']

    def description(self):
        return self.__desk

    def course(self):
        return self.__course

    def mark(self):
        return self.__mark

    def __str__(self):
        return "{0}; c = {1}, m = {2}".format(self.__desk, self.__course, self.__mark)

    def __repr__(self):
        return "Student: [{}]".format(self.__str__())

    @staticmethod
    def to_student(obj: dict):
        return Student(mark=obj['mark'], course=obj['course'], desk=DeskHuman.to_desk(obj['desk']))
