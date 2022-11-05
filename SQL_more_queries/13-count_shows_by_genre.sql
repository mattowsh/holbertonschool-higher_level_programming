-- Task 13:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. lists all genres from hbtn_0d_tvshows and displays the number of
-- shows linked to each

SELECT ge.name, COUNT(sh_ge.genre_id)
FROM tv_genres ge

INNER JOIN tv_show_genres sh_ge
ON ge.id = sh_ge.genre_id

ORDER BY COUNT(sh_ge.genre_id) DESC;
