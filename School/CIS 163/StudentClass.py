class Student:

    def __init__(self, name:str="No Name", gpa:float=0, year:int=2000):
        self.name = str(name)
        self.gpa = float(gpa)
        self.year = int(year)
    
    def __str__(self):
        return f"{self.name} gradates/graduated in {self.year} and has/had a gpa of {self.gpa}"

    def get_name(self) -> str:
        return self.name
    
    def get_gpa(self) -> float:
        return self.gpa
    
    def get_year(self) -> int:
        return self.year
    
    def set_name(self, name) -> None:
        self.name = name
    
    def set_gpa(self, gpa) -> None:
        self.gpa = gpa
    
    def set_year(self, year) -> None:
        self.year = year
    
    def high_gpa_number(lst:list) -> int | float:
        max_gpa = lst[0].get_gpa()
        for i in lst:
            new_gpa = i.get_gpa()
            if new_gpa > max_gpa:
                max_gpa = new_gpa
        return max_gpa

    def high_gpa_name(lst:list) -> str:
        max_gpa = lst[0].get_gpa()
        max_name = lst[0].get_name()
        for i in lst:
            new_gpa = i.get_gpa()
            if new_gpa > max_gpa:
                max_gpa = new_gpa
                max_name = i.get_name()
        return max_name
    
    def high_gpa_year_number(lst:list, year:int) -> int | float:
        max_gpa = lst[0].get_gpa()
        for i in lst:
            new_gpa = i.get_gpa()
            if new_gpa > max_gpa and i.get_year == year:
                max_gpa = new_gpa
        return max_gpa

    def high_gpa_name_year(lst:list, year:int) -> str:
        max_gpa = lst[0].get_gpa()
        max_name = lst[0].get_name()
        for i in lst:
            new_gpa = i.get_gpa()
            if new_gpa > max_gpa and i.get_year == year:
                max_gpa = new_gpa
                max_name = i.get_name()
        return max_name
