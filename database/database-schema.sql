CREATE TABLE countries (
    id integer,
    noc text,
    region text,
    notes text
);

CREATE TABLE athletes (
    id integer,
    name text,
    sex text,
    height integer,
    weight decimal
);

CREATE TABLE competitions (
    id integer,
    year integer,
    season text,
    city text
);

CREATE TABLE athletes_countries_age_competitions (
    athletes_id integer,
    noc_id integer,
    age integer,
    competitions_id integer
);

CREATE TABLE events (
    id integer,
    competitions_id integer,
    sport text,
    event text,
    gold integer,
    silver integer,
    bronze integer
);

CREATE TABLE athletes_events (
	athletes_id integer,
	events_id integer
);

