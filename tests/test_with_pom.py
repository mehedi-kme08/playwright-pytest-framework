import re
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.docs_page import DocsPage


def test_search_navigation(page: Page):
    home = HomePage(page)
    docs = DocsPage(page)

    home.open()
    home.search("locators")
    home.click_search_result("Locators")

    expect(docs.heading("Locators")).to_be_visible()


def test_get_started_link(page: Page):
    home = HomePage(page)

    home.open()
    home.go_to_get_started()

    expect(page).to_have_url(re.compile(".*docs/intro"))