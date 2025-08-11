import allure
from allure_commons.types import Severity
from selene import have, be
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
        )
    with allure.step("Проверить, что заголовки результатов содержат 'laptop'"):
        main_page.results_should_contain_text("laptop")


@allure.id("2")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры поиска")
@allure.title("Фильтрация по категории Electronics")
@allure.link("https://www.ebay.com", name="eBay")
def test_filter_by_category():
    (
        main_page
        .open_ebay_main_page()
        .search_for("phone")
        .filter_by_category("Electronics")
        .results_should_contain_text("phone")
    )


@allure.id("3")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Корзина")
@allure.title("Добавление первого товара в корзину")
@allure.link("https://www.ebay.com", name="eBay")
def test_add_first_item_to_cart():
    (
        main_page
        .open_ebay_main_page()
        .search_for("headphones")
        .open_first_item()
        .add_to_cart()
        .cart_should_contain_item()
    )


@allure.id("4")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Корзина")
@allure.title("Проверка наличия товара в корзине")
@allure.link("https://www.ebay.com", name="eBay")
def test_cart_contains_item():
    (
        main_page
        .open_ebay_main_page()
        .go_to_cart()
        .cart_should_not_be_empty()
    )


@allure.id("5")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры по цене")
@allure.title("Фильтрация по цене (диапазон от и до)")
@allure.link("https://www.ebay.com", name="eBay")
def test_filter_by_price_range():
    (
        main_page
        .open_ebay_main_page()
        .search_for("camera")
        .filter_price_from("100")
        .filter_price_to("500")
        .results_should_have_price_in_range(100, 500)
    )


@allure.id("6")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Сортировка")
@allure.title("Сортировка по цене: от меньшей к большей")
@allure.link("https://www.ebay.com", name="eBay")
def test_sort_by_price_ascending():
    (
        main_page
        .open_ebay_main_page()
        .search_for("smartwatch")
        .sort_by_price_ascending()
        .results_should_be_sorted_by_price_ascending()
    )


@allure.id("7")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Обработка ошибок")
@allure.title("Поведение при отсутствии результатов")
@allure.link("https://www.ebay.com", name="eBay")
def test_no_results_behavior():
    (
        main_page
        .open_ebay_main_page()
        .search_for("nonexistentitem")
        .results_should_be_empty()
    )


@allure.id("8")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Интерфейс")
@allure.title("Проверка элементов хэдера")
@allure.link("https://www.ebay.com", name="eBay")
def test_header_elements_visibility():
    main_page.open_ebay_main_page()
    main_page.daily_deals_link.should(be.visible)
    main_page.help_contact_link.should(be.visible)
    main_page.sign_in_button.should(be.visible)
    main_page.language_selector.should(be.visible)


@allure.id("9")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Интерфейс")
@allure.title("Проверка элементов футера")
@allure.link("https://www.ebay.com", name="eBay")
def test_footer_elements_visibility():
    main_page.open_ebay_main_page()
    main_page.footer_logo.should(be.visible)
    main_page.footer_links.should(have.size_greater_than(5))


@allure.id("10")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Карточка товара")
@allure.title("Проверка наличия заголовка, цены и количества")
@allure.link("https://www.ebay.com", name="eBay")
def test_product_detail_elements():
    (
        main_page
        .open_ebay_main_page()
        .search_for("keyboard")
        .open_first_item()
    )
    main_page.item_title_detail.should(be.visible)
    main_page.item_price_detail.should(be.visible)
    main_page.item_quantity_info.should(be.visible)


@allure.id("11")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры")
@allure.title("Проверка наличия фильтров состояния и бренда")
@allure.link("https://www.ebay.com", name="eBay")
def test_condition_and_brand_filters():
    (
        main_page
        .open_ebay_main_page()
        .search_for("tablet")
    )
    main_page.condition_filter_section.should(be.visible)
    main_page.brand_filter_section.should(be.visible)

