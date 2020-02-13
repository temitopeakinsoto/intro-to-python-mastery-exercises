class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def cal_annual_salary(self):
        return self.pay*12 + self.bonus

    def __str__(self):
        return f"I earn {self.pay} monthly!"

class NYSC:
    def __init__(self, name, pay, bonus):
        self.name = name
        self.allowee = Salary(pay, bonus)

    def __str__(self):
        return f" Hi, I am {self.name} and my allowee is {self.allowee.cal_annual_salary()}"

youth_corper = NYSC("GREG", 1800, 1000)
print(youth_corper)

sal1 = Salary(2000, 1000)
print(sal1.cal_annual_salary())