import allure
from allure_commons.types import Severity
from pages.main_page import MainPage

main_page = MainPage()


@allure.id("1")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Поиск товаров")
@allure.title("Поиск товаров по ключевому слову")
@allure.link("https://www.ebay.com", name="eBay")
def test_search_items_by_keyword():
    with allure.step("Открыть главную страницу и выполнить поиск по ключевому слову 'laptop'"):
        (
            main_page
            .open_ebay_main_page()
            .search_for("laptop")
            .results_should_contain_text("laptop")
        )


@allure.id("2")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Корзина")
@allure.title("Добавление первого товара в корзину")
@allure.link("https://www.ebay.com", name="eBay")
def test_add_first_item_to_cart():
    with allure.step("Открыть главную страницу, найти 'headphones', открыть первый товар и добавить в корзину"):
        (
            main_page
            .open_ebay_main_page()
            .search_for("headphones")
            .open_first_item()
            .add_to_cart()
            .cart_should_not_be_empty()
        )


@allure.id("3")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Корзина")
@allure.title("Проверка наличия товара в корзине")
@allure.link("https://www.ebay.com", name="eBay")
def test_cart_contains_item():
    with allure.step("Открыть корзину и проверить, что она не пуста"):
        (
            main_page
            .open_ebay_main_page()
            .go_to_cart()
            .cart_should_not_be_empty()
        )


@allure.id("4")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Интерфейс")
@allure.title("Проверка элементов хэдера")
@allure.link("https://www.ebay.com", name="eBay")
def test_header_elements_visibility():
    with allure.step("Проверить видимость элементов хэдера"):
        main_page.open_ebay_main_page().check_header_elements()


@allure.id("5")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Интерфейс")
@allure.title("Проверка элементов футера")
@allure.link("https://www.ebay.com", name="eBay")
def test_footer_elements_visibility():
    with allure.step("Проверить видимость элементов футера"):
        main_page.open_ebay_main_page().check_footer_elements()


@allure.id("6")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Главная страница")
@allure.title("Проверка видимости популярных категорий")
@allure.link("https://www.ebay.com", name="eBay")
def test_popular_categories_visibility():
    with allure.step("Проверить видимость популярных категорий на главной странице"):
        main_page.open_ebay_main_page().popular_categories_should_be_visible()


@allure.id("7")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры")
@allure.title("Проверка фильтров состояния и бренда")
@allure.link("https://www.ebay.com", name="eBay")
def test_condition_and_brand_filters():
    with allure.step("Открыть главную страницу, найти 'tablet' и проверить фильтры состояния и бренда"):
        (
            main_page
            .open_ebay_main_page()
            .search_for("tablet")
            .check_condition_and_brand_filters()
        )
