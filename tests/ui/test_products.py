import pytest
from playwright.sync_api import Page
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

TEST_EMAIL = "email@testmail.com"
TEST_PASSWORD = "autopw1234"


class TestProducts:

    def test_all_products_page_is_visible(self, page: Page):
        product_page = ProductPage(page)
        product_page.navigate()
        assert product_page.is_all_products_visible(), "All Products heading should be visible"
        assert product_page.get_product_count() > 0, "Product list should not be empty"

    def test_search_product(self, page: Page):
        product_page = ProductPage(page)
        product_page.navigate()
        product_page.search_product("T-Shirt")
        assert product_page.is_searched_products_visible(), "Searched Products heading should appear"
        assert product_page.get_product_count() > 0, "Search results should not be empty"

    def test_view_product_detail(self, page: Page):
        product_page = ProductPage(page)
        product_page.navigate()
        product_page.view_first_product()
        name = product_page.get_product_detail_name()
        assert name is not None and len(name) > 0, "Product detail name should be visible"

    def test_add_product_to_cart(self, page: Page):
        product_page = ProductPage(page)
        cart_page = CartPage(page)
        product_page.navigate()
        product_page.add_first_product_to_cart()
        product_page.continue_shopping()
        cart_page.navigate()
        assert cart_page.get_cart_item_count() > 0, "Cart should have at least one item"

    def test_remove_product_from_cart(self, page: Page):
        product_page = ProductPage(page)
        cart_page = CartPage(page)
        product_page.navigate()
        product_page.add_first_product_to_cart()
        product_page.continue_shopping()
        cart_page.navigate()
        cart_page.remove_first_item()
        page.wait_for_timeout(1000)
        assert cart_page.is_cart_empty(), "Cart should be empty after removing item"

    def test_filter_products_by_category(self, page: Page):
        product_page = ProductPage(page)
        product_page.filter_by_women_dress()
        assert "category_products/1" in page.url, "Should be on Women > Dress category page"
        assert product_page.get_product_count() > 0, "Category should have products"