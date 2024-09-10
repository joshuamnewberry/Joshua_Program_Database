class NonPositiveError(Exception):
    def __init__(self):
        pass
    def __str__(self) -> str:
        return "Input must be a positive number"

def AreaOfRectangle(l:float, w:float) -> int | float:
    try:
        if l <= 0 or w <= 0:
            raise NonPositiveError
        print(f"Area of Rectangle: {l * w}")
    except ValueError as msg:
        print("Inputs should be numbers,", msg)
    except NonPositiveError as msg:
        print(msg)
