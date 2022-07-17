from product_list import *

class getClassification():

    def __init__(self, param):
        self.param = param
        self.percent_H2O2 = 0
        self.O_a = 0
    

    def run_calc(self):
        self.get_H2O2()
        self.get_avail_oxygen()
        return self.determine_classification()

    def get_H2O2(self):
        key = 'name'
        value = 'hydrogen peroxide'

        list_of_values = [ele[key] for ele in self.param]

        if value in list_of_values:
            # print(f"{value} is in the list")
            sum_max = sum(ele['max (%)'] for ele in self.param)
            self.percent_H2O2 = round((self.param[list_of_values.index(value)]['max (%)'] / sum_max) * 100, 2)
            # print(self.percent_H2O2)
            return self.percent_H2O2
        else:
            # print(f"{value} is not in the list")
            return 0
    
    def get_avail_oxygen(self):
        # print(self.param)
        # print(type(self.param))
        sum_of = 0

        for i in self.param:
            n_i = i['num of peroxyl groups']
            c_i = i['max (%)']
            m_i = i['molecular mass']
            calc = (n_i * c_i) / m_i
            sum_of += calc
        # print(sum_of)
        self.O_a = round((16 * sum_of), 2)
        # print(f"{self.O_a}% of oxygen is available")
        return self.O_a
    
    def determine_classification(self):
        if self.percent_H2O2 <= 1.0 and self.O_a <= 1.0:
            return "not an Organic Peroxide according to CFR 173.128(a)(4)(i)"
        elif self.percent_H2O2 > 1.0 and self.percent_H2O2 <= 7.0 and self.O_a <= 0.5:
            return "not an Organic Peroxide according to CFR 173.128(a)(4)(ii)"
        else:
            return "an Organic Peroxide according to CFR 173.128(a)(4)"




p_1 = getClassification(product_1)
print(f"Product 1 is {p_1.run_calc()}")

p_2 = getClassification(product_2)
print(f"Product 2 is {p_2.run_calc()}")

p_3 = getClassification(product_3)
print(f"Product 3 is {p_3.run_calc()}")