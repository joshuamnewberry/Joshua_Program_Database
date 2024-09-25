class Course:

    def __init__(self, name:str, number:int, instructor:str, subject:str, prereqs:str=None) -> None:
        self.name = name
        self.number = number
        self.instructor = instructor
        self.subject = subject
        self.prereqs = prereqs
    
    def get_name(self) -> str:
        return self.name
    
    def get_number(self) -> int:
        return self.number
    
    def get_instructor(self) -> str:
        return self.instructor
    
    def get_subject(self) -> str:
        return self.subject
    
    def get_prereqs(self) -> str:
        return self.prereqs
    
    def set_name(self, name:str) -> None:
        self.name = name
    
    def set_number(self, number:int) -> None:
        self.number = number
    
    def set_instructor(self, instructor:str) -> None:
        self.instructor = instructor
    
    def set_subject(self, subject:str) -> None:
        self.subject = subject
    
    def set_prereqs(self, prereqs:str) -> None:
        self.prereqs = prereqs
    
    def cancel_course(self) -> None:
        self.name += "CANCELED"
        self.number = None
        self.instructor = None
        self.subject = None
        self.prereqs = None
        print("Class has been cancelled")