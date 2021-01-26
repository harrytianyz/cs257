CREATE TABLE NOC (
    id integer,
    NOC text,
    region text,
    notes text,
);

CREATE TABLE athletes (
    id integer,
    name text,
    sex text,
    height integer,
    weight integer,
);

CREATE TABLE competitions (
    id integer,
    year integer,
    season text,
    city text,
);

CREATE TABLE athletes_NOC_age_competitions (
    athletes_id integer,
    NOC_id integer,
    age integer,
    competitions_id integer,
);

CREATE TABLE events (
    id integer,
    competitions_id integer,
    sport text,
    event text,
    gold integer,
    silver integer,
    bronze integer,
);

CREATE TABLE athletes_events (
	athletes_id integer,
	events_id integer
);

