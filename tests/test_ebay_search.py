import allure
from allure_commons.types import Severity
from pages.ebay_page import EbayPage


@allure.tag("ebay")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.feature("Поиск на eBay")
@allure.story("Поиск ноутбуков")
@allure.link("https://ebay.com", name="eBay")
def test_search_laptop():
    page = EbayPage()

    with allure.step("Открыть главную страницу eBay"):
        page.open()

    with allure.step("Выполнить поиск 'laptop'"):
        page.search("laptop")

    with allure.step("Проверить, что в результатах есть товары с названием 'laptop'"):
        page.should_see_results_with("laptop")


@allure.story("Поиск iPhone")
def test_search_iphone():
    page = EbayPage()

    with allure.step("Открыть eBay"):
        page.open()

    with allure.step("Искать iPhone 13"):
        page.search("iPhone 13")

    with allure.step("Проверить результаты"):
        page.should_see_results_with("iPhone")


@allure.story("Поиск фотоаппаратов")
def test_search_camera():
    page = EbayPage()

    with allure.step("Открыть eBay"):
        page.open()

    with allure.step("Искать Canon Camera"):
        page.search("Canon Camera")

    with allure.step("Проверить, что Canon встречается в результатах"):
        page.should_see_results_with("Canon")


@allure.story("Фильтрация по б/у товарам")
def test_search_with_filter_used():
    page = EbayPage()

    with allure.step("Открыть eBay"):
        page.open()

    with allure.step("Искать PlayStation 5"):
        page.search("PlayStation 5")

    with allure.step("Применить фильтр 'Used'"):
        page.apply_condition_filter("Used")

    with allure.step("Проверить, что в результатах есть 'Pre-Owned'"):
        page.should_see_condition("Pre-Owned")


@allure.story("Поиск несуществующего товара")
def test_search_zero_results():
    page = EbayPage()

    with allure.step("Открыть eBay"):
        page.open()

    with allure.step("Искать несуществующий товар"):
        page.search("asdasd912u3n1293u")

    with allure.step("Убедиться, что нет результатов"):
        page.should_see_zero_results()
