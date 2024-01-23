#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides elements by element 2 lists"""
    div_list = []
    for i in range(list_length):
        div = None
    list_div = []

    for x in range(list_length):
        div = 0

        try:
            if isinstance(my_list_1[i], (int, float)):
                div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        except TypeError:
            print('wrong type')
            div = my_list_1[x] / my_list_2[x]
        except (ValueError, ZeroDivisionError):
            print("division by 0")
            div = 0  # set division result to 0
        except (TypeError):
            print("wrong type")
            div = 0
        except (IndexError):
            print("out of range")
            div = 0

        finally:
            if div is not None:
                div_list.append(div)
            else:
                div_list.append(0)
    return div_list
            list_div.append(div)  # add division result into new list

    return list_div
