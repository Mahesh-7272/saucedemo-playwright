from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page=page

    def remove_item(self,product):
        self.page.get_by_test_id(f"remove-{product}").click()