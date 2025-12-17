CREATE TABLE artist(
    artist_id INT,
    name VARCHAR(255) NOT NULL,
    country VARCHAR,
    PRIMARY KEY(artist_id)
);

CREATE TABLE album(
    album_id INT,
    title VARCHAR(255),
    artist_id INT,
    release_year INT,
    PRIMARY KEY(album_id),
    CONSTRAINT fk_artist
        FOREIGN KEY(artist_id)
        REFERENCES artist(artist_id)
        ON DELETE CASCADE
);

CREATE TABLE customer(
    customer_id INT,
    name VARCHAR(255),
    email VARCHAR UNIQUE,
    PRIMARY KEY(customer_id)
);

CREATE TABLE purchase(
    purchase_id INT,
    purchase_date VARCHAR,
    customer_id INT,
    album_id INT,
    PRIMARY KEY(purchase_id),
    CONSTRAINT fk_customer
        FOREIGN KEY(customer_id)
        REFERENCES customer(customer_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_album
        FOREIGN KEY(album_id)
        REFERENCES album(album_id)
        ON DELETE CASCADE
);

INSERT INTO artist (artist_id, name, country) VALUES
    (1, 'Alireza Eftekhari', 'Iran'),
    (2, 'Shahram Nazeri', 'Iran'),
    (3, 'Homayon Shajarian', 'Iran');

INSERT INTO album (album_id, title, artist_id, release_year) VALUES
    (1, 'Niloofaraneh', 1, 1996),
    (2, 'Sayad', 1, 2005),
    (3, 'Gol-e Sad Barg', 2, 1984),
    (4, 'Beshno az Ney', 2, 1995),
    (5, 'Nasim-e Vasl', 3, 2003),
    (6, 'Shoghe Doost', 3, 2004);

INSERT INTO customer (customer_id, name, email) VALUES
    (1, 'maryam', 'a@b.com'),
    (2, 'javad', 'c@d.com');

INSERT INTO purchase (purchase_id, customer_id, album_id, purchase_date) VALUES
    (1, 1, 1, '2025-02-06'),
    (2, 1, 2, '2024-09-12'),
    (3, 1, 3, '2022-10-10'),
    (4, 1, 4, '2020-11-11'),
    (5, 1, 5, '2021-12-12'),
    (6, 2, 6, '2023-09-09'),
    (7, 2, 2, '2024-09-09'),
    (8, 2, 3, '2021-09-09'),
    (9, 2, 5, '2025-09-09'),
    (10, 2, 1, '2013-09-09');