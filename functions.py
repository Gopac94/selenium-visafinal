# For testing
# ------------------------------------
from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "http://vizefinal.net"
driver.get(url)
# -------------------------------------


def justVisaFinal():
    inputVisa  = int(input("vize notun:"))
    inputVisaRate = int(input("vize oranı:"))
    inputFinal = int(input("final notun:"))
    inputFinalRate = int(input("final oranı:"))
    driver.find_element_by_id("4").click() #FOR TESTİNG
    visaElement = driver.find_element_by_id("vn")
    visaRateElement = driver.find_element_by_id("vo")
    finalElement = driver.find_element_by_id("fn")
    finalRateElement = driver.find_element_by_id("fo")
    visaElement.send_keys(inputVisa)
    visaRateElement.send_keys(inputVisaRate)
    finalElement.send_keys(inputFinal)
    finalRateElement.send_keys(inputFinalRate)

def extra1():
    extra1  = int(input("1.Extra Değerlendirme Notu:"))
    extra1Rate = int(input("1.Extra Değerlendirme Oranı:"))
    extra1Element = driver.find_element_by_id("d1n")
    extra1RateElement = driver.find_element_by_id("d1o")
    extra1Element.send_keys(extra1)
    extra1RateElement.send_keys(extra1Rate)

def extra2():
    extra2  = int(input("2.Extra Değerlendirme Notu:"))
    extra2Rate = int(input("2.Extra Değerlendirme Oranı:"))
    extra2Element = driver.find_element_by_id("d2n")
    extra2RateElement = driver.find_element_by_id("d2o")
    extra2Element.send_keys(extra2)
    extra2RateElement.send_keys(extra2Rate)

def extra3():
    extra3  = int(input("3.Extra Değerlendirme Notu:"))
    extra3Rate = int(input("3.Extra Değerlendirme Oranı:"))
    extra3Element = driver.find_element_by_id("d3n")
    extra3RateElement = driver.find_element_by_id("d3o")
    extra3Element.send_keys(extra3)
    extra3RateElement.send_keys(extra3Rate)

def extra4():
    extra4  = int(input("4.Extra Değerlendirme Notu:"))
    extra4Rate = int(input("4.Extra Değerlendirme Oranı:"))
    extra4Element = driver.find_element_by_id("d4n")
    extra4RateElement = driver.find_element_by_id("d4o")
    extra4Element.send_keys(extra4)
    extra4RateElement.send_keys(extra4Rate)

def calculation():
    driver.find_element_by_id("hesap").click()
    #put timer here.
    print(driver.find_element_by_id("bilgiAlanı"))


justVisaFinal() #for testing
        
        





