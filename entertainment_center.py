import fresh_tomatoes
import media

toy_store = media.Movie("Toy Story", "A story of a boy that comes to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A story of blue man in your imaginnary world", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hitch = media.Movie("Hitch", "A story of a man who has a job that learn other people to conquerer the heart of a drean woman", "https://www.movieposter.com/posters/archive/main/96/MPW-48388", "https://www.youtube.com/watch?v=dMaq_pfxs-0")

_toy_store = media.Movie("Toy Story", "A story of a boy that comes to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

_avatar = media.Movie("Avatar", "A story of blue man in your imaginnary world", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

_hitch = media.Movie("Hitch", "A story of a man who has a job that learn other people to conquerer the heart of a drean woman", "https://www.movieposter.com/posters/archive/main/96/MPW-48388", "https://www.youtube.com/watch?v=dMaq_pfxs-0")

# print(toy_store.storyline)

# print(avatar.storyline)

# print(hitch.storyline)

# hitch.show_trailer()

movies = [toy_store, avatar, hitch, _toy_store, _avatar, _hitch]

# fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)