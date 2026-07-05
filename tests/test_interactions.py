import re
from playwright.sync_api import Page, expect


def test_search_navigation(page: Page):
    page.goto("https://playwright.dev")

    # Click the search button and type a query
    page.get_by_role("button", name="Search").click()
    page.get_by_placeholder("Search docs").fill("locators")

    # Click the first search result
    page.get_by_role("link", name=re.compile("Locators")).first.click()

    # Verify we landed on the right page
    expect(page.get_by_role("heading", name="Locators", exact=True)).to_be_visible()


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev")

    page.get_by_role("link", name="Get started").click()

    expect(page).to_have_url(re.compile(".*docs/intro"))
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()