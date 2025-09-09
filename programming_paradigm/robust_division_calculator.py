# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division with error handling for zero division and non-numeric inputs.
    
    Args:
        numerator: The numerator as a string
        denominator: The denominator as a string
        
    Returns:
        str: Result message with division result or error message
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except ValueError:
        return "Error: Please enter numeric values only."
        
    except Exception as e:
        return f"Error: {str(e)}"