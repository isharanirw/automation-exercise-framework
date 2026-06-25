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
        # Wait for the item row to disappear
        self.cart_product_names.first.wait_for(state="hidden", timeout=5000)

    def is_cart_empty(self):
        # Wait for empty cart message to appear
        try:
            self.empty_cart_message.wait_for(state="visible", timeout=5000)
            return self.empty_cart_message.is_visible()
        except Exception:
            return False

    def proceed_to_checkout(self):
        self.proceed_to_checkout.click()