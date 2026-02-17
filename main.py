from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # pyright: ignore[reportMissingImports]
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore


print("🚀 Iniciando teste Selenium - SauceDemo Login")

# 1. Setup do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

try:
    # 2. Abrir o site
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    print("✅ Site carregado")

    # 3. Localizar campos de login
    username = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    password = driver.find_element(By.ID, "password")

    # 4. Inserir credenciais válidas
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    print("✅ Credenciais preenchidas")

    # 5. Clicar em Login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # 6. Validação: usuário entrou na página de produtos
    title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert title.text == "Products"

    print("🎉 TESTE PASSOU: Login realizado com sucesso!")

except Exception as e:
    print("❌ TESTE FALHOU:", e)
    driver.save_screenshot("erro_login.png")
    print("📸 Screenshot salva como erro_login.png")

finally:
    driver.quit()
    print("🧹 Navegador fechado")
