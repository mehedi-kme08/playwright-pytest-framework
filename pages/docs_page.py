from playwright.sync_api import Page


class DocsPage:
    def __init__(self, page: Page):
        self.page = page

    def heading(self, name: str):
        return self.page.get_by_role("heading", name=name, exact=True)