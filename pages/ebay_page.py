from selene import browser, have


class EbayPage:

    def open(self):
        browser.open('/')
        return self

    def search(self, query: str):
        browser.element('#gh-ac').type(query)
        browser.element('#gh-btn').click()
        return self

    def should_see_results_with(self, text: str):
        browser.all('.s-item__title').element_by(have.text(text)).should(have.text(text))
        return self

    def apply_condition_filter(self, condition: str):
        browser.element(f'label[for*="{condition.lower()}"]').click()
        return self

    def should_see_condition(self, condition_text: str):
        browser.all('.s-item__subtitle').filtered_by(have.text(condition_text)).should(have.size_greater_than(0))
        return self

    def should_see_zero_results(self):
        browser.element('.srp-controls__count-heading').should(have.text('0 results'))
        return self
