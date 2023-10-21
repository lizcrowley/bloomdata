'''
The Student parent class below holds two attributes (gca and knowledge)
and two methods (study and outcome).
'''
class Student:
    '''
    The two attributes below hold the students gca score and whether the student is
    knowledgable or not.
    The study method determines whether the student studied a lot or not a lot this week
    based on the amount of hours studied. The outcome method determines how likely it is
    that this student lands a job based on their gca score.
    '''
    def __init__(self, gca, hours_studied = None):
        self.gca = gca
        self.hours_studied = hours_studied

    def study(self, hours_studied):
        if hours_studied is None:
            return 'not a lot this week'
        if hours_studied > 0 and hours_studied < 10:
            return 'some this week'
        if hours_studied > 10:
            return 'a lot this week'

    def outcome(self):
        if self.gca < 650:
            return "not likely"
        if self.gca > 650 and self.gca < 750:
            return "more likely"
        return "very likely"

    def __repr__(self):
        return f'''A student with a GCA score of {self.gca} who studied 
        {self.study(25)} will be {self.outcome()} to get a job'''

#if __name__ == "__main__":
    #my_student = Student(682, True)

    #print(my_student)


class BloomTechStudent(Student):
    '''
    The language attribute is supposed to determine what job the BloomTech student 
    is to receive.
    '''
    def __init__(self, gca, hours_studied, language):
        super().__init__(gca, hours_studied)
        self.language = language

    def job(self):
        if self.language == 'python' and self.gca > 700:
            return 'as a Data Scientist.'
        if self.language == 'java' and self.gca > 700:
            return 'as a Software Developer.'
        if self.language == 'html' and self.gca > 700:
            return 'as a Software Developer.'
        return 'as a Janitor.'

    def __repr__(self):
        return f'''A BloomTech student with a GCA score of {self.gca} who studied 
        {self.study(25)} will be {self.outcome()} to get a job {self.job()}'''

#if __name__ == "__main__":
    #my_student = BloomTechStudent(750, True, 'python')

    #print(my_student)
