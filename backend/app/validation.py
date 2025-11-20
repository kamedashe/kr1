def validate_value(value):
    """
    Validates the input value based on equivalence classes.
    
    Args:
        value: The input value to validate.
        
    Returns:
        int: The validated integer value.
        
    Raises:
        ValueError: If the value is invalid.
    """
    if value is None or value == "":
        raise ValueError("Поле обов'язкове")
    
    # Check if it's a float first to give specific error
    if isinstance(value, float) or (isinstance(value, str) and '.' in value and value.replace('.', '', 1).isdigit()):
            raise ValueError("Потрібно ціле число")

    try:
        int_val = int(value)
    except (ValueError, TypeError):
        # Check if it's a float string that failed int conversion or just random text
        # The requirement says "Потрібно ввести число" for letters/specials
        # and "Потрібно ціле число" for floats.
        
        if isinstance(value, str) and any(c.isalpha() for c in value):
             raise ValueError("Потрібно ввести число") # EC4
        if isinstance(value, str) and any(not c.isalnum() for c in value):
             raise ValueError("Потрібно ввести число") # EC5
        
        # Fallback for other non-integers
        raise ValueError("Потрібно ввести число")


    if int_val < 1 or int_val > 100:
        raise ValueError("Число має бути від 1 до 100")
        
    return int_val
