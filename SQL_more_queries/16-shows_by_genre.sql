-- Task 16:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. lists all shows, and all genres linked to that show, from the
-- database hbtn_0d_tvshows

SELECT sh.title, ge.name
FROM
    tv_shows sh LEFT JOIN tv_show_genres sh_ge
ON
    sh.id = sh_ge.show_id LEFT JOIN tv_genres ge
ON
    ge.id = sh_ge.genre_id
ORDER BY
    sh.title, ge.name