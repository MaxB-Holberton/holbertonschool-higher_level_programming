-- show all the tv shows and their genres
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres on tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_gernmes ON tv_show_genres.genres_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
