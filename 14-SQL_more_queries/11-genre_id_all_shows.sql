-- Task 11:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. lists all shows contained in the database hbtn_0d_tvshows

SELECT sh.title, genre.genre_id
FROM tv_shows sh
-- In this case we want return all elements of the A table (sh), no matter
-- if has or not a value in the B table (genre):
LEFT JOIN tv_show_genres genre
ON sh.id = genre.show_id
ORDER BY sh.title, genre.genre_id ASC;