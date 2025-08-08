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
        main_page.open().search_for("laptop")

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
    with allure.step("Выполнить поиск по ключевому слову 'phone'"):
        main_page.open().search_for("phone")

    with allure.step("Выбрать категорию 'Electronics'"):
        main_page.filter_by_category("Electronics")

    with allure.step("Проверить, что результаты содержат 'phone'"):
        main_page.results_should_contain_text("phone")


@allure.id("3")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Корзина")
@allure.title("Добавление первого товара в корзину")
@allure.link("https://www.ebay.com", name="eBay")
def test_add_first_item_to_cart():
    with allure.step("Выполнить поиск по ключевому слову 'headphones'"):
        main_page.open().search_for("headphones")

    with allure.step("Открыть первый товар из результатов поиска"):
        main_page.open_first_item()

    with allure.step("Добавить товар в корзину"):
        main_page.add_to_cart()

    with allure.step("Проверить, что товар отображается в корзине"):
        main_page.cart_should_contain_item()


@allure.id("4")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Корзина")
@allure.title("Проверка наличия товара в корзине")
@allure.link("https://www.ebay.com", name="eBay")
def test_cart_contains_item():
    with allure.step("Перейти в корзину"):
        main_page.open().go_to_cart()

    with allure.step("Проверить, что корзина не пуста"):
        main_page.cart_should_not_be_empty()


@allure.id("5")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Фильтры по цене")
@allure.title("Фильтрация по цене (диапазон от и до)")
@allure.link("https://www.ebay.com", name="eBay")
def test_filter_by_price_range():
    with allure.step("Выполнить поиск по ключевому слову 'camera'"):
        main_page.open().search_for("camera")

    with allure.step("Указать диапазон цены от 100 до 500"):
        main_page.filter_price_from("100").filter_price_to("500")

    with allure.step("Проверить, что цены в результатах соответствуют диапазону"):
        main_page.results_should_have_price_in_range(100, 500)


@allure.id("6")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Сортировка")
@allure.title("Сортировка по цене: от меньшей к большей")
@allure.link("https://www.ebay.com", name="eBay")
def test_sort_by_price_ascending():
    with allure.step("Выполнить поиск по ключевому слову 'smartwatch'"):
        main_page.open().search_for("smartwatch")

    with allure.step("Отсортировать результаты по цене по возрастанию"):
        main_page.sort_by_price_ascending()

    with allure.step("Проверить, что результаты отсортированы по возрастанию цены"):
        main_page.results_should_be_sorted_by_price_ascending()


@allure.id("7")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Обработка ошибок")
@allure.title("Поведение при отсутствии результатов")
@allure.link("https://www.ebay.com", name="eBay")
def test_no_results_behavior():
    with allure.step("Выполнить поиск по ключевому слову 'nonexistentitem'"):
        main_page.open().search_for("nonexistentitem")

    with allure.step("Проверить, что результат пуст"):
        main_page.results_should_be_empty()


@allure.id("8")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Интерфейс")
@allure.title("Проверка элементов хэдера")
@allure.link("https://www.ebay.com", name="eBay")
def test_header_elements_visibility():
    main_page.open()
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
    main_page.open()
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
    main_page.open().search_for("keyboard").open_first_item()
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
    main_page.open().search_for("tablet")
    main_page.condition_filter_section.should(be.visible)
    main_page.brand_filter_section.should(be.visible)


@allure.id("12")
@allure.tag("web")
@allure.severity(Severity.TRIVIAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Навигация")
@allure.title("Проверка хлебных крошек")
@allure.link("https://www.ebay.com", name="eBay")
def test_breadcrumbs_navigation():
    main_page.open().search_for("book")
    main_page.breadcrumbs.should(have.size_greater_than(0))


@allure.id("13")
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Корзина")
@allure.title("Проверка отображения кнопки 'Checkout'")
@allure.link("https://www.ebay.com", name="eBay")
def test_checkout_button_visible_in_cart():
    main_page.open().go_to_cart()
    main_page.checkout_button.should(be.visible)


@allure.id("14")
@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ZhannaOvcharenko")
@allure.suite("Обработка ошибок")
@allure.title("Проверка блока с сообщением при отсутствии результатов")
@allure.link("https://www.ebay.com", name="eBay")
def test_error_message_block_on_no_results():
    main_page.open().search_for("abcxyz12345")
    main_page.error_message_block.should(be.visible)
