from selenium import webdriver
import time
from functions import justVisaFinal,calculation,scoreYouWant,scoreYouWantCalculation,deleteAll,justVisaFinalCalculator
from functions import picking1,picking2,picking3,picking4,extra1,extra2,extra3,extra4

print("Visa and final notes calculator.")
while True:
    while True:
        pick = input("Do you have any other assessments besides midterm and final?(y/n):")
        
        if pick == "n":
            while True:
                justVisaFinalCalculator()
                break

        if pick == "y":
            while True:
                pickExtra = input("How many extra reviews do you have?(can be max 4, answer : 1,2,3,4):")

                if pickExtra == "1":
                    picking1()
                    extra1()
                    justVisaFinalCalculator()
                    break

                if pickExtra == "2":
                    picking2()
                    extra1()
                    extra2()
                    justVisaFinalCalculator()
                    break

                if pickExtra == "3":
                    picking3()
                    extra1()
                    extra2()
                    extra3()
                    justVisaFinalCalculator()
                    break

                if pickExtra == "4":
                    picking4()
                    extra1()
                    extra2()
                    extra3()
                    extra4()
                    justVisaFinalCalculator()
                    break

        else:
            print("You gave the wrong command.Try again.")
            break


                    


            


        # if pick != "n":
        # else:
            # print("You gave the wrong command.Try again.")
            # break
                
                
            
    
        


    

    