from selenium import webdriver
import time
from functions import justVisaFinal,calculation,scoreYouWant,scoreYouWantCalculation,deleteAll

print("Visa and final notes calculator.")
while True:
    while True:
        pick = input("Do you have any other assessments besides midterm and final?(y/n)")
        #-------------------------------------------------------
        #fix this area
        # if pick != "y" or "n":
        #     print("You gave the wrong command.Try again.")
        #     break
        #-------------------------------------------------------
        if pick == "n":
            while True:
                justVisaFinal()
                calculation()
                print("Enter the score you want, calculate how many you need to get from the final.")
                scoreYouWant()
                scoreYouWantCalculation()
                deleteAll()
                break
                
                
            
    
        


    

    