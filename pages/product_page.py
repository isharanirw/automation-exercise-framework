class ProductPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://automationexercise.com/products"

        # Locators
        self.all_products_heading = page.locator('h2.title.text-center:has-text("All Products")')
        self.product_list = page.locator('.product-image-wrapper')
        self.search_input = page.locator('#search_product')
        self.search_button = page.locator('#submit_search')
        self.searched_products_heading = page.locator('h2.title.text-center:has-text("Searched Products")')
        self.product_names = page.locator('.productinfo p')
        self.view_product_button = page.locator('a[href="/product_details/1"]')
        self.product_detail_name = page.locator('.product-information h2')
        self.continue_shopping_button = page.locator('button:has-text("Continue Shopping")')
        self.view_cart_button = page.locator('a:has-text("View Cart")')
        self.category_women = page.locator('a[href="#Women"]')
        self.category_women_dress = page.locator('a[href="/category_products/1"]')

    def navigate(self):
        self.page.goto(self.url)

    def search_product(self, keyword):
        self.search_input.fill(keyword)
        self.search_button.click()

    def is_all_products_visible(self):
        return self.all_products_heading.is_visible()

    def is_searched_products_visible(self):
        return self.searched_products_heading.is_visible()

    def get_product_count(self):
        return self.product_list.count()

    def view_first_product(self):
        first_product = self.product_list.first
        first_product.hover()
        view_button = first_product.locator('a[href="/product_details/1"]')
        view_button.wait_for(state="visible")
        view_button.click()
        # Wait for product detail heading to appear
        self.product_detail_name.wait_for(state="visible")

    def get_product_detail_name(self):
        return self.product_detail_name.text_content()

    def add_first_product_to_cart(self):
        # Hover over first product to reveal the Add to cart button
        first_product = self.product_list.first
        first_product.hover()
        add_button = first_product.locator('a.add-to-cart').first
        add_button.wait_for(state="visible")
        add_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def go_to_cart(self):
        self.view_cart_button.click()

    def dismiss_ad_if_present(self):
        # Dismiss Google ad overlay if it appears
        try:
            ad_close = self.page.locator('#google_vignette')
            if ad_close.is_visible(timeout=3000):
                self.page.keyboard.press("Escape")
                self.page.wait_for_timeout(500)
        except Exception:
            pass

    def filter_by_women_dress(self):
        # Navigate directly to Women > Dress category page
        # bypassing the homepage ad issue
        self.page.goto("https://automationexercise.com/category_products/1")
        self.page.wait_for_load_state("networkidle")