CREATE TABLE client_data (
    client_id INTEGER PRIMARY KEY,
    age INTEGER,
    job TEXT,
    marital TEXT,
    education TEXT,
    default BOOLEAN,
    housing BOOLEAN,
    loan BOOLEAN
);

CREATE TABLE campaign_data (
    client_id INTEGER REFERENCES client_data(client_id),
    contact TEXT,
    month TEXT,
    day INTEGER,
    campaign INTEGER,
    pdays INTEGER,
    previous INTEGER,
    poutcome TEXT
);

CREATE TABLE loan_outcomes (
    client_id INTEGER REFERENCES client_data(client_id),
    subscribed BOOLEAN
);
