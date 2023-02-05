import datetime


months = [1,2,3,4,5,6,7,8,9,10]
month_labels = [
    # Generate a list of tuples (x_value, x_label)
    (m, datetime.date(2020, m, 1).strftime('%B'))
    for m in months
        ]
print(month_labels)