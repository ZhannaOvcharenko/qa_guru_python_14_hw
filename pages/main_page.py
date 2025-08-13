import allure
from selene import browser, have, be


class MainPage:

    def __init__(self):
        # Хедер
        self.daily_deals_link = browser.element('//a[@aria-label="Daily Deals"]')
        self.help_contact_link = browser.element('//a[@aria-label="Help & Contact"]')
        self.sign_in_button = browser.element('//a[normalize-space()="Sign in"]')
        self.language_selector = browser.element('#gh-eb-Geo')

        # Поисковая строка
        self.search_input = browser.element('#gh-ac')
        self.search_button = browser.element('#gh-btn')

        # Результаты поиска
        self.search_results = browser.all('li.s-item .s-item__title')
        self.first_item = browser.element('li.s-item:not(.s-item--ad) a.s-item__link')

        # Фильтры
        self.condition_filter_section = browser.element('div[aria-label="Condition"]')
        self.brand_filter_section = browser.element('div[aria-label="Brand"]')

        # Карточка товара
        self.item_title_detail = browser.element('#itemTitle')
        self.item_price_detail = browser.element('#prcIsum, .notranslate')
        self.item_quantity_info = browser.element('#qtySubTxt')

        # Корзина
        self.add_to_cart_button = browser.element('#isCartBtn_btn, #atcRedesignId_btn')
        self.cart_icon = browser.element('#gh-cart-n')
        self.cart_link = browser.element('#gh-cart-i')

        # Футер
        self.footer_logo = browser.element('.gh-w')
        self.footer_links = browser.all('footer a')

    @allure.step("Открыть главную страницу eBay")
    def open_ebay_main_page(self):
        browser.open('https://www.ebay.com/')
        return self

    @allure.step("Выполнить поиск по ключевому слову: {keyword}")
    def search_for(self, keyword):
        self.search_input.should(be.visible).type(keyword)
        self.search_button.should(be.visible).click()
        return self

    @allure.step("Открыть первый товар из результатов поиска")
    def open_first_item(self):
        self.first_item.should(be.visible).click()
        return self

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        self.add_to_cart_button.should(be.visible).click()
        return self

    @allure.step("Проверить, что корзина не пуста")
    def cart_should_not_be_empty(self):
        self.cart_icon.should(be.visible).should(have.no.text('0'))
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.cart_link.should(be.visible).click()
        return self

    @allure.step("Проверить элементы хэдера")
    def check_header_elements(self):
        self.daily_deals_link.should(be.visible)
        self.help_contact_link.should(be.visible)
        self.sign_in_button.should(be.visible)
        self.language_selector.should(be.visible)
        return self

    @allure.step("Проверить элементы футера")
    def check_footer_elements(self):
        self.footer_logo.should(be.visible)
        self.footer_links.should(have.size_greater_than(5))
        return self

    @allure.step("Проверить элементы карточки товара")
    def check_product_detail_elements(self):
        self.item_title_detail.should(be.visible)
        self.item_price_detail.should(be.visible)
        self.item_quantity_info.should(be.visible)
        return self

    @allure.step("Проверить наличие фильтров состояния и бренда")
    def check_condition_and_brand_filters(self):
        self.condition_filter_section.should(be.visible)
        self.brand_filter_section.should(be.visible)
        return self
