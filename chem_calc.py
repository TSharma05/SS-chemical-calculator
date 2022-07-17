from product_list import *


def get_H2O2(param):
    key = 'name'
    value = 'hydrogen peroxide'

    list_of_values = [ele[key] for ele in param]

    if value in list_of_values:
        print(f"{value} is in the list")
        sum_max = sum(ele['max (%)'] for ele in param)
        percent_H2O2 = round((param[list_of_values.index(value)]['max (%)'] / sum_max) * 100, 2)
        print(percent_H2O2)
    else:
        print(f"{value} is not in the list")


# get_H2O2(product_1)
# get_H2O2(product_2)
# get_H2O2(product_3)


def get_avail_oxygen(param):
    # print(param)
    # print(type(param))
    sum_of = 0

    for i in param:
        n_i = i['num of peroxyl groups']
        c_i = i['max (%)']
        m_i = i['molecular mass']
        calc = (n_i * c_i) / m_i
        sum_of += calc
    print(sum_of)
    O_a = round((16 * sum_of), 2)
    print(f"{O_a}% of oxygen is available")

# get_avail_oxygen(product_1)
# get_avail_oxygen(product_2)
# get_avail_oxygen(product_3)
