import math


def determine_orders(order):
    log_order = round(math.log(order, 10), 2)

    root_log_order = int(log_order // 2)

    return (log_order, root_log_order) 


def  determine_time_measures(order):
    seconds = order - 9

    minutes = round(math.log(10**seconds / 60, 10), 2)
    hours = round(math.log(10**minutes / 60, 10), 2)
    days = round(math.log(10**hours / 24, 10), 2)
    years = round(math.log(10**days / 365, 10), 2)

    return (int(seconds), minutes, hours, days, years, int(years))