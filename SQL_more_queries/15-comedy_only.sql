-- Task 15:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. lists all Comedy shows in the database hbtn_0d_tvshows

SELECT sh.title AS title
FROM
    tv_shows sh INNER JOIN tv_show_genres sh_ge
ON
    sh.id = sh_ge.show_id INNER JOIN tv_genres ge
ON
    ge.id = sh_ge.genre_id
WHERE
    ge.name = "Comedy"
ORDER BY
    sh.title ASC;