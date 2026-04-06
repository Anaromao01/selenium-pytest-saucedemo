# ✅ QA Automation Portfolio — SauceDemo (Selenium + Pytest)

This repository is part of my **QA Automation portfolio**, focused on automated testing using **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** design pattern.

The goal is to demonstrate professional project organization, best practices, and end-to-end test execution in a fictional e-commerce system.

---

##  Technologies Used

- Python 3.12  
- Selenium WebDriver  
- Pytest  
- WebDriver Manager  
- Page Object Model (POM)  

---

##  Application Under Test

Demo system: **SauceDemo**

https://www.saucedemo.com/

---

##  Automated Features

### Implemented Tests:

- Login with valid credentials  
- Add product to cart  
- Complete checkout flow (End-to-End)  

---

##  Project Structure

```bash
Selenium-ChromeDrive/
│
├── pages/                  # Page Objects (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/                  # Automated test cases
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   └── test_checkout_e2e.py
│
├── screenshots/            # Automatic failure evidence
│
├── conftest.py             # WebDriver fixture + screenshot hook
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
└── README.md
```
--- 
##  Project Structure

Project developed by Ana Claudia Romão

🔗 LinkedIn: https://www.linkedin.com/in/ana-claudia-rom%C3%A3o-9082a133/