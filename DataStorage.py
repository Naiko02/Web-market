from selenium.webdriver.common.by import By

TestData={
    'TestEmail': "MeduzaKarapuza@mail.ru",
    'TestPassword': "12345678"
}

nav_data = {
            'BOOKS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/books"]'],
            'COMPUTERS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/computers"]'],
            'ELECTRONICS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/electronics"]'],
            'APPAREL & SHOES': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/apparel-shoes"]'],
            'DIGITAL DOWNLOADS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/digital-downloads"]'],
            'JEWELRY': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/jewelry"]'],
            'GIFT CARDS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/gift-cards"]'],
            'TEST': [By.CSS_SELECTOR, 'div[class="breadcrumb"] strong[class="current-item"]']
        }

AuthorizationData = {
    'Authorization': [By.CSS_SELECTOR, 'a.ico-login'],
    'Email': [By.CSS_SELECTOR, 'input#Email'],
    'Password': [By.CSS_SELECTOR, 'input#Password'],
    'AuthButton': [By.CSS_SELECTOR, 'div.buttons input[value="Log in"]'],
    'Test': [By.CSS_SELECTOR, 'div.header-links a.account'],


}

RegistrationData = {
    'Registration': [By.CSS_SELECTOR, 'a.ico-register'],
    'Gender': [By.CSS_SELECTOR, 'input#gender-male'],
    'FirstName': [By.CSS_SELECTOR, 'input#FirstName'],
    'LastName': [By.CSS_SELECTOR, 'input#LastName'],
    'Email': [By.CSS_SELECTOR, 'input#Email'],
    'Password': [By.CSS_SELECTOR, 'input#Password'],
    'Confirm': [By.CSS_SELECTOR, 'input#ConfirmPassword'],
    'RegButton': [By.ID, 'register-button'],
    'Test': [By.CSS_SELECTOR, 'div.header-links a.account']

}

SearchData={
    'Search': [By.ID, 'small-searchterms'],
    'Button': [By.CSS_SELECTOR, 'input[value="Search"]'],
    'Test': [By.CSS_SELECTOR, 'h2[class="product-title"] a[href$="science"]']
}

FilterData = {
    'BOOKS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/books"]'],
    'Filter': [By.CSS_SELECTOR, 'a[href*="=50"]'],
    'Test': [By.CSS_SELECTOR, 'h2[class="product-title"] a[href$="science"]']

}

AddCartData = {
    'BOOKS': [By.CSS_SELECTOR, 'ul[class="top-menu"] a[href="/books"]'],
    'Product': [By.CSS_SELECTOR, 'input[onclick*="45/1/1"]'],
    'Cart': [By.CSS_SELECTOR, 'a[class="ico-cart"] span[class="cart-label"]'],
    'Test': [By.CSS_SELECTOR, 'a[class="product-name"][href*=fiction]']

}

ChangeCartData = {
    'ChangeProduct': [By.CSS_SELECTOR, 'tbody .qty input'],
    'ApplyChange': [By.NAME, 'updatecart'],
    'Test': [By.CLASS_NAME, 'product-subtotal']

}