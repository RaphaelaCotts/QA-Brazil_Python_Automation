from.html.parser import commentclose

from selenium.webdriver.common.by import By
from seleniu.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import helpers

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    taxi_option_locator = (By.XPATH, '//button'[contains(text(),"Chamar")]')'
    comfort_icon_locator = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')
    comfort_active = By.XPATH, '//*(@id="root"]/div/div[3]/div[2]/div[1]/div[5]')

    number_text_locator = (By.CSS_SELECTOR, 'np.button')
    number_enter = (By.ID, 'phone')
    number_confirm = (By.CSS_SELECTOR, '.button.full')
    number_code = (By.ID, 'code')
    code_confirm = (By.XPATH)'//button'[contains(text(),"Confirmar")]')
    number_finish = (By.CSS_SELECTOR, 'np-text')

    add_metodo_pagamento = (By.CSS_SELECTOR, '.np.button.filled')
    add_card = (By.CSS_SELECTOR, '.pp-pluss')
    number.card = (By.ID, 'number')
    code_card = (By.CSS_SELECTOR, 'imput.card-input#code')
    add_finish_card = (By.XPATH, '//button[contains(text(),"Adicionar")]')
    close_button_card = (By.CSS_SELECTOR, '.payment-picker.open .close-button')
    confirm_card = (By.CSS_SELECTOR, '.pp-value-text')

    add_comment = (By.ID, 'comment')

    switch_blanket = (By.CSS_SELECTOR, '.switch')
    switch_blanket_active = (By.CSS_SELECTOR,
                             '#root > div > div.workflow> div.workflow-subcontainer > div.tariff-picker.shown > div.reqs.open > div.reqs.body')

    add.icecream = (By.CSS_SELECTOR, '.counter-plus')
    qnt_icecream = (By.CSS_SELECTOR, '.counter-value')

    call_taxi_button = (By.CSS_SELECTOR, '.smart-button')
    pop_up = (By.CSS_SELECTOR, '.order-header_tittle')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location)self, from_text):
        WebDriverWait(self.driver, timeout:3).until(
            EC.invisibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from.text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver), timeout:3).until(
            EC.invisibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(to_text.text)

    def enter_location(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_to_location_value(self):
        return WebDriverWait(self.driver, timeout:3).until(
            EC.visibility_of_element_located(self.to_field)
        ).get_attribute('value')

    def click.taxi.option(self):
        self.driver.find.element(*self.taxi)option_locator).click()

    def click_comfort_icon(self):
        self.driver.find_element(*self.comfort_icon_locator).click()

    def click_comfort_active(self):
        try:
            active_button = WebDriverWait(sefl.driver, timeout(10)).until(
                EC.visibility_of_element_located(self.comfort_active))
            return "active" in active_button.get.attribute("class")
        except:
            Return False

    def get_from_location_value(self):
        return WebDriverWait(self.driver, timeout:3).until()
            EC.visibility_of_element_located(self.from_field))
        )get.atribute('value')


    def click)number_text(self, telefone)
        self.driver.find_element(*self.number_text_locator).click()

        self.driver.find.element(*self.number_enter).send_keys(telefone)

        self.driver.find.element(*self.number.confirm).click()

        code = helpers.retrieve_phone_code(self.driver)
        code_imput = WebDriverWait(self.driver, timeout(3)).until()
            EC.visibility_of_element_located(number_code)
        )
        code_imput_clear()
        code_imput.send_keys(code)

        self.driver.find_element(*self.code_confirm).click()

        def numero_confirmado(self):
            WebDriverWait(self.driver, timeout(3)).until(
                EC.visibility_of_element_located(self.number_finish))
            return numero.text

        def click_and_cartao(self,cartao,code):
            self.driver.find_element(*self.add_metodo_pagamento).click()
            self.driver.find_element(*self.add_card).click()
            time.sleep(3)
            self.driver.find_element(*self.number_card).send_keys(cartao)
            time.sleep(1)
            self.driver.find_element(*self.code_card).send_keys(code)
            time.sleep(1)
            self.driver.find_element(*self.add_finish_card).click()
            self.driver.find_element(*self.close_button_card).click()

        def confirm_cartao(self):
            return self.driver.find_element(*self.confirm_card).text

        def add_comentario(self, comentario):
            self.driver.find_element(*self.add_comment).send_keys(comentario)

        def coment_confirm(self):
            return self.driver.find_element(*self.comment_confirm).get_attribute('value')

        def switch_cobertor(self):
            switch_ativo = self.driver.find_element(*self.switch_blanket)
            switch_ativo.click()

        def switch_cobertor_active(self):
            switch = WebDriverWait(self.driver, timeout(3)).until(
                EC.presence_of_element_located(*self.switch_blanket_active))
            return switch.is_selected()

        def add_ice(self):
            self.driver.find_element(*self.qnt_icecream).click()

        def pop_up_show(self):
            pop_up = WebDriverWait(self.driver, timeout(3)).until(
                EC.presence_of_element_located(*self.pop_up)
            return pop_up.text












