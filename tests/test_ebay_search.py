import allure
from allure_commons.types import Severity
from pages.main_page import MainPage

main_page = MainPage()


@allure.id("1")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры поиска")
@allure.title("Проверка фильтров для Laptops")
@allure.link("https://www.ebay.com", name="eBay")
def test_laptops_filters():
    with allure.step("Применить фильтры для Laptops"):
        (
            main_page
            .open_ebay_main_page()
            .search_for("laptop")
            .apply_condition_filter("New")
            .apply_brand_filter("Dell")
            .apply_price_filter("500", "1500")
        )


@allure.id("2")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры поиска")
@allure.title("Проверка фильтров для Smartphones")
@allure.link("https://www.ebay.com", name="eBay")
def test_smartphones_filters():
    with allure.step("Применить фильтры для Smartphones"):
        (
            main_page
            .open_ebay_main_page()
            .search_for("smartphone")
            .apply_condition_filter("Used")
            .apply_brand_filter("Apple")
            .apply_price_filter("200", "800")
        )


@allure.id("3")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры поиска")
@allure.title("Проверка фильтров для Watches")
@allure.link("https://www.ebay.com", name="eBay")
def test_watches_filters():
    with allure.step("Применить фильтры для Watches"):
        (
            main_page
            .open_ebay_main_page()
            .search_for("watch")
            .apply_condition_filter("New")
            .apply_brand_filter("Casio")
            .apply_price_filter("50", "500")
        )


@allure.id("4")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры поиска")
@allure.title("Проверка фильтров для Tablets")
@allure.link("https://www.ebay.com", name="eBay")
def test_tablets_filters():
    with allure.step("Применить фильтры для Tablets"):
        (
            main_page
            .open_ebay_main_page()
            .search_for("tablet")
            .apply_condition_filter("New")
            .apply_brand_filter("Samsung")
            .apply_price_filter("100", "600")
        )


@allure.id("5")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры поиска")
@allure.title("Проверка фильтров для Cameras")
@allure.link("https://www.ebay.com", name="eBay")
def test_cameras_filters():
    with allure.step("Применить фильтры для Cameras"):
        (
            main_page
            .open_ebay_main_page()
            .search_for("camera")
            .apply_condition_filter("Used")
            .apply_brand_filter("Canon")
            .apply_price_filter("150", "1000")
        )


@allure.id("6")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Главная страница")
@allure.title("Проверка видимости популярных блоков на главной странице")
@allure.link("https://www.ebay.com", name="eBay")
def test_trending_blocks_visibility():
    with allure.step("Проверить видимость всех основных блоков на главной странице"):
        main_page.open_ebay_main_page() \
            .check_trending_block("Trending in Sneakers") \
            .check_trending_block("eBay Live") \
            .check_trending_block("Trending in Watches") \
            .check_trending_block("Trending in Refurbished")
