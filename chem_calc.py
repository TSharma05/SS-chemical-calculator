from product_list import *


def get_H2O2(param):
    key = 'name'
    value = 'hydrogen peroxide'

    list_of_values = [ele[key] for ele in param]

    if value in list_of_values:
        # print(f"{value} is in the list")
        sum_max = sum(ele['max (%)'] for ele in param)
        percent_H2O2 = round((param[list_of_values.index(value)]['max (%)'] / sum_max) * 100, 2)
        # print(percent_H2O2)
        return percent_H2O2
    else:
        # print(f"{value} is not in the list")
        return 0


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
    # print(sum_of)
    O_a = round((16 * sum_of), 2)
    # print(f"{O_a}% of oxygen is available")
    return O_a

# get_avail_oxygen(product_1)
# get_avail_oxygen(product_2)
# get_avail_oxygen(product_3)


def determine_classification(param):
    percent_H2O2 = get_H2O2(param)
    available_O_a = get_avail_oxygen(param)

    if percent_H2O2 <= 1.0 and available_O_a <= 1.0:
        return "not an Organic Peroxide according to CFR 173.128(a)(4)(i)"
    elif percent_H2O2 > 1.0 and percent_H2O2 <= 7.0 and available_O_a <= 0.5:
        return "not an Organic Peroxide according to CFR 173.128(a)(4)(ii)"
    else:
        return "an Organic Peroxide according to CFR 173.128(a)(4)"


print(f"Product 1 is {determine_classification(product_1)}")
print(f"Product 2 is {determine_classification(product_2)}")
print(f"Product 3 is {determine_classification(product_3)}")
# determine_classification(product_2)
# determine_classification(product_3)