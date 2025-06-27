-- List all genre from hbtn_0d_tvshows and displays the number of show linked to each
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name HAVING COUNT(*)
ORDER BY number_of_shows DESC;