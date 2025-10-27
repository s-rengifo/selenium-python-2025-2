from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ImdbHomePage(BasePage):
    SEARCH_INPUT = (By.CLASS_NAME, "imdb-header-search__input")
    SEARCH_BTN = (By.ID, "suggestion-search-button")

    def search_movie(self, artist_name):
        self.enter_text(self.SEARCH_INPUT, artist_name)
        self.click(self.SEARCH_BTN)

