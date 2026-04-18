import re
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def clean_price(text):
    if not text: return None
    try:
        val = re.sub(r'[^\d,.]', '', text).replace(',', '.')
        if val.count('.') > 1:
            parts = val.split('.')
            val = "".join(parts[:-1]) + "." + parts[-1]
        return float(val)
    except:
        return None

def get_universal_deals(url):
    """
    Scanează pagini de tip feed (Chollometro principal) pentru a găsi toate k-ofertele.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # User-Agent rotativ sau foarte comun
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
    
    # Evitare detecție Selenium (mai agresiv)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Injectăm script pentru a ascunde 'navigator.webdriver'
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () =>渲染 undefined})"
    })

    deals = []

    try:
        driver.get(url)
        # Simulare scroll uman pentru a activa încărcarea lazy
        for _ in range(3):
            driver.execute_script(f"window.scrollBy(0, {random.randint(500, 1000)});")
            time.sleep(1)

        # Toate ofertele sunt în elemente de tip articol sau div-uri specifice
        # Folosim un selector mai permisiv: .threadCard, article, .thread
        items = driver.find_elements(By.CSS_SELECTOR, "article, .threadCard")

        print(f"   [Scraper] Am găsit {len(items)} elemente pe pagină.")

        for item in items:
            try:
                # Folosim try-except pe fiecare sub-element pentru a nu opri loop-ul
                try:
                    title_el = item.find_element(By.CSS_SELECTOR, "a.thread-title--card, .thread-title")
                    title = title_el.text
                    link = title_el.get_attribute("href")
                except: continue

                # Prețuri
                try:
                    price_text = item.find_element(By.CSS_SELECTOR, ".thread-price, .cept-price").text
                    current_price = clean_price(price_text)
                    
                    old_price_text = item.find_element(By.CSS_SELECTOR, ".thread-price--old, .text--line-through").text
                    old_price = clean_price(old_price_text)
                except:
                    current_price, old_price = None, None

                if title and current_price and old_price:
                    deals.append({
                        "title": title,
                        "link": link,
                        "price": current_price,
                        "old_price": old_price
                    })
            except:
                continue

    except Exception as e:
        print(f"   [Scraper Error] {e}")
    finally:
        driver.quit()
    
    return deals
