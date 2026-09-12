import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Importar a classe POM

def test_personal_bike_option():
    driver = webdriver.Chrome()
    # Etapa 1: Abra o aplicativo e atualize a URL após iniciar o servidor
    driver.get('https://cnt-fd677479-89ab-4ea3-ad09-0999796f6ec8.containerhub.tripleten-services.com')

    # Crie uma instância da classe de página
    urban_routes_page = UrbanRoutesPage(driver)

    # Etapa 2: use métodos POM para executar ações na página
    # Insira os locais "De" e "Para".
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    # Selecione a opção "Personal".
    urban_routes_page.click_personal_option()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Clique no ícone "Bicicleta".
    urban_routes_page.click_bike_icon()
    time.sleep(2)  # Adicione atraso para visibilidade; opcional

    # Etapa 3: Verifique se o texto da bicicleta é exibido corretamente
    actual_value = urban_routes_page.get_bike_text()
    expected_value = "Bicicleta"
    assert expected_value in actual_value, f"Esperado '{expected_value}', mas obtido '{actual_value}'"
    driver.quit()





