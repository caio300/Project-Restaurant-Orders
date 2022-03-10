import csv


def reader_csv(path):
    dataFile = []
    with open(path) as file:
        my_csv = csv.reader(file, delimiter=",")
        for row in my_csv:
            dataFile.append(row)
    return dataFile


def write_file(str):
    with open("data/mkt_campaign.txt", mode="w") as file:
        file.writelines(str)


def favorite_order(file, customer):
    meals = {}
    for order in file:
        if customer in order:
            if order[1] not in meals:
                meals[order[1]] = 1
            else:
                meals[order[1]] += 1
    return max(meals, key=meals.get)


def quantity_order(file, customer, item):
    meals = {}
    for order in file:
        if customer in order:
            if order[1] not in meals:
                meals[order[1]] = 1
            else:
                meals[order[1]] += 1
    if item in meals:
        return meals[item]
    return 0


def never_ordered(file, customer):
    meals = set()
    customerOrdered = set()
    for order in file:
        meals.add(order[1])
        if customer in order:
            customerOrdered.add(order[1])

    return meals.difference(customerOrdered)


def days_never_visited(file, customer):
    week = set()
    customerVisited = set()
    for order in file:
        week.add(order[2])
        if customer in order:
            customerVisited.add(order[2])
    return week.difference(customerVisited)


def analyze_log(path_to_file):
    dataFile = []
    dataFile = reader_csv(path_to_file)

    string = "{0}\n{1}\n{2}\n{3}".format(
        favorite_order(dataFile, "maria"),
        quantity_order(dataFile, "arnaldo", "hamburguer"),
        never_ordered(dataFile, "joao"),
        days_never_visited(dataFile, "joao"),
    )

    write_file(string)
