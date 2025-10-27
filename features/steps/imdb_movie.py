from behave import given, when, then
from selenium import webdriver

from pages.imdb_home_page import ImdbHomePage
from pages.imdb_movie_page import ImdbMoviePage
from pages.imdb_results_page import ImdbResultPage
from pages.lastfm_home_page import LastFmHomePage
from pages.lastfm_results_page import LastFmResultPage
from pages.lastfm_artist_page import LastFmArtistPage

@given("el usuario esta en el home page de imdb")
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com")
    context.imdb_home = ImdbHomePage(context.driver)

@when('busca la pelicula "{movie_name}"')
def step_search_movie(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_results = ImdbResultPage(context.driver)

@when("selecciona el resultado inception")
def step_search_result(context):
    context.imdb_results.click_movie_link()
    context.imdb_movie = ImdbMoviePage(context.driver)


@then('el titulo de la pelicula dede ser "{movie_name}"')
def step_get_movie_name(context, movie_name):
    object_data = context.imdb_movie.get_movie_title()
    assert object_data == movie_name, f"El nombre no coincide con Inception"

@then('el rating de la pelicula debe ser "{movie_rating}"')
def step_get_movie_rating(context, movie_rating):
    object_data = context.imdb_movie.get_movie_rating()
    assert object_data == movie_rating, f"El rating no coincide con 8.8"