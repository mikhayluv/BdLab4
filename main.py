import random
import datetime
from dateutil.relativedelta import relativedelta


def random_date(start, end):  # возвращает случайную дату (datetime) между start и end
    delta = (end - start).days
    rng = random.randrange(1, delta)
    return start + datetime.timedelta(days=rng)


# Инсерты космических кораблей
def spaceships():  # POINT (-180<X<180, -90<Y<90)
    string = "INSERT INTO s311289.Spaceship (spaceship_name, longitude, latitude ) VALUES "
    names = open("raw_data/spaceship_names", 'r', encoding="utf-8").read().splitlines()
    spaceship_id = []
    for i in range(len(names)):
        i += 1
        spaceship_id.append(i)
        substring = "('" + names[i - 1] + "', '" + str(random.uniform(-179.999, 179.999)) + "', '" + str(
            random.uniform(-89.999, 89.999)) + "')"
        if i != len(names):
            substring += ","
        string += substring
    string += ";"
    stream = open("inserts/spaceships.txt", 'w')
    stream.write(string)
    return spaceship_id


# Инсерты планет
def create_planets():
    string = "INSERT INTO s311289.Planet (planet_name) VALUES "
    planet_names = open("raw_data/planets_name", 'r', encoding="utf-8").read().splitlines()
    planet_id = []
    # print(len(planet_names))
    for i in range(len(planet_names)):
        i += 1
        planet_id.append(i)
        # print(i)
        substring = "('" + planet_names[i - 1] + "')"
        if i != len(planet_names):
            substring += ","
        string += substring
    string += ";"

    stream = open("inserts/planets.txt", "w")
    stream.write(string)
    return planet_id


# Инсерты роботов
def robots():
    string = "INSERT INTO s311289.Robots (model) VALUES "
    model_names = open("raw_data/Robot_models", 'r', encoding="utf-8").read().splitlines()
    eve_robots_ids = []
    robots_id = []
    for i in range(1, 15000):
        rnd_choose = random.choice(model_names)
        substring = "('" + rnd_choose + "')"
        if rnd_choose == "EVE":
            eve_robots_ids.append(i)
        else:
            robots_id.append(i)
        if i != 14999:
            substring += ","
        string += substring
    string += ";"

    stream = open("inserts/robot.txt", 'w')
    stream.write(string)
    return eve_robots_ids, robots_id


# Инсерты людей
def humans():
    string = "INSERT INTO s311289.Human (human_surname, human_name, age, is_working) VALUES "
    surname = open("raw_data/human_surname", 'r', encoding="utf-8").read().splitlines()
    name = open("raw_data/human_name", 'r', encoding="utf-8").read().splitlines()
    human_amount = 10000
    humans_id = []
    worker_ids = []
    for i in range(1, human_amount + 1):
        humans_id.append(i)
        age = random.randrange(4, 86)
        substring = "('" + random.choice(surname) + "', '" + random.choice(name) + "', '" + str(age) + "', '"
        if 18 <= age <= 65:
            subsubstring = "TRUE" + "')"
            worker_ids.append(i)
        else:
            subsubstring = "FALSE" + "')"
        if i != human_amount:
            subsubstring += ","
        string += substring
        string += subsubstring
    string += ";"
    stream = open("inserts/humans.txt", "w")
    stream.write(string)
    return human_amount, worker_ids, humans_id


# Инсерты рабочих контрактов
def work_contract(worker_ids, human_ids):  # Капитана можно присвоить одному человеку, id которого я выберу сам
    string = "INSERT INTO s311289.Work_contract (human_id, job_post, start_date, end_date) VALUES "
    contract_duration = [1, 2, 3, 5]
    max_future_date = datetime.date(year=2030, month=12, day=12)
    today_date = datetime.date(year=2022, month=11, day=10)
    amount_of_contracts = 0
    spaceship_jobs = open("raw_data/spaceship_workers", "r", encoding="utf-8").read().splitlines()
    active_contracts_id = []
    for index, value in enumerate(worker_ids):
        temp_date = random_date(datetime.date(year=2010, month=1, day=1), datetime.date(year=2017, month=11, day=20))
        while temp_date <= today_date:
            amount_of_contracts += 1
            # пока контракт не продлен ЗА сегодняшнюю дату
            next_date = temp_date + relativedelta(years=random.choice(contract_duration))
            # if next_date > max_future_date:
            #     temp_date = next_date
            # else:
            substring = "('" + str(value) + "', '" + random.choice(spaceship_jobs) + "', '" + str(
                temp_date) + "', '" + str(next_date) + "')"
            temp_date = next_date
            # ПОДУМАТЬ КАК УБРАТЬ ЗАПЯТУЮ - ВЫПОЛНЕНО!
            if index != len(worker_ids) - 1 or temp_date <= today_date:
                substring += ", "
            string += substring
            if temp_date > today_date:
                active_contracts_id.append(amount_of_contracts)
    string += ";"
    stream = open("inserts/workers.txt", 'w')
    stream.write(string)
    return amount_of_contracts, active_contracts_id


