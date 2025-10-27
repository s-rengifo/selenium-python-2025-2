from behave import given, when, then
from selenium import webdriver
from pages.lastfm_home_page import LastFmHomePage
from pages.lastfm_results_page import LastFmResultPage
from pages.lastfm_artist_page import LastFmArtistPage

@given("el usuario esta en el home page de last.fm")
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm")
    context.lastfm_home = LastFmHomePage(context.driver)

@when('busca al artista "{artist_name}"')
def step_search_artist(context, artist_name):
    context.lastfm_home.search_artist(artist_name)
    context.lastfm_results = LastFmResultPage(context.driver)

@when("selecciona el primer resultado")
def step_search_result(context):
    context.lastfm_results.click_artist_link()
    context.lastfm_artist = LastFmArtistPage(context.driver)

@then('la fecha del ultimo release dede ser "{release_date}"')
def step_get_release_date(context, release_date):
    object_data = context.lastfm_artist.get_latest_release_date()
    assert object_data == release_date, f"La fecha del ultimo release del artista no coincide"