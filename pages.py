from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import retrieve_phone_code

class UrbanRoutesPage:
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD   = (By.ID, 'to')

    CALL_A_TAXI_BUTTON = (By.XPATH, '//button[text()="Chamar um táxi"]')
    COMFORT_TARIFF_OPTION = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    CURRENT_TARIFF        = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    ADD_PHONE_NUMBER_MAIN_BUTTON = (By.XPATH, '//div[@class="np-button"]//div[contains(text(), "Número de telefone")]')
    PHONE_NUMBER_INPUT_FIELD     = (By.ID,    'phone')
    PHONE_NUMBER_NEXT_BUTTON     = (By.XPATH, '//button[text()="Próximo"]')
    PHONE_CODE_FIELD             = (By.ID,    'code')
    PHONE_NUMBER_CONFIRM_BUTTON  = (By.XPATH, '//button[contains(text(), "Confirmar")]')
    REGISTERED_PHONE_NUMBER      = (By.XPATH, '//div[contains(@class, "np-text")]')
    PAYMENT_METHOD_BUTTON  = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Método de pagamento")]')
    ADD_CARD_OPTION_BUTTON = (By.XPATH, '//div[contains(text(), "Adicionar cartão")]')
    CARD_NUMBER_INPUT      = (By.ID,    'number')
    CARD_CODE_INPUT        = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    FINAL_ADD_CARD_BUTTON  = (By.XPATH, '//button[contains(text(), "Adicionar")]')
    CURRENT_PAYMENT_METHOD = (By.XPATH, '//div[contains(@class, "pp-value-text")]')
    MESSAGE_FOR_DRIVER_FIELD               = (By.ID,    'comment')
    BLANKET_AND_HANDKERCHIEFS_OPTION_DIV   = (By.XPATH, "//div[contains(text(), 'Cobertor e lençóis')]/following-sibling::div[1]/div")
    BLANKET_AND_HANDKERCHIEFS_OPTION_INPUT = (By.XPATH, "//div[contains(text(), 'Cobertor e lençóis')]/following-sibling::div[1]/div/input")
    ADD_ICECREAM_BUTTON                    = (By.XPATH, "//div[text()='Sorvete']/following::div[contains(@class, 'counter-plus')][1]")
    CURRENT_ICECREAM_AMOUNT_FIELD          = (By.XPATH, "//div[text()='Sorvete']/following::div[contains(@class, 'counter-value')][1]")
    ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "smart-button")]')
    ORDER_TIMER  = (By.XPATH, '//div[contains(@class, "order-header-time")]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
         self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_value(self, locator):
        return self._find(locator).get_attribute('value')

    def _get_text(self, locator):
        return self._find(locator).text

    def _press_tab(self):
        self.driver.switch_to.active_element.send_keys(Keys.TAB)

    def set_route_addresses(self, from_address, to_address):
        self._type(self.FROM_FIELD, from_address)
        self._type(self.TO_FIELD, to_address)

    def get_from_field_text(self):
        return self._get_value(self.FROM_FIELD)

    def get_to_field_text(self):
        return self._get_value(self.TO_FIELD)

    def click_call_a_taxi_button(self):
        self._click(self.CALL_A_TAXI_BUTTON)

    def click_comfort_option(self):
        self._click(self.COMFORT_TARIFF_OPTION)

    def get_selected_tariff_option(self):
        return self._get_text(self.CURRENT_TARIFF)

    def set_phone(self, phone_number):

        self._click(self.ADD_PHONE_NUMBER_MAIN_BUTTON)
        self._type(self.PHONE_NUMBER_INPUT_FIELD, phone_number)
        self._click(self.PHONE_NUMBER_NEXT_BUTTON)
        phone_code = retrieve_phone_code(self.driver)
        self._type(self.PHONE_CODE_FIELD, phone_code)
        self._click(self.PHONE_NUMBER_CONFIRM_BUTTON)

    def get_inserted_phone_number(self):
        # Retorna o telefone exibido após a confirmação
        return self._get_text(self.REGISTERED_PHONE_NUMBER)

    def set_card(self, card_number, card_code):

        # Passo 1: Abrir a área de métodos de pagamento.
        self._click(self.PAYMENT_METHOD_BUTTON)

        # Passo 2: Escolher a opção de adicionar cartão.
        self._click(self.ADD_CARD_OPTION_BUTTON)

        # Passo 3: Preencher o número do cartão.
        self._type(self.CARD_NUMBER_INPUT, card_number)

        self._type(self.CARD_CODE_INPUT, card_code)

        self._press_tab()

        self._click(self.FINAL_ADD_CARD_BUTTON)


    def get_current_payment_method(self):
        # Retorna a forma de pagamento atualmente selecionada
        return self._get_text(self.CURRENT_PAYMENT_METHOD)

    def set_message_for_driver(self, message):
        # Preenche a mensagem personalizada que será enviada ao motorista
        self._type(self.MESSAGE_FOR_DRIVER_FIELD, message)

    def get_message_for_driver(self):
        # Retorna a mensagem que está preenchida no campo
        return self._get_value(self.MESSAGE_FOR_DRIVER_FIELD)

    def click_blanket_and_handkerchiefs_option(self):
        # Marca a opção de cobertor e lençóis para a corrida
        self._click(self.BLANKET_AND_HANDKERCHIEFS_OPTION_DIV)


    def is_blanket_and_handkerchiefs_option_checked(self):
        # Verifica se a opção de cobertor e lençóis foi marcada
        return self._find(self.BLANKET_AND_HANDKERCHIEFS_OPTION_INPUT).is_selected()

    def add_icecream(self, amount):
        for _ in range(amount):
            self._click(self.ADD_ICECREAM_BUTTON)

    def get_current_icecream_amount(self):
        # Retorna a quantidade atual de sorvetes selecionados
        return int(self._get_text(self.CURRENT_ICECREAM_AMOUNT_FIELD).strip())

    def click_order_button(self):
        # Clica no botão final para pedir o carro
        self._click(self.ORDER_BUTTON)

    def is_order_taxi_popup_displayed(self):
        # Verifica se o timer do pop-up de busca do carro apareceu na tela
        return self._find(self.ORDER_TIMER).is_displayed()
