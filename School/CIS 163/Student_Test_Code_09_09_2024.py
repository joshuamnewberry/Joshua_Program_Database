from Student_Class_09_09_2024 import NonPositiveNumberError, NoGradeError, Student
import unittest

class TestStudentClass(unittest.TestCase):
    def test_StringOnlyName(self) -> None:
        a = Student("Joe")
        self.assertEqual("Joe", a.name)

    def test_StringOnlyList(self) -> None:
        a = Student("Joe")
        self.assertEqual([], a.grades)
    
    def test_ListEqual(self) -> None:
        a = Student("Jim", [1,2,3,4,5,10])
        self.assertEqual([1,2,3,4,5,10], a.grades)
    
    def test_avgGrades(self) -> None:
        a = Student("Joe", [1,3,5,7,9])
        self.assertEqual(5.0, a.calculate_average())
    
    def test_addGrades(self) -> None:
        a = Student("Joe", [1,5])
        a.add_grade(6)
        self.assertEqual([1,5,6], a.grades)
    
    def test_addNegativeGrade(self) -> None:
        a = Student("Jim", [2])
        with self.assertRaises(NonPositiveNumberError):
            a.add_grade(-7)
    
    def test_calculateAverageNone(self) -> None:
        a = Student("Jill")
        with self.assertRaises(NoGradeError):
            a.calculate_average()
    
if __name__ == "__main__":
    unittest.main()
