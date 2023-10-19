from application.salary import calculate_salary, plot_salary
from application.db.people import get_employees
from application.db.salary import month_salary
from datetime import date


if __name__ == '__main__':
    print(date.today(), calculate_salary())
    print(date.today(), get_employees())
    plot_salary(month_salary)

