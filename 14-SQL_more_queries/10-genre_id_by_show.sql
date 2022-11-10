-- Task 10:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked

SELECT sh.title, genres.genre_id
FROM tv_shows sh
-- We want compare two columns of different tables, and return the intersection
-- thus, we want return only the records when these values are the same:
INNER JOIN tv_show_genres genres
ON sh.id = genres.show_id
ORDER BY sh.title, genres.genre_id ASC;