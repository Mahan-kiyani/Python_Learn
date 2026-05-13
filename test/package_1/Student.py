class Student:
        """
        This class is for the user's student information.
        """
        
        def __init__(self, name = None, _id = None, age: int = None):
            """Initialize the student's name and student ID."""
            self.name = name
            self._id= _id
            self.age = age
        
        def score(self):
            self.moadel = None

_g = 65 
__all__ = ['_g', 'Student']