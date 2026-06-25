class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://automationexercise.com/login"

        # Locators
        self.login_email = page.locator('form[action="/login"] input[data-qa="login-email"]')
        self.login_password = page.locator('form[action="/login"] input[data-qa="login-password"]')
        self.login_button = page.locator('button[data-qa="login-button"]')
        self.error_message = page.locator('p:has-text("Your email or password is incorrect!")')
        self.logged_in_text = page.locator('a:has-text(" Logged in as")')
        self.logout_button = page.locator('a[href="/logout"]')

    def navigate(self):
        self.page.goto(self.url)

    def login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()

    def is_logged_in(self):
        return self.logged_in_text.is_visible()

    def is_logged_out(self):
        return self.page.url == "https://automationexercise.com/login"

    def get_error_message(self):
        return self.error_message.is_visible()