from selenium.webdriver.common.by import By

class BASEMENTWEBSITE:
    # текст Heatlhcheck
    text_heatlhcheck = (By.XPATH, '//a[@class="status_url"]')
    # текст в шапке на странице документации сайта
    text_website_documents = (By.XPATH, './/h2[text()="Время загрузки этой страницы "]')
    # текст Битва покемонов
    text_pokemon_battle = (By.XPATH, '//h1[@class="auth__title"]')