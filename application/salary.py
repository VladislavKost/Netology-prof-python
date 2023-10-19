import matplotlib.pyplot as plt


def calculate_salary():
    return 'Считаю зарплату сотрудника'

def plot_salary(month_salary):
    months = []
    values = []
    for month, value in month_salary.items():
        months.append(month)
        values.append(value)
    plt.plot(months, values)
    plt.xlabel('Месяц')
    plt.ylabel('Зарплата')
    plt.savefig('salary_plot.png')
    print('Рисунок с графиком сохранен')
