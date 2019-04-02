#
# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 3 - Assignment 1: Superclasses
#
# I'm choosing to build a Time Keeper app for the Week 8 project,
# so I will start by describing users.
#


class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def __repr__(self):
        return "{}, {}".format(self.__last_name, self.__first_name)

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name


class Employee(Person):
    UNDEFINED_EMP = "U"
    EXEMPT_EMP = "X"
    HOURLY_EMP = "H"
    TEMPORARY_EMP = "T"

    REGULAR_WORK_HOURS_PER_WEEK = 40

    def __init__(self, first_name, last_name, employee_id):
        super(Employee, self).__init__(first_name, last_name)
        self.__emp_id = employee_id
        self.__employee_classification = self.UNDEFINED_EMP

    def __repr__(self):
        return "{} [{}]".format(super().__repr__(), self.__emp_id)

    def get_employee_id(self):
        return self.__emp_id

    def get_employee_type(self):
        return self.__employee_classification

    def set_employee_type(self, classification):
        self.__employee_classification = classification


class ExemptEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, people_lead, bonus_rate):
        super(ExemptEmployee, self).__init__(first_name, last_name, employee_id)
        super().set_employee_type(self.EXEMPT_EMP)
        self.__people_lead = people_lead
        self.__bonus_rate = bonus_rate

    def get_bonus_rate(self):
        return self.__bonus_rate / 100

    def is_people_lead(self):
        return self.__people_lead

    def calc_bonus(self, hours_worked):
        return 1.0 + (self.__bonus_rate / 100) * hours_worked


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, overtime_rate, max_overtime):
        super(HourlyEmployee, self).__init__(first_name, last_name, employee_id)
        self.__employee_classification = self.HOURLY_EMP
        self.__overtime_rate = overtime_rate
        self.__max_overtime = max_overtime

    def get_overtime_rate(self):
        return self.__overtime_rate

    def set_overtime_rate(self, rate):
        self.__overtime_rate = rate

    def get_max_overtime(self):
        return self.__max_overtime

    def set_max_overtime(self, max_overtime):
        self.__max_overtime = max_overtime

    #
    # calc_paid_hours:
    # Calculating paid hours for hourly workers
    # requires an overtime rate for all hours >
    # self.REGULAR_WORK_HOURS_PER_WEEK.  This
    # function returns a value that
    # when multiplied by the rate will calculate
    # the pay total.
    #
    def calc_paid_hours(self, hours_worked):
        if hours_worked <= self.REGULAR_WORK_HOURS_PER_WEEK:
            return hours_worked
        else:
            # Overtime hours measured at the rate supplied
            return self.REGULAR_WORK_HOURS_PER_WEEK + \
                   ((hours_worked - self.REGULAR_WORK_HOURS_PER_WEEK) * self.__overtime_rate)

    #
    # calc_comp_time:
    # There is a max budget for overtime, so any additional time
    # worked above the "max overtime" range is tracked as
    # comp time.
    #
    def calc_comp_time(self, hours_worked):
        total_paid_hours = self.__max_overtime + self.REGULAR_WORK_HOURS_PER_WEEK
        if total_paid_hours < hours_worked:
            return hours_worked - total_paid_hours
        else:
            return 0


class Contractor(Employee):
    FIXED_RATE_TYPE = "F"
    HOURLY_RATE_TYPE = "H"

    def __init__(self, first_name, last_name, employee_id, rate_type):
        super(Contractor, self).__init__(first_name, last_name, employee_id)
        super().set_employee_type(self.TEMPORARY_EMP)
        self.__rate_type = rate_type

    def get_rate_type(self):
        return self.__rate_type

    def calc_paid_hours(self, hours_worked):
        if self.__rate_type == self.FIXED_RATE_TYPE:
            return 1.0
        else:
            return hours_worked

    def calc_bonus_multiplier(self, hours_worked, original_estimate):
        if self.__rate_type == self.FIXED_RATE_TYPE and hours_worked < original_estimate:
            return 1.1
        else:
            if hours_worked < original_estimate * 0.5:
                return 1.25
            elif hours_worked < original_estimate * 0.75:
                return 1.1
            else:
                return 1.0
