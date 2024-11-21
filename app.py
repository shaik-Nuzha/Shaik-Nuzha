# app.py

def add(a, b):
    return a + b

def get_output():
    return f"5 + 3 = {add(5, 3)}"

if _name_ == "_main_":
    print(get_output())  # This will print the result if run directly