# Инсерты локаций с запоминанием на каком именно корабле какая локация
def locations():
    string = "INSERT INTO s311289.Location (location_name, spaceship_id) VALUES "
    location_names = open("raw_data/location_name", "r", encoding="utf-8").read().splitlines()
    location_with_spaceship_1 = []
    location_with_spaceship_2 = []
    location_with_spaceship_3 = []
    location_with_spaceship_4 = []
    location_with_spaceship_5 = []
    for i in range(len(location_names)):
        i += 1
        rnd_ship = random.randrange(1, 5)
        substirng = "('" + location_names[i - 1] + "','" + str(rnd_ship) + "')"
        if rnd_ship == 1:
            location_with_spaceship_1.append(i)
        elif rnd_ship == 2:
            location_with_spaceship_2.append(i)
        elif rnd_ship == 3:
            location_with_spaceship_3.append(i)
        elif rnd_ship == 4:
            location_with_spaceship_4.append(i)
        else:
            location_with_spaceship_5.append(i)
        if i != len(location_names):
            substirng += ","
        string += substirng
    string += ";"
    stream = open("inserts/locations.txt", 'w')
    stream.write(string)
    return location_with_spaceship_1, location_with_spaceship_2, location_with_spaceship_3, location_with_spaceship_4, location_with_spaceship_5


# ТУТ ВЕЗДЕ ENUMERATE МОЖНО ЮЗАТЬ
# Инсерты людей на корабль
def boarded_humans(humans_id):
    string = "INSERT INTO s311289.Human_on_spaceship (human_id , spaceship_id, boarded_date) VALUES "
    boarded_date_for_spaceship_1 = datetime.datetime(year=2020, month=10, day=random.randrange(20, 27),
                                                     hour=random.randrange(0, 23), minute=random.randrange(0, 60),
                                                     second=random.randrange(0, 60))
    boarded_date_for_spaceship_2 = datetime.datetime(year=2021, month=5, day=random.randrange(8, 15),
                                                     hour=random.randrange(0, 23), minute=random.randrange(0, 60),
                                                     second=random.randrange(0, 60))
    boarded_date_for_spaceship_3 = datetime.datetime(year=2020, month=6, day=random.randrange(12, 19),
                                                     hour=random.randrange(0, 23), minute=random.randrange(0, 60),
                                                     second=random.randrange(0, 60))
    boarded_date_for_spaceship_4 = datetime.datetime(year=2021, month=7, day=random.randrange(5, 12),
                                                     hour=random.randrange(0, 23), minute=random.randrange(0, 60),
                                                     second=random.randrange(0, 60))
    boarded_date_for_spaceship_5 = datetime.datetime(year=2021, month=3, day=random.randrange(1, 7),
                                                     hour=random.randrange(0, 23), minute=random.randrange(0, 60),
                                                     second=random.randrange(0, 60))
    person_on_ship_1 = []
    person_on_ship_2 = []
    person_on_ship_3 = []
    person_on_ship_4 = []
    person_on_ship_5 = []
    for i in humans_id:
        rnd_ship = random.randrange(1, 5)
        substring = "('" + str(i) + "', '"
        if rnd_ship == 1:
            subsubstring = str(1) + "', '" + str(boarded_date_for_spaceship_1) + "')"
            person_on_ship_1.append(i)
        elif rnd_ship == 2:
            subsubstring = str(2) + "', '" + str(boarded_date_for_spaceship_2) + "')"
            person_on_ship_2.append(i)
        elif rnd_ship == 3:
            subsubstring = str(3) + "', '" + str(boarded_date_for_spaceship_3) + "')"
            person_on_ship_3.append(i)
        elif rnd_ship == 4:
            subsubstring = str(4) + "', '" + str(boarded_date_for_spaceship_4) + "')"
            person_on_ship_4.append(i)
        else:
            subsubstring = str(5) + "', '" + str(boarded_date_for_spaceship_5) + "')"
            person_on_ship_5.append(i)
        if i != len(humans_id):
            subsubstring += ","
        substring += subsubstring
        string += substring
    string += ";"
    stream = open("inserts/boarded_humans.txt", 'w')
    stream.write(string)
    return person_on_ship_1, person_on_ship_2, person_on_ship_3, person_on_ship_4, person_on_ship_5


