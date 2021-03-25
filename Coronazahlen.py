from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://soziales.hessen.de/gesundheit/corona-in-hessen/taegliche-uebersicht-der-bestaetigten-sars-cov-2-faelle")

tdcount = 0
tabelle = driver.find_elements_by_tag_name("td")

for td in tabelle:
    tdcount +=1
    if tdcount == 34:
        print(f"Die Anzahl der Coronafälle in Gießen beträgt : {td.text}")

driver.quit()
