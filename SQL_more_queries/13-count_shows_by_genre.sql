-- Task 13:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. lists all genres from hbtn_0d_tvshows and displays the number of
-- shows linked to each

SELECT genres.name, COUNT(sh_genres.genre_id)
FROM tv_genres genres

INNER JOIN tv_show_genres sh_genres
ON genres.id = sh_genres.genre_id

ORDER BY COUNT(sh_genres.genre_id) DESC;
