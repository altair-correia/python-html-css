DROP TABLE IF EXISTS entradas;

CREATE TABLE entradas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    título STRING NOT NULL,
    texto STRING not NULL
);