# ТУТ ВЕЗДЕ ENUMERATE МОЖНО ЮЗАТЬ
# Инсерты людей на локации в зависимости от того, на каком они корабле
def human_location(person_on_ship_1, person_on_ship_2, person_on_ship_3, person_on_ship_4, person_on_ship_5,
                   location_with_spaceship_1, location_with_spaceship_2, location_with_spaceship_3,
                   location_with_spaceship_4, location_with_spaceship_5):
    string = "INSERT INTO s311289.Human_location (location_id, human_id) VALUES "
    for index, value in enumerate(person_on_ship_1):
        substring = "('" + str(random.choice(location_with_spaceship_1)) + "', '" + str(value) + "')"
        if index != len(person_on_ship_1) - 1:
            substring += ","
        string += substring
    for index, value in enumerate(person_on_ship_2):
        substring = "('" + str(random.choice(location_with_spaceship_2)) + "', '" + str(value) + "')"
        if index != len(person_on_ship_2) - 1:
            substring += ","
        string += substring
    for index, value in enumerate(person_on_ship_3):
        substring = "('" + str(random.choice(location_with_spaceship_3)) + "', '" + str(value) + "')"
        if index != len(person_on_ship_3) - 1:
            substring += ","
    for index, value in enumerate(person_on_ship_4):
        substring = "('" + str(random.choice(location_with_spaceship_4)) + "', '" + str(value) + "')"
        if index != len(person_on_ship_4) - 1:
            substring += ","
        string += substring
    for index, value in enumerate(person_on_ship_5):
        substring = "('" + str(random.choice(location_with_spaceship_5)) + "', '" + str(value) + "')"
        if index != len(person_on_ship_5) - 1:
            substring += ","
        string += substring
    string += ";"
    stream = open("inserts/human_location.txt", 'w')
    stream.write(string)


# Инсерты работников с активными контрактами.
# Данная таблица подразумевает тригерную функцию или процедуру хз
def employee(active_contracts_id):
    employee_id = []
    string = "INSERT INTO s311289.Employee (work_contract_id) VALUES "
    for index, value in enumerate(active_contracts_id):
        employee_id.append(index + 1)
        substring = "('" + str(value) + "')"
        if index != len(active_contracts_id) - 1:
            substring += ","
        string += substring
    string += ";"
    stream = open("inserts/employee.txt", "w")
    stream.write(string)
    return employee_id


def main():
    spaceship_id = spaceships()
    print(f"Id планет кораблей {spaceship_id}")
    planet_id = create_planets()
    print(f"Id планет {planet_id}")
    eve_robots_ids, robots_id = robots()
    print(f"Id ЕВА {eve_robots_ids}")
    print(f"Id роботов {robots_id}")
    human_amount, worker_ids, human_ids = humans()
    print(f"Все людей: {human_amount}")
    print(f"ID людей: {human_ids}")
    print(f"Количество работников: {len(worker_ids)}")
    amount_of_contracts, active_contracts_id = work_contract(worker_ids, human_ids)
    print(f"Количество контрактов: {amount_of_contracts}")
    print(f"Id активных контрактов: {active_contracts_id}")
    location_with_spaceship_1, location_with_spaceship_2, location_with_spaceship_3, location_with_spaceship_4, location_with_spaceship_5 = locations()
    print(f"Локи на 1 корбале {location_with_spaceship_1}")
    person_on_ship_1, person_on_ship_2, person_on_ship_3, person_on_ship_4, person_on_ship_5 = boarded_humans(human_ids)
    print(person_on_ship_1)
    print(location_with_spaceship_1)
    human_location(person_on_ship_1, person_on_ship_2, person_on_ship_3, person_on_ship_4, person_on_ship_5,
                   location_with_spaceship_1, location_with_spaceship_2, location_with_spaceship_3,
                   location_with_spaceship_4, location_with_spaceship_5)
    employee_id = employee(active_contracts_id)
    print(f"ID работника {employee_id}")


main()
