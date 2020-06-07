INSERT INTO clubs(name, creation_date, number_of_trophies)
(SELECT md5(random()::text),
        (CURRENT_DATE -(random() * (CURRENT_DATE -'01.01.1850'))::int),
        trunc(random() * 29 + 1) FROM generate_series(1, 300));


INSERT INTO players(first_name, last_name, date_of_birth, is_injured, height, position_id, club_id)
(SELECT md5(random()::text),
        md5(random()::text),
        ('01.01.2000'::date -(random() * ('01.01.2000'::date -'01.01.1975'::date))::int),
        random() > 0.5,
        trunc(random() * 39 + 160),
        trunc(random() * 3 + 1),
        (SELECT club_id FROM clubs ORDER BY random() LIMIT 1) FROM generate_series(1, 4000));


INSERT INTO tournaments(name, description)
    (SELECT md5(random()::text),
        md5(random()::text) FROM generate_series(1, 1000));