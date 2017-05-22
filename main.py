import movie;
import fresh_tomatoes;

# Common dataset for all the movies.
# New movies to be added here.
movie_data = [
    {
        'title': 'Inception',
        'trailer_youtube_url': 'https://www.youtube.com/watch?v=YoHD9XEInc0',
        'poster_image_url': 'https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/inception_keyart.jpg?itok=7jXiglyb'
    },
    {
        'title': 'The Big Short',
        'trailer_youtube_url': 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&cad=rja&uact=8&ved=0ahUKEwiEkOualILUAhUq5oMKHZyHBi8QtwIITjAF&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DvgqG3ITMv1Q&usg=AFQjCNGjZjIMjNljnk-cPgmvxFKhomubfQ',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg'
    },
    {
        'title': 'Fury',
        'trailer_youtube_url': 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=6&cad=rja&uact=8&ved=0ahUKEwiUnoXflILUAhVKtJQKHQjUBLkQtwIITzAF&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D-OGvZoIrXpg&usg=AFQjCNH1deZpYZdN15m7PZAfuewUu4bLFQ',
        'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4MDU0NTUyN15BMl5BanBnXkFtZTgwMzQxMzY4MjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg'
    }
];

movies = [];

# Iterate through the dataset
for item in movie_data:
    movie_obj = movie.Movie(item['title'], item['trailer_youtube_url'], item['poster_image_url']);
    movies.append(movie_obj);

fresh_tomatoes.create_movie_tiles_content(movies);
fresh_tomatoes.open_movies_page(movies);
