import sys

class MealyError(Exception):
    pass

class RaisesContext:
    def __init__(self, exception_type):
        self.exception_type = exception_type
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exception_type):
            self.exception = exc_val
            return True
        return False

def raises(exception_type):
    return RaisesContext(exception_type)

def test_mealy_error():
    with raises(MealyError) as e:
        raise MealyError("Mealy error occurred")
    assert isinstance(e.exception, MealyError)
    assert str(e.exception) == "Mealy error occurred"

if __name__ == "__main__":
    test_mealy_error()