from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator.basement_website_locators import BASEMENTWEBSITE
from page_objects.base_page import BasePage

class MainPage(BasePage):

    # @allure.title('проскроллить до раздела вопросы')
    def scroll_to_section_questions(self):
        element = self.driver.find_element(*BASEMENTWEBSITE.text_heatlhcheck)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    # @allure.title('ожидание загрузки текста документа')
    def wait_text_documents(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            BASEMENTWEBSITE.text_website_documents))

    # @allure.title('нажать текст Heatlhcheck')
    def click_button_healthcheck(self):
        self.click_on_element(BASEMENTWEBSITE.text_heatlhcheck)

    # allure.title('проверка, что загрузилась главная страница документа Healthcheck')
    def check_displaying_of_page_heading(self):
        return self.driver.find_element(BASEMENTWEBSITE.text_website_documents).is_displayed()

    # @allure.title('ожидание загрузки страницы')
    def wait_pokemon_battle(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(BASEMENTWEBSITE.text_pokemon_battle))

