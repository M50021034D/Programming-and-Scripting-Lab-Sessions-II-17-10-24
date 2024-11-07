
def employee_pay():
    hourly_rate = float(input(f'Please enter your hourly rate, e.g. 11.44: '))
    num_hours_worked = float(input(f'Please enter your number of hours worked, e.g. 35.3: '))
    emp_pay = hourly_rate * num_hours_worked
    emp_pay = f'£ {emp_pay}'
    return emp_pay

def average_age(ages_list:list):

    sum_ages = sum(ages_list)
    num_ages = len(ages_list)
    avg_list = sum_ages / num_ages
    return avg_list

list_ages_1 = (29, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
avg_age = average_age(list_ages_1)
print(f'The average age is {avg_age} years')

emplye_pay = employee_pay()
print(f'Employee pay is {emplye_pay}')
