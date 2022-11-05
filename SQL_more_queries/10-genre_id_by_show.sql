-- Task 10:
-- 1. import the database dump from hbtn_0d_tvshows to your MySQL server
-- 2. lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;