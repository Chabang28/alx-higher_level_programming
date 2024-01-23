#!/usr/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and prints the results"""
    div = None
    result = None

    try:
        div = a / b
    except Exception:
        return
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if div is not None:
            print('Inside result: {:.1f}'.format(div))
        else:
            print('Inside result: ', div)
    return div
        print("Inside result: {:}" .format(result))
    return result
