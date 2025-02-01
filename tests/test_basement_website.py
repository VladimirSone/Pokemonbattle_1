import time
from conftest import driver
from page_objects.basement_website_page import MainPage


class TestBasementWebsite:
    # клик по тексту Healthcheck открывает вкладку с документацией
    def test_text_heatlhcheck_click(self, driver):
        main_page = MainPage(driver)
        main_page.wait_pokemon_battle()  # ожидание загрузки страницы Pokemonbattle
        main_page.scroll_to_section_questions()  # проскроллить вниз страницу
        main_page.click_button_healthcheck()  # клик о тексту Healthcheck
        main_page.switch_to_next_tab()  # активировать новую вкладку
        assert main_page.check_displaying_of_page_heading

    # клик по тексту QA Studio
    def test_icon_qa_studio_click(self, driver):
        main_page = MainPage(driver)
