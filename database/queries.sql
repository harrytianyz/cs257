'''List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. 
These entities, by the way, are mostly equivalent to countries. 
But in some cases, you might find that a portion of a country participated in a particular games 
(e.g. one guy from Newfoundland in 1904) or some other oddball situation.
'''
SELECT countries.noc
FROM countries
ORDER BY countries.noc;

'''List the names of all the athletes from Kenya. 
If your database design allows it, sort the athletes by last name.
'''
SELECT DISTINCT athletes.name, countries.noc
FROM athletes, athletes_countries_age_competitions, countries
WHERE countries.noc = 'KEN'
AND athletes.id = athletes_countries_age_competitions.athletes_id
AND athletes_countries_age_competitions.noc_id = countries.id;

'''List all the medals won by Greg Louganis, sorted by year. 
Include whatever fields in this output that you think appropriate.
'''

SELECT events.event, competitions.year
FROM events, athletes, competitions
WHERE events.gold = athletes.id
AND athletes.name = 'Gregory Efthimios "Greg" Louganis'
AND competitions.id = events.competitions_id
ORDER BY competitions.year;

'''List all the NOCs and the number of gold medals they have won, 
in decreasing order of the number of gold medals.
'''

SELECT COUNT(DISTINCT events.id), countries.noc
FROM events, countries, athletes_countries_age_competitions
WHERE events.gold = athletes_countries_age_competitions.athletes_id
AND events.competitions_id = athletes_countries_age_competitions.competitions_id
AND athletes_countries_age_competitions.noc_id = countries.id
GROUP BY countries.noc
ORDER BY COUNT(DISTINCT events.id) DESC;

