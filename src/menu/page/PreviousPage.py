from menu.page.PageBase import PageBase


class PreviousPage(PageBase):
    def __init__(self, page_id, previous_page: PageBase | None):
        super().__init__(page_id, "Back")
        self.previous_page = previous_page

    def run(self):
        if self.previous_page is not None:
            self.previous_page.run()
