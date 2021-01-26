import csv

def create_NOC_csv():
    ''' creates noc.csv by adding a NOC_ID field '''

    reader = csv.reader(open('noc_regions.csv'))
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

    return NOC_dict
  
def create_athletes_csv():
    ''' creates athletes_info.csv that stores an athlete's id, name, sex, height, weight '''
    athletes = {}

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

    with open('athletes_info.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for athlete in athletes.values():
            writer.writerow(athlete) 

def create_competitions_csv():
    ''' creates competitions_info.csv that stores a game's id, year, season, city'''
    competitions = {}

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

    with open('competitions_info.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for game in competitions.values():
            writer.writerow(game) 

    return competitions

def create_athletes_NOC_age_competitions_csv(NOC_dict, competition):
    ''' creates csv that links athlete id to their age, game, and NOC'''
	
    with open('athletes_NOC_age_competitions.csv', 'w', newline='') as csvfile: 
        writer = csv.writer(csvfile)
        reader = csv.reader(open('athlete_events.csv'))
        next(reader)
        for row in reader:
            athlete_id = row[0]
            age = row[3]
            game = row[8]
            NOC = row[7]
            competition_id = competition[game][0]
            
            # hard coded to fix crashing
            if NOC == "SGP":
                NOC = "SIN"

            NOC_id = NOC_dict[NOC]
            writer.writerow([athlete_id, NOC_id, age, competition_id])
	
def create_events_csv(competitions):
    ''' 
        creates athletes_events.csv that links athlete id to event id
        creates events.csv that stores event_id, competition_id, sport, event, and the athlete_id of the gold, silver, and bronze winners
    '''
    events = []
	
    class Event():
		def __init__(self, sport, event, competition_id, event_id):
			self.sport = sport
			self.event = event
			self.competition_id = competition_id
			self.event_id = event_id
			self.gold = None
			self.silver = None
			self.bronze = None
		
		def set_gold_id(self, athlete_id):
			self.gold = athlete_id
		def set_silver_id(self, athlete_id):
			self.silver = athlete_id
		def set_bronze_id(self, athlete_id):
			self.bronze = athlete_id
	
		def __eq__(self, other):
			return self.competition_id == other.competition_id and self.event == other.event
			
	with open('athletes_events.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		reader = csv.reader(open('athlete_events.csv'))
		next(reader)
		event_id = 1
		for row in reader:
			athlete_id = row[0]
			game = row[8]
			sport = row[12]
			event_name = row[13]
			medal = row[14]
			competition_id = competitions[game][0]
			event = Event(sport, event_name, competition_id, event_id)
    
            # checking for duplicates
			event_exists = False
			for ev in events:
				if ev == event:
					event = ev
					event_exists = True
					break

			if medal.lower() == 'gold':
				event.set_gold_id(athlete_id)
			elif medal.lower() == 'silver':
				event.set_silver_id(athlete_id)
			elif medal.lower() == 'bronze':
				event.set_bronze_id(athlete_id)
            
			if not event_exists:
				events.append(event)
				event_id += 1

			writer.writerow([athlete_id, event.event_id])

	with open('events.csv', 'w', newline='') as csvfile: 
		writer = csv.writer(csvfile)
		for event in events:
			writer.writerow([event.event_id, event.competition_id, event.sport, event.event, event.gold, event.silver, event.bronze])

def main():
    NOC = create_NOC_csv()
    create_athletes_csv()
    competitions = create_competitions_csv()
    create_athletes_NOC_age_competitions_csv(NOC, competitions)
    create_events_csv(competitions)
    
main()
