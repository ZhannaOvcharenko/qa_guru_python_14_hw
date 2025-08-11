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
        self.search_input = browser.element('//input[@id="gh-ac"]')
        self.search_button = browser.element('//span[@class="gh-search-button__label"]')

        # Результаты поиска
        self.search_results = browser.all('li.s-item .s-item__title')
        self.item_prices = browser.all('li.s-item span.s-item__price')
        self.first_item = browser.element('li.s-item:not(.s-item--ad) a.s-item__link')
        self.breadcrumbs = browser.all('.breadcrumb li')

        # Фильтры
        self.condition_filter_section = browser.element('div[aria-label="Condition"]')
        self.brand_filter_section = browser.element('div[aria-label="Brand"]')
        self.min_price_input = browser.element('input[aria-label="Minimum Value in $"]')
        self.max_price_input = browser.element('input[aria-label="Maximum Value in $"]')
        self.sort_menu = browser.element('button[aria-label="Sort selector"]')
        self.sort_price_asc_option = browser.element('//a[contains(text(), "Price + Shipping: lowest first")]')

        # Карточка товара
        self.item_title_detail = browser.element('#itemTitle')
        self.item_price_detail = browser.element('#prcIsum, .notranslate')
        self.item_quantity_info = browser.element('#qtySubTxt')

        # Корзина
        self.add_to_cart_button = browser.element('#isCartBtn_btn, #atcRedesignId_btn')
        self.cart_icon = browser.element('#gh-cart-n')
        self.checkout_button = browser.element('[aria-label="Proceed to checkout"]')

        # Переход в корзину
        self.cart_link = browser.element('#gh-cart-i')

        # Футер
        self.footer_logo = browser.element('.gh-w')
        self.footer_links = browser.all('footer a')

        # Блок ошибки
        self.error_message_block = browser.element('h3.srp-controls__count-heading, [data-test-id="no-results"]')

    @allure.step("Открыть главную страницу eBay")
    def open_ebay_main_page(self):
        browser.open('https://www.ebay.com/')
        return self

    @allure.step("Выполнить поиск по ключевому слову: {keyword}")
    def search_for(self, keyword):
        self.search_input.should(be.visible).type(keyword)
        self.search_button.should(be.visible).click()
        return self

    @allure.step("Проверить, что результаты содержат текст: {text}")
    def results_should_contain_text(self, text):
        self.search_results.should(have.size_greater_than(0))
        texts = self.search_results.texts()
        assert any(text.lower() in t.lower() for t in texts), f"Результаты не содержат текст '{text}'"
        return self

    @allure.step("Выбрать категорию: {category}")
    def filter_by_category(self, category):
        browser.element(f'a[href*="{category.lower()}"]').should(be.visible).click()
        return self

    @allure.step("Открыть первый товар из результатов поиска")
    def open_first_item(self):
        self.first_item.should(be.visible).click()
        return self

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        self.add_to_cart_button.should(be.visible).click()
        return self

    @allure.step("Проверить, что товар добавлен в корзину")
    def cart_should_contain_item(self):
        self.cart_icon.should(be.visible).should(have.no.text('0'))
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.cart_link.should(be.visible).click()
        return self

    @allure.step("Проверить, что корзина не пуста")
    def cart_should_not_be_empty(self):
        self.cart_icon.should(be.visible).should(have.no.text('0'))
        return self

    @allure.step("Указать минимальную цену: {price}")
    def filter_price_from(self, price):
        self.min_price_input.should(be.visible).type(price).press_enter()
        return self

    @allure.step("Указать максимальную цену: {price}")
    def filter_price_to(self, price):
        self.max_price_input.should(be.visible).type(price).press_enter()
        return self

    @allure.step("Отсортировать по цене по возрастанию")
    def sort_by_price_ascending(self):
        self.sort_menu.should(be.visible).click()
        self.sort_price_asc_option.should(be.visible).click()
        return self

    @allure.step("Проверить название товара содержит: {text}")
    def item_title_should_contain(self, text):
        self.item_title_detail.should(be.visible).should(have.text(text))
        return self

    @allure.step("Проверить цену товара отображается")
    def item_price_should_be_visible(self):
        self.item_price_detail.should(be.visible)
        text = self.item_price_detail.text.strip()
        assert text != "", "Цена товара не отображается или пустая"
        return self

    @allure.step("Проверить, что цены товаров в диапазоне от {min_price} до {max_price}")
    def results_should_have_price_in_range(self, min_price, max_price):
        self.item_prices.should(have.size_greater_than(0))
        prices_texts = self.item_prices.texts()
        prices = []
        for price_text in prices_texts:
            try:
                price_num = float(price_text.replace("$", "").replace(",", "").strip())
                prices.append(price_num)
            except ValueError:
                continue
        assert all(min_price <= price <= max_price for price in prices), \
            f"Найдены цены вне диапазона {min_price} - {max_price}: {prices}"
        return self
