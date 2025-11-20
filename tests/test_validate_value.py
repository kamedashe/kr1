import pytest
import sys
import os

# Add the backend directory to sys.path so we can import the app module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app.validation import validate_value

@pytest.mark.parametrize("input_value, expected", [
    ("42", 42),   # EC1: Valid representative
    ("1", 1),     # Boundary
    ("100", 100), # Boundary
])
def test_valid_values(input_value, expected):
    assert validate_value(input_value) == expected

@pytest.mark.parametrize("input_value, errmsg", [
    ("0", "Число має бути від 1 до 100"),      # EC2: Too small
    ("101", "Число має бути від 1 до 100"),    # EC3: Too large
    ("abc", "Потрібно ввести число"),          # EC4: Letters
    ("@#", "Потрібно ввести число"),           # EC5: Specials
    ("", "Поле обов'язкове"),                  # EC6: Empty
    ("3.14", "Потрібно ціле число"),           # EC7: Float
])
def test_invalid_values_raise(input_value, errmsg):
    with pytest.raises(ValueError) as exc:
        validate_value(input_value)
    assert errmsg in str(exc.value)

