#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    rtn_list = []
    i = 0
    try:
        while i < list_length:
            try:
                rtn_list.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                print("division by 0")
                rtn_list.append(0)
            except TypeError:
                print("wrong type")
                rtn_list.append(0)
            except IndexError:
                print("out of range")
                rtn_list.append(0)
            finally:
                i += 1
    except:
        pass
    finally:
        return (rtn_list)
