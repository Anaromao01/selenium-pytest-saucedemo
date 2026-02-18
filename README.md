# ✅ QA Automation Portfolio — SauceDemo (Selenium + Pytest)

Este repositório faz parte do meu portfólio de **QA Automation**, com foco em testes automatizados utilizando **Selenium WebDriver**, **Pytest** e o padrão **Page Object Model (POM)**.

O objetivo é demonstrar organização profissional de projeto, boas práticas e execução de testes end-to-end em um sistema de e-commerce fictício.

---

## 🚀 Tecnologias utilizadas

- Python 3.12
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Page Object Model (POM)

---

## 📌 Aplicação testada

Sistema demo: **SauceDemo**

https://www.saucedemo.com/

---

## ✅ Funcionalidades automatizadas

### Testes implementados:

- Login com credenciais válidas
- Adicionar produto ao carrinho
- Fluxo completo de checkout (End-to-End)

---

## 🧪 Estrutura do projeto

```bash
Selenium-ChromeDrive/
│
├── pages/                  # Page Objects (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/                  # Test cases automatizados
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   └── test_checkout_e2e.py
│
├── screenshots/            # Evidências automáticas em falha
│
├── conftest.py             # Fixture do WebDriver + screenshot hook
├── pytest.ini              # Configuração do Pytest
├── requirements.txt        # Dependências do projeto
└── README.md


#Autor

Projeto desenvolvido por Ana Claudia Romão
QA em transição para automação de testes.

🔗 LinkedIn: https://www.linkedin.com/in/ana-claudia-rom%C3%A3o-9082a133/
