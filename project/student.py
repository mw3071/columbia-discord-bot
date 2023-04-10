class Student(object):
    def __init__(self, username, uni):
        self.username = username
        self.uni = uni
        self.classes = []
        self.profs = []

    def __str__(self) -> str:
        ret = ""
        ret += self.username + ", " + self.uni + ", ["
        for c in self.classes:
            ret += c + ", "
        ret += "], ["

        for p in self.profs:
            ret += p + ", "
        ret += "]"
        return ret

    def set_uni(self, u):
        '''Takes in a string u and changes the student's uni to u'''
        self.uni = u

    def add_class(self, c):
        '''Takes in a string c and adds that to the student's classes array'''
        if c not in self.classes:
            self.classes.append(c)
            print("added!")
        else:
            print("already added")

    def remove_class(self, c):
        '''Takes in a string c and removes it from the student's classes array'''
        if c in self.classes:
            self.classes.remove(c)
            print("removed")
        else:
            print("class not found")

    def add_prof(self, p):
        '''Takes in a string c and adds that to the student's prof array'''
        if p not in self.profs:
            self.profs.append(p)
            print("added!")

    def remove_prof(self, p):
        '''Takes in a string c and removes it from the student's prof array'''
        if p in self.profs:
            self.profs.remove(p)
            print("removed")
        else:
            print("prof not found")

    def get_profs(self):
        '''returns the student's prof array'''
        return self.profs

    def get_classes(self):
        '''returns the student's classes array'''
        return self.classes
