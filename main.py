import random
import datetime
from dateutil.relativedelta import relativedelta

def random_date(start, end):  # возвращает случайную дату (datetime) между start и end
    delta = (end - start).days
    rng = random.randrange(1, delta)
    return start + datetime.timedelta(days=rng)


def insert_spaceships():  # POINT (-180<X<180, -90<Y<90)
    string = "INSERT INTO s311289.Spaceship (spaceship_name, longitude, latitude ) VALUES "
    names = open("raw_data/spaceship_names", 'r', encoding="utf-8").read().splitlines()
    for i in range(len(names)):
        substring = "('" + names[i] + "', '" + str(random.uniform(-179.999, 179.999))+ "', '" + str(random.uniform(-89.999, 89.999)) + "')"
        if i != len(names) - 1:
            substring += ","
        string += substring
    string += ";"
    stream = open("inserts/spaceships.txt", 'w')
    stream.write(string)
    return

def create_planets():
    string = "INSERT INTO s311289.Planet (planet_name) VALUES "
    planet_names = open("raw_data/planets_name", 'r', encoding="utf-8").read().splitlines()
    # print(len(planet_names))
    for i in range(len(planet_names)):
        # print(i)
        substring = "('" + planet_names[i] + "')"
        if i != len(planet_names) - 1:
            substring += ","
        string += substring
    string += ";"

    stream = open("inserts/planets.txt", "w")
    stream.write(string)
    return

#Добавить массив для запоминания ЕВЫ
def robots():
    string = "INSERT INTO s311289.Robots (model) VALUES "
    model_names = open("raw_data/Robot_models", 'r', encoding="utf-8").read().splitlines()
    for i in range(15000):
        substring = "('" + random.choice(model_names) + "')"
        if i != 14999:
            substring += ","
        string += substring
    string += ";"

    stream = open("inserts/robot.txt", 'w')
    stream.write(string)
    return

def humans():
    string = "INSERT INTO s311289.Human (human_surname, human_name, age, is_working) VALUES "
    surname = open("raw_data/human_surname", 'r', encoding="utf-8").read().splitlines()
    name = open("raw_data/human_name", 'r', encoding="utf-8").read().splitlines()
    human_amount = random.randrange(10000, 12500)
    worker_ids = []
    for i in range(1, human_amount + 1):
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
    return human_amount, worker_ids

def work_contract(worker_ids): #Капитана можно присвоить одному человеку, id которого я выберу сам
    string = "INSERT INTO s311289.Work_contract (human_id, job_post, start_date, end_date) VALUES "
    #Дописать контракты 1,3,5 лет
    start_date = []
    end_date = []
    spaceship_workers = worker_ids[:4000]
    default_workers = worker_ids[4000:]
    spaceship_jobs = open("raw_data/spaceship_workers", "r", encoding="utf-8").read().splitlines()
    default_jobs = open("raw_data/human_job_not_space", "r", encoding="utf-8").read().splitlines()
    for id in spaceship_workers:
        substring = "(" + str(id) + ",'" + random.choice(spaceship_jobs)






def main():
    # insert_spaceships()
    # create_planets()
    # robots()
    human_amount, worker_ids = humans()
    print(f"Количество кожанных мешков {human_amount}")
    print(len(worker_ids))


main()
