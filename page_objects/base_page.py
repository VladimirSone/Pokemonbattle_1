class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # кликнуть на нужный элемент
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    # @allure.step('Проскроллить до нужного элемента: например до кнопки')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    # @allure.title('открытие новой вкладки')
    def switch_to_next_tab(self):
        self.driver.switch_to.new_window(self.driver.window_handles[1])