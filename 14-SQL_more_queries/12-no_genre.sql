-- Task 12:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. lists all shows contained in hbtn_0d_tvshows without a genre linked

SELECT sh.title, genres.genre_id
FROM tv_shows sh
-- We want the records with NULL genre_id:
LEFT JOIN tv_show_genres genres
ON sh.id = genres.show_id
WHERE
    genres.show_id IS NULL
ORDER BY sh.title, genres.genre_id ASC;