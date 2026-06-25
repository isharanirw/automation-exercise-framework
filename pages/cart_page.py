class CartPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://automationexercise.com/view_cart"

        # Locators
        self.cart_items = page.locator('tr.cart_menu + tr')
        self.cart_product_names = page.locator('.cart_description h4 a')
        self.cart_prices = page.locator('.cart_price p')
        self.cart_quantities = page.locator('.cart_quantity button')
        self.remove_buttons = page.locator('a.cart_quantity_delete')
        self.empty_cart_message = page.locator('b:has-text("Cart is empty!")')
        self.proceed_to_checkout = page.locator('a:has-text("Proceed To Checkout")')

    def navigate(self):
        self.page.goto(self.url)

    def get_cart_item_count(self):
        return self.cart_product_names.count()

    def get_first_product_name(self):
        return self.cart_product_names.first.text_content()

    def remove_first_item(self):
        self.remove_buttons.first.click()

    def is_cart_empty(self):
        return self.empty_cart_message.is_visible()

    def proceed_to_checkout(self):
        self.proceed_to_checkout.click()