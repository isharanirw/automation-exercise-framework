class SignupPage:
    def __init__(self, page):
        self.page = page

        #Signup from locators
        self.signup_name = page.locator('input[data-qa="signup-name"]')
        self.signup_email = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')

        # Account info locators
        self.title_mr = page.locator('#id_gender1')
        self.password = page.locator('input[data-qa="password"]')
        self.days = page.locator('select[data-qa="days"]')
        self.months = page.locator('select[data-qa="months"]')
        self.years = page.locator('select[data-qa="years"]')
        self.first_name = page.locator('input[data-qa="first_name"]')
        self.last_name = page.locator('input[data-qa="last_name"]')
        self.address = page.locator('input[data-qa="address"]')
        self.country = page.locator('select[data-qa="country"]')
        self.state = page.locator('input[data-qa="state"]')
        self.city = page.locator('input[data-qa="city"]')
        self.zipcode = page.locator('input[data-qa="zipcode"]')
        self.mobile_number = page.locator('input[data-qa="mobile_number"]')
        self.create_account_button = page.locator('button[data-qa="create-account"]')

        # Success locators
        self.account_created_text = page.locator('h2[data-qa="account-created"]')
        self.continue_button = page.locator('a[data-qa="continue-button"]')
        self.logged_in_text = page.locator('a:has-text(" Logged in as")')
        self.email_exists_error = page.locator('p:has-text("Email Address already exist!")')

    def enter_name_and_email(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()

    def fill_account_details(self, password, first_name, last_name,
                              address, state, city, zipcode, mobile):
        self.title_mr.check()
        self.password.fill(password)
        self.days.select_option("10")
        self.months.select_option("January")
        self.years.select_option("1995")
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.address.fill(address)
        self.country.select_option("Canada")
        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zipcode)
        self.mobile_number.fill(mobile)
        self.create_account_button.click()

    def is_account_created(self):
        return self.account_created_text.is_visible()

    def continue_after_signup(self):
        self.continue_button.wait_for(state="visible")
        self.continue_button.click()
        # Wait for home page to load after registration
        self.page.wait_for_load_state("domcontentloaded")

    def is_logged_in(self):
        self.logged_in_text.wait_for(state="visible", timeout=5000)
        return self.logged_in_text.is_visible()

    def is_email_already_exists(self):
        try:
            self.email_exists_error.wait_for(state="visible", timeout=5000)
            return self.email_exists_error.is_visible()
        except Exception:
            return False