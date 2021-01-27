SELECT countries.noc
FROM countries
ORDER BY countries.noc;

SELECT DISTINCT athletes.name, countries.noc
FROM athletes, athletes_countries_age_competitions, countries
WHERE countries.noc = 'KEN'
AND athletes.id = athletes_countries_age_competitions.athletes_id
AND athletes_countries_age_competitions.noc_id = countries.id;

SELECT events.event, competitions.year
FROM events, athletes, competitions
WHERE events.gold = athletes.id
AND athletes.name = 'Gregory Efthimios "Greg" Louganis'
AND competitions.id = events.competitions_id
ORDER BY competitions.year;

SELECT COUNT(events.gold), countries.noc
FROM events, countries, athletes, athletes_countries_age_competitions
WHERE events.gold = athletes.id
AND athletes.id = athletes_countries_age_competitions.athletes_id
AND athletes_countries_age_competitions.competitions_id = events.competitions_id
GROUP BY countries.noc
ORDER BY COUNT(events.gold) DESC;
