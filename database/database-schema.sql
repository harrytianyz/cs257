CREATE TABLE NOC (
    id SERIAL,
    NOC text,
    region text,
    notes text,
);

CREATE TABLE athletes (
    id SERIAL,
    name text,
    sex text,
    height integer,
    weight integer,
    team text,
    (sports?)
);

CREATE TABLE athletes_NOC_age_competitions (
    athletes_id integer,
    NOC_id integer,
    age integer,
    competitions_id integer,
);

CREATE TABLE competitions (
    id SERIAL,
    year integer,
    season text,
    city text,
);

CREATE TABLE events (
    id SERIAL,
    competitions_id integer,
    sport text,
    event text,
    gold integer,
    silver integer,
    bronze integer,
);

