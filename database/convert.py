import csv

def create_NOC_csv():
    ''' creates a new noc.csv by removing the header and adding a NOC_ID field '''

    reader = csv.reader(open('noc_regions.csv'))
    writer = csv.writer(open('noc.csv','w'))
    next(reader)

    NOC_dict = {}
    NOC_ID = 1
    for NOC_row in reader:
        NOC = NOC_row[0]
        NOC_dict[NOC] = NOC_ID
        NOC_ID += 1

        ID_row = NOC_row.insert(0, NOC_ID)
        writer.writerow(ID_row)

    reader.close()
    writer.close()

    return NOC_dict
  
def create_athletes_csv():
    class Athlete():
        def __init__(self, athlete_id, name, sex, height, weight):
            self.athlete_id = athlete_id
            self.name = name
            self.sex = sex
            self.height = height
            self.weight = weight

    athletes = {}

    # read from csv and only store name, sex, height, weight
    reader = csv.reader(open('athlete_events.csv'))
    next(reader)
    for row in reader:
        athlete_id = row[0]
        name = row[1]
        sex = row[2]
        height = row[4]
        weight = row[5]
        if athlete_id not in athletes:
            athlete = Athlete(athlete_id, name, sex, height, weight)
            athletes[athlete_id] = athlete

    # write into new csv
    writer = csv.writer(open('athletes_info.csv','w'))
    for athlete_id in athletes:
        athlete = athletes[athlete_id]
        row = [athlete.name, athlete.sex, athlete.height, athlete.weight]
        writer.writerow(row) 

    reader.close()
    writer.close()


def create_competitions_csv():
    competitions = {}

    # read from csv and only store name, sex, height, weight
    reader = csv.reader(open('athlete_events.csv'))
    next(reader)
    game_ID = 1
    for row in reader:
        game = row[8]
        year = row[9]
        season = row[10]
        city = row[11]
        if game not in competitions:
            competitions[game] = [year, season, city, game_ID]
            game_ID += 1

    # write into new csv
    writer = csv.writer(open('competitions_info.csv','w'))
    for game in competitions.values():
        writer.writerow(game) 

    reader.close()
    writer.close()
