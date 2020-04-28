from selenium.webdriver.common.by import By

BASE_PAGE_LOCATORS = {}
LOGIN_PAGE_LOCATORS = {
    'logo':                     (By.CSS_SELECTOR, '.overlay-signup__logo'),
    'sign up button':           (By.CSS_SELECTOR, '.overlay-signup__btn'),
    'sign in title':            (By.CSS_SELECTOR, '.signup__title-form'),
    'sign in social panel':     (By.CSS_SELECTOR, '.signup__social'),
    'email input':              (By.CSS_SELECTOR, '.signup__input-text#email'),
    'password input':           (By.CSS_SELECTOR, '.signup__input-text#password'),
    'password recover button':  (By.CSS_SELECTOR, '[data-autotest-id="mr-link-forgot-password-1"]'),
    'sign in button':           (By.CSS_SELECTOR, '.signup__submit'),
    'sign in SSO button':       (By.CSS_SELECTOR, '[data-autotest-id="mr-link-signin-with-sso-1"]'),
    'enter email notice':       (By.CSS_SELECTOR, '[data-autotest-id="mr-error-please enter your email address.-1"]'),
    'enter password notice':    (By.CSS_SELECTOR, '[data-autotest-id="mr-error-please enter your password.-1"]'),
    'wrong credentials notice': (By.XPATH, '//div[contains(@data-autotest-id, "mr-error-the email or password")]'),
}
