import allure
from selene import browser, have, be


class MainPage:

    def __init__(self):
        # Поле поиска и кнопка
        self.search_input = browser.element('#gh-ac')
        self.search_button = browser.element('#gh-search-btn')

        # Заголовки товаров
        self.result_titles = browser.all('.s-item__title')

        # Категории фильтров
        self.category_filters = browser.all('.srp-controls__control')

        # Первый товар
        self.first_item_title = self.result_titles.first

        # Кнопка добавления в корзину (универсальный селектор — может отличаться в разных карточках)
        self.add_to_cart_button = browser.element('#isCartBtn_btn, #atcRedesignId_btn, .add-to-cart-btn')

        # Иконка корзины
        self.cart_icon = browser.element('#gh-cart-n')

        # Товары в корзине
        self.cart_items = browser.all('.cart-bucket-lineitem')

        # Поля фильтрации по цене
        self.price_from_input = browser.element('input[aria-label="Minimum Value in $"]')
        self.price_to_input = browser.element('input[aria-label="Maximum Value in $"]')
        self.price_go_button = browser.element('button:has-text("Go")')

        # Сортировка по цене
        self.sort_dropdown = browser.element('select[aria-label="Sort selector"]')
        self.sort_option_lowest_price = self.sort_dropdown.element('option[value*="15"]')

        # Элемент с сообщением об отсутствии результатов
        self.no_results_title = browser.element('.srp-controls__count-heading')

        # Цены на товары
        self.result_prices = browser.all('.s-item__price')

        # Элементы хэдера
        self.daily_deals_link = browser.element('a[title="Daily Deals"]')
        self.help_contact_link = browser.element('a[title="Help & Contact"]')
        self.sign_in_button = browser.element('#gh-ug a[href*="SignIn"]')
        self.language_selector = browser.element('#gh-eb-Geo-a-default')

        # Элементы футера
        self.footer_links = browser.all('footer a')
        self.footer_logo = browser.element('footer img[alt="eBay"]')

        # Элементы карточки товара (на странице товара)
        self.item_title_detail = browser.element('#itemTitle')
        self.item_price_detail = browser.element('#prcIsum, #mm-saleDscPrc')
        self.item_quantity_info = browser.element('#qtySubTxt')

        # Элементы корзины
        self.cart_item_titles = browser.all('.cart-bucket-lineitem .item-title')
        self.checkout_button = browser.element('a[aria-label="Go to checkout"]')

        # Дополнительные фильтры
        self.condition_filter_section = browser.all('.x-refine__main__list').element_by(have.text('Condition'))
        self.brand_filter_section = browser.all('.x-refine__main__list').element_by(have.text('Brand'))
        self.apply_filter_button = browser.element('button[aria-label="Apply"]')

        # Навигация (хлебные крошки)
        self.breadcrumbs = browser.all('.srp-listings__breadcrumb span')

        # Сообщения об ошибке / пустые результаты
        self.error_message_block = browser.element('.srp-controls__count-heading')

    @allure.step("Открыть главную страницу eBay")
    def open(self):
        browser.open('https://www.ebay.com/')
        return self

    @allure.step("Выполнить поиск: {query}")
    def search_for(self, query: str):
        self.search_input.set_value(query)
        self.search_button.click()
        return self

    @allure.step("Проверить, что заголовки содержат: {text}")
    def results_should_contain_text(self, text: str):
        self.result_titles.filtered_by(have.text(text)).should(have.size_greater_than(0))
        return self

    @allure.step("Выбрать категорию: {category}")
    def filter_by_category(self, category: str):
        self.category_filters.element_by(have.text(category)).click()
        return self

    @allure.step("Открыть первый товар")
    def open_first_item(self):
        self.first_item_title.click()
        return self

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        self.add_to_cart_button.click()
        return self

    @allure.step("Проверить, что товар в корзине")
    def cart_should_contain_item(self):
        self.cart_icon.should(be.visible).should_not(have.text('0'))
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.cart_icon.click()
        return self

    @allure.step("Проверить, что корзина не пуста")
    def cart_should_not_be_empty(self):
        self.cart_items.should(have.size_greater_than(0))
        return self

    @allure.step("Установить цену от: {price_from}")
    def filter_price_from(self, price_from: str):
        self.price_from_input.set_value(price_from)
        return self

    @allure.step("Установить цену до: {price_to}")
    def filter_price_to(self, price_to: str):
        self.price_to_input.set_value(price_to)
        self.price_go_button.click()
        return self

    @allure.step("Проверить, что цены в диапазоне от {min_price} до {max_price}")
    def results_should_have_price_in_range(self, min_price: int, max_price: int):
        for price_element in self.result_prices:
            price_text = price_element.text.replace('$', '').replace(',', '').split()[0]
            if price_text.replace('.', '', 1).isdigit():
                price = float(price_text)
                assert min_price <= price <= max_price, f"Цена {price} вне диапазона"
        return self

    @allure.step("Сортировать по возрастанию цены")
    def sort_by_price_ascending(self):
        self.sort_dropdown.click()

        self.sort_option_lowest_price.click()
        return self

    @allure.step("Проверить, что цены отсортированы по возрастанию")
    def results_should_be_sorted_by_price_ascending(self):
        prices = []
        for price_element in self.result_prices:
            price_text = price_element.text.replace('$', '').replace(',', '').split()[0]
            if price_text.replace('.', '', 1).isdigit():
                prices.append(float(price_text))
        assert prices == sorted(prices), "Цены не отсортированы по возрастанию"
        return self

    @allure.step("Проверить, что результатов нет")
    def results_should_be_empty(self):
        self.no_results_title.should(have.text('0 results'))
        return self
