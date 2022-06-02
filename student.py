class Student:
    school="AkiraChix"
    def __init__(self ,full_name ,year_of_birth ,initials):
        self.full_name = full_name
        self.year_of_birth = year_of_birth
        self.initials = initials

    def full_name(self):
        return f"hello { self.full_name} from Kenya"

    def year_of_birth(self):
        return f"you were born in { self.year_of_birth}"

    def initials(self):
        return f"your initials are{self.initials}"        


        
