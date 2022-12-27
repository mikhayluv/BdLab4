import random
import datetime
from dateutil.relativedelta import relativedelta


def random_date(start, end):  # возвращает случайную дату (datetime) между start и end
    delta = (end - start).days
    rng = random.randrange(1, delta)
    return start + datetime.timedelta(days=rng)


# Инсерты космических кораблей
def insert_spaceships():  # POINT (-180<X<180, -90<Y<90)
    string = "INSERT INTO s311289.Spaceship (spaceship_name, longitude, latitude ) VALUES "
    names = open("raw_data/spaceship_names", 'r', encoding="utf-8").read().splitlines()
    spaceship_id = []
    for i in range(1, len(names)):
        spaceship_id.append(i)
        substring = "('" + names[i] + "', '" + str(random.uniform(-179.999, 179.999)) + "', '" + str(
            random.uniform(-89.999, 89.999)) + "')"
        if i != len(names) - 1:
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
    for i in range(1, len(planet_names)):
        planet_id.append(i)
        # print(i)
        substring = "('" + planet_names[i] + "')"
        if i != len(planet_names) - 1:
            substring += ","
        string += substring
    string += ";"

    stream = open("inserts/planets.txt", "w")
    stream.write(string)
    return


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
    human_amount = 5000
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
# Удалить запятную в конце
def work_contract(worker_ids, human_ids):  # Капитана можно присвоить одному человеку, id которого я выберу сам
    string = "INSERT INTO s311289.Work_contract (human_id, job_post, start_date, end_date) VALUES "
    contract_duration = [1, 2, 3, 5]
    max_future_date = datetime.date(year=2030, month=12, day=12)
    today_date = datetime.date(year=2022, month=11, day=10)
    amount_of_contracts = 0
    spaceship_jobs = open("raw_data/spaceship_workers", "r", encoding="utf-8").read().splitlines()
    for i in worker_ids:
        temp_date = random_date(datetime.date(year=2010, month=1, day=1), datetime.date(year=2017, month=11, day=20))
        while temp_date <= today_date:  # пока контракт не продлен ЗА сегодняшнюю дату
            next_date = temp_date + relativedelta(years=random.choice(contract_duration))
            if next_date > max_future_date:
                temp_date = next_date
            else:
                substring = "(" + str(i) + ",'" + random.choice(spaceship_jobs) + "', '" + str(
                    temp_date) + "', '" + str(next_date) + "')"
                temp_date = next_date
                #ПОДУМАТЬ КАК УБРАТЬ ЗАПЯТУЮ
                if i != len(human_ids):
                    substring += ", "
                string += substring
                amount_of_contracts += 1
    string += ";"
    stream = open("inserts/workers.txt", 'w')
    stream.write(string)
    return amount_of_contracts


def locations():
    string = "INSERT INTO s311289.Location (location_name, spaceship_id) VALUES "
    location_names = open("raw_data/location_name", "r", encoding="utf-8").read().splitlines()
    location_with_spaceship_1 = []
    location_with_spaceship_2 = []
    location_with_spaceship_3 = []
    location_with_spaceship_4 = []
    location_with_spaceship_5 = []
    for i in range(len(location_names)):
        rnd_ship = random.randrange(1, 5)
        substirng = "('" + location_names[i] + "','" + str(rnd_ship) + "')"
        if rnd_ship == 1:
            location_with_spaceship_1.append(location_names[i])
        elif rnd_ship == 2:
            location_with_spaceship_2.append(location_names[i])
        elif rnd_ship == 3:
            location_with_spaceship_3.append(location_names[i])
        elif rnd_ship == 4:
            location_with_spaceship_4.append(location_names[i])
        else:
            location_with_spaceship_5.append(location_names[i])
        if i != len(location_names) - 1:
            substirng += ","
        string += substirng
    string += ";"
    stream = open("inserts/locations.txt", 'w')
    stream.write(string)
    return location_with_spaceship_1, location_with_spaceship_2, location_with_spaceship_3, location_with_spaceship_4, location_with_spaceship_5


#ТУТ ВЕЗДЕ ENUMERATE МОЖНО ЮЗАТЬ
def boarded_humans(humans_id):
    string = "INSERT INTO s311289.Human_on_spaceship (human_id , spaceship_id, boarded_date) VALUES "
    boarded_date_for_spaceship_1 = datetime.date(year=2020, month=10, day=25)
    boarded_date_for_spaceship_2 = datetime.date(year=2021, month=5, day=15)
    boarded_date_for_spaceship_3 = datetime.date(year=2020, month=6, day=19)
    boarded_date_for_spaceship_4 = datetime.date(year=2021, month=7, day=6)
    boarded_date_for_spaceship_5 = datetime.date(year=2021, month=3, day=1)
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

#ТУТ ВЕЗДЕ ENUMERATE МОЖНО ЮЗАТЬ
def human_location(person_on_ship_1, person_on_ship_2, person_on_ship_3, person_on_ship_4, person_on_ship_5, location_with_spaceship_1, location_with_spaceship_2, location_with_spaceship_3, location_with_spaceship_4, location_with_spaceship_5):
    string = "INSERT INTO s311289.Human_location (location_id, human_id) VALUES "
    for i in person_on_ship_1:
        substring = "('" + str(random.choice(location_with_spaceship_1)) + "', '" + str(person_on_ship_1) + "')"
        string += substring
    for i in person_on_ship_2:
        substring = "('" + str(random.choice(location_with_spaceship_2)) + "', '" + str(person_on_ship_2) + "')"
        string += substring
    for i in person_on_ship_3:
        substring = "('" + str(random.choice(location_with_spaceship_3)) + "', '" + str(person_on_ship_3) + "')"
        string += substring
    for i in person_on_ship_4:
        substring = "('" + str(random.choice(location_with_spaceship_4)) + "', '" + str(person_on_ship_4) + "')"
        string += substring
    for i in person_on_ship_5:
        substring = "('" + str(random.choice(location_with_spaceship_5)) + "', '" + str(person_on_ship_5) + "')"
        string += substring

def main():
    insert_spaceships()
    create_planets()
    eve_robots_ids, robots_id = robots()
    # print(eve_robots_ids)
    human_amount, worker_ids, human_ids = humans()
    print(f"Количество кожанных мешков: {human_amount}")
    print(f"Количество работников: {len(worker_ids)}")
    amount_of_contracts = work_contract(worker_ids, human_ids)
    print(f"Количество контрактов: {amount_of_contracts}")
    location_with_spaceship_1, location_with_spaceship_2, location_with_spaceship_3, location_with_spaceship_4, location_with_spaceship_5 = locations()
    boarded_humans(human_ids)
    # print(location_with_spaceship_1)


main()
