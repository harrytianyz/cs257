import csv

def create_NOC_csv():
    ''' creates a new noc.csv by removing the header and adding a NOC_ID field '''

    reader = csv.reader(open('noc_regions.csv'))
    # writer = csv.writer(open('noc.csv','w'))
    next(reader)

    NOC_dict = {}
    NOC_ID = 1

    with open('noc.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for NOC_row in reader:
            NOC = NOC_row[0]
            NOC_dict[NOC] = NOC_ID

            NOC_row.insert(0, NOC_ID)
            writer.writerow(NOC_row)

            NOC_ID += 1
    # reader.close()
    # writer.close()

    return NOC_dict
  
def create_athletes_csv():
    athletes = {}

    # read from csv and only store name, sex, height, weight
    reader = csv.reader(open('athlete_events.csv'))
    next(reader)
    for row in reader:
        athlete_id = int(row[0])
        name = row[1]
        sex = row[2]
        height = row[4]
        if height != "NA":
            height = int(height)
        weight = row[5]
        if weight != "NA":
            weight = float(weight)
        if athlete_id not in athletes:
            athletes[athlete_id] = [athlete_id, name, sex, height, weight]

    # write into new csv
    
    # writer = csv.writer(open('athletes_info.csv','w'))
    with open('athletes_info.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for athlete in athletes.values():
            writer.writerow(athlete) 

    # reader.close()
    # writer.close()


def create_competitions_csv():
    competitions = {}

    # read from csv and only store name, sex, height, weight
    reader = csv.reader(open('athlete_events.csv'))
    next(reader)
    game_ID = 1
    for row in reader:
        game = row[8]
        year = int(row[9])
        season = row[10]
        city = row[11]
        if game not in competitions:
            competitions[game] = [game_ID, year, season, city]
            game_ID += 1

    # write into new csv
    # writer = csv.writer(open('competitions_info.csv','w'))
    with open('competitions_info.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for game in competitions.values():
            writer.writerow(game) 

    # reader.close()
    # writer.close()

def create_athletes_NOC_age_competitions(NOC_dict, competitions):
	
	with open('athletes_NOC_age_competitions.csv', 'w', newline='') as csvfile: 
		writer = csv.writer(csvfile)
		reader = csv.reader(open('athlete_events.csv'))
		next(reader)
		for row in reader:
			age = row[3]
			athlete_id = row[0]
			game = row[8]
			NOC = row[7]
			competition_id = competitions[game][0]
			NOC_id = NOC_dict[NOC]
			writer.writerow([athlete_id, NOC_id, age, competition_id])
	
def create_events():
	class Event(sport, event, competitions):
		
	
	reader = csv.reader(open('athlete_events.csv'))

def main():
    create_NOC_csv()
    create_athletes_csv()
    create_competitions_csv()

main()
