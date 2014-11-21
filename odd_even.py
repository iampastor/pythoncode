#coding:utf-8
is_odd_number = lambda data:(data%2!=0)

def odd_even_sort(lst):
    """利用list conprehension"""
    tmp_list1 = [item for item in lst if is_odd_number(item)]
    tmp_list2 = [item for item in lst if not is_odd_number(item)]
    tmp_list1.extend(tmp_list2)
    return tmp_list1

test_lst = [7,9,12,5,4,9,8,3,12,89]

print (odd_even_sort(test_lst))