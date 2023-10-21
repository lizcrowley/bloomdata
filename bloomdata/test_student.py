'''Imports such as pytest and student.py classes are necessary for these tests.'''
import pytest
from bloomdata.student import Student
from bloomdata.student import BloomTechStudent

'''Initializing pytest fixtures to clean up my test functions.'''
@pytest.fixture
def good_student():
    return Student(780)

@pytest.fixture
def good_btstudent():
    return BloomTechStudent(780, 15, 'python')


'''Testing the study method'''
def test_study(good_student):
    assert good_student.study(15) == "a lot this week"
    assert good_student.study(2) == "some this week"

'''Testing the outcome method'''
def test_outcome(good_student):
    assert good_student.outcome() == "very likely"

'''Testing the job method'''
def test_job(good_btstudent):
    assert good_btstudent.job() == "as a Data Scientist."
