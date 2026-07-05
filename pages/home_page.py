import re
from playwright.sync_api import Page


class HomePage:
    URL = "https://playwright.dev"

    def __init__(self, page: Page):
        self.page = page
        # Locators defined ONCE, here
        self.search_button = page.get_by_role("button", name="Search")
        self.search_input = page.get_by_placeholder("Search docs")
        self.get_started_link = page.get_by_role("link", name="Get started")

    def open(self):
        self.page.goto(self.URL)

    def search(self, query: str):
        self.search_button.click()
        self.search_input.fill(query)

    def click_search_result(self, name: str):
        self.page.get_by_role("link", name=re.compile(name)).first.click()

    def go_to_get_started(self):
        self.get_started_link.click()