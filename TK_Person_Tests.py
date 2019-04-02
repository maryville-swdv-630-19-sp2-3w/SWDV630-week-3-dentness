#
# SWDV-630-3W 2019/SP2
# Joe Dent
# Week 3 - Assignment 1: Superclasses
#
#
# Testing Application

import TK_Person


def test_person(person):
    print(person)
    print("First Name: {}\nLast Name: {}".format(person.get_first_name(), person.get_last_name()))


def test_employee(emp):
    test_person(emp)
    print("Employee ID: {}\nEmployee Type: {}".format(emp.get_employee_id(), emp.get_employee_type()))


def test_exempt_employee(emp, hourly_rate, hours_worked):
    test_employee(emp)
    print("People Lead: {}".format(emp.is_people_lead()))
    print("Bonus Rate: {}".format(emp.get_bonus_rate()))
    print("Bonus for {} hours worked is ${:8.2f}".format(hours_worked,
                                                         emp.get_bonus_rate() * (hourly_rate * hours_worked)))


def test_hourly_employee(emp, pay_rate, hours_worked):
    test_employee(emp)
    print("Overtime Rate: {}\nMax overtime hours: {}".format(emp.get_overtime_rate(), emp.get_max_overtime()))
    print("Hours Paid: {}\nHours comp: {}".format(emp.calc_paid_hours(hours_worked), emp.calc_comp_time(hours_worked)))
    print("Total pay: {}".format(pay_rate * emp.calc_paid_hours(hours_worked)))


def test_contract_employee(emp, pay_rate, hours_worked, original_estimate):
    test_employee(emp)
    print("Rate Type: {}\nRate {}".format(emp.get_rate_type(), pay_rate))
    print("Paid Hours: {}".format(emp.calc_paid_hours(hours_worked)))
    print("Original Est: {}".format(original_estimate))
    bonus_multiplier = emp.calc_bonus_multiplier(hours_worked, original_estimate)
    print(
        "Bonus Multiplier {}\nCalc bonus: {}".format(bonus_multiplier, bonus_multiplier * (hours_worked * pay_rate)))


def main():
    print("Person")
    test_person(TK_Person.Person("Peter", "Parker"))
    print("")

    print("Employee (Generic)")
    test_employee(TK_Person.Employee("May", "Parker", 300301))
    print("")

    print("Exempt Employee - Individual Contributor")
    test_exempt_employee(TK_Person.ExemptEmployee("Mary Jane", "Watson", 288100, False, 2.5), 100.00, 46.00)
    print("")

    print("Exempt Employee - People Lead")
    test_exempt_employee(TK_Person.ExemptEmployee("JJ", "Jameson", 130233, True, 9.5), 100.00, 90.0)
    print("")

    print("Hourly Employee")
    test_hourly_employee(TK_Person.HourlyEmployee("Ben", "Parker", 111000, 1.5, 8), 100.00, 2080.00)
    print("")

    print("Contract Employee - Fixed Bid")
    test_contract_employee(TK_Person.Contractor("Harry", "Osborn", 450023, TK_Person.Contractor.FIXED_RATE_TYPE),
                           10000.00, 200.00, 1000.00)
    print("")

    print("Contract Employee - Hourly")
    test_contract_employee(TK_Person.Contractor("Marvin", "Osborn", 450022, TK_Person.Contractor.HOURLY_RATE_TYPE),
                           100.00, 365.00, 600.00)
    print("")


main()
