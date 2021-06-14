class Employee:
    parameter = 5
    rise = 1.15
    personal_count = 0

    def __init__(self, first_name, last_name, wage):
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage
        self.email = self.first_name + self.last_name + "@company.com"
        Employee.personal_count += 1

    def full_name(self):
        return "First Name: {} - Last Name: {}".format(self.first_name, self.last_name)

    def increase(self):
        self.wage = (self.wage * self.rise)

    @classmethod
    def change_rise(cls, new_ratio):
        cls.rise = new_ratio

    @classmethod
    def new_personal(cls, personal_info):
        first_name, last_name, wage = personal_info.split("-")
        return cls(first_name, last_name, wage)

    @staticmethod
    def tel_no(telephone):
        return telephone.split(" ")


personal1 = Employee("Ali", "Kivrak", 5000)

text_personal1 = "Veli-Can-4000"

new_personal1 = Employee.new_personal(text_personal1)
# new_personal1.change_rise(2)
# new_personal1.increase()
print(new_personal1.wage)

num_tel = "0123 456 78 90"
print(Employee.tel_no(num_tel))
