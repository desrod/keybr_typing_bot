from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from constants import settings_constants as sc


class SettingsPage:

    def __init__(self, driver):
        self._driver = driver

    def extend_alphabet(self):
        slider = self._driver.find_element(By.XPATH, sc.ALPHABET_SLIDER)
        move = ActionChains(self._driver)
        move.click_and_hold(slider).move_by_offset(288, 0).release().perform()
        print('Alphabet extended!')

    def extend_lesson_length(self):
        slider = self._driver.find_element(By.XPATH, sc.LESSON_LENGTH_SLIDER)
        move = ActionChains(self._driver)
        move.click_and_hold(slider).move_by_offset(288, 0).release().perform()
        print('Lesson length extended!')

    def enable_capital_letters(self):
        self._driver.find_element(By.XPATH, sc.CAPITAL_LETTERS).click()
        print('Capital letters enabled!')

    def enable_punctuation_characters(self):
        self._driver.find_element(By.XPATH, sc.PUNCTUATION).click()
        print('Punctuation characters enabled!')

    def save_settings(self):
        self._driver.find_element(By.XPATH, sc.DONE_BUTTON).click()
        print('Settings saved!')
