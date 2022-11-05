-- Task 14:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT ge.name AS name
FROM 
    tv_genres ge INNER JOIN tv_show_genres sh_ge
ON 
    ge.id = sh_ge.genre_id INNER JOIN tv_shows sh
ON
    sh.id = sh_ge.show_id
WHERE
    sh.title = "Dexter"
ORDER BY
    ge.name ASC;