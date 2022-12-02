from calculadora import sumar, restar

# Happy path
def test_sumar_function_add_two_numbers():
    result = sumar(3, 5)

    assert result == 8

def test_restar_function_substract_two_numbers():
    result = restar(9, 3)
    
    assert result ==6



# Edge cases
def test_sumar_function_fails_if_first_number_letters():
    result = sumar('a', 5)

    assert result == 'Error, esto no es un numer'