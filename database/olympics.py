# Harry Tian
#!/usr/bin/env python3
'''
    olympics.py
    Harry Tian

    This program connects to and queries the olympics database, 
    which can be set up by:
        psql -U MY_POSTGRES_USER_NAME olympics < olympics.sql

    This code is based on Jeff's psycopg2-sample.py
'''
import psycopg2
import argparse
import sys

def gold_all_NOC(database, user, password, limit):
    '''
    List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.
    '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    query = 'SELECT COUNT(DISTINCT events.id), countries.noc FROM events, countries, athletes_countries_age_competitions WHERE events.gold = athletes_countries_age_competitions.athletes_id AND events.competitions_id = athletes_countries_age_competitions.competitions_id AND athletes_countries_age_competitions.noc_id = countries.id GROUP BY countries.noc ORDER BY COUNT(DISTINCT events.id)  DESC LIMIT {0};'.format(limit)
    try:
        cursor = connection.cursor()
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    print('===== All  NOCs and their number of gold medals=====')
    for row in cursor:
        print(row[0], row[1])
    print()

    connection.close()

def search_athletes_from_NOC(database, user, password, search_string):
    '''
    List the names of all the athletes from a specified NOC.
    '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    query = 'SELECT DISTINCT athletes.name FROM athletes, athletes_countries_age_competitions, countries WHERE countries.noc = \'' + search_string + '\' AND athletes.id = athletes_countries_age_competitions.athletes_id AND athletes_countries_age_competitions.noc_id = countries.id;'
    try:
        cursor = connection.cursor()
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    print('===== All athletes from {0}====='.format(search_string))
    for row in cursor:
        print(row[0])
    print()

    connection.close()

def search_gold_athlete(database, user, password, search_string):
    '''
    List all the gold medals won by a specified athelete
    '''
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    query = 'SELECT events.event, competitions.year FROM events, athletes, competitions WHERE events.gold = athletes.id AND athletes.name = %s AND competitions.id = events.competitions_id ORDER BY competitions.year;'
    try:
        cursor = connection.cursor()
        cursor.execute(query, (search_string,))
    except Exception as e:
        print(e)
        exit()

    print('===== Gold Medals won by {0}====='.format(search_string))
    for row in cursor:
        print(row[0], row[1])
    print()

    connection.close()

def get_parsed_arguments():
    """
    Returns arguments from argparser. 
    """
    parser = argparse.ArgumentParser(description='Makes queries to olympics.sql database')
    
    parser.add_argument('-n', '--NOC',
                        type = int,
                        metavar='LIMIT',
                        help='List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals. You may limit the number of NOCs to be displayed',
                        default=1000000)
    
    parser.add_argument('-a', '--athletes', 
                        metavar='NOC', 
                        help='List the names of all the athletes from a specified NOC.')
    
    parser.add_argument('-g', '--gold', 
                        metavar='athlete', 
                        help='List all the gold medals won by a specified athelete. Enter the full name of the athlete in quotations.')
    
    parsed_arguments = parser.parse_args()

    return parsed_arguments

def main():
    args = get_parsed_arguments()

    try:
        from config import user
        from config import password
    except Exception as e:
        print("Missing config file. In this directory, create config.py:\n  user = <yourusername> \n    password = <yourdatabasepassword>")
        exit()
    database = 'olympics'

    # the default operation is to list all the NOCs and the number of gold medals they have won
    if args.athletes:
        print(args.athletes)
        search_athletes_from_NOC(database, user, password, args.athletes)
    elif args.gold:
        search_gold_athlete(database, user, password, args.gold)
    else:
        gold_all_NOC(database, user, password, args.NOC)

if __name__ == '__main__':
    main()
