from bs4 import BeautifulSoup
from datetime import datetime
import time
import requests as r
import pretty_print as p



length = int(input("Enter the number of seconds to track (600==10 mins) >>"))
priceValue = 0
prev_priceValue = 0
prices = []
with open("prices_"+str(datetime.today())[:-16]+".txt","w") as fout:
    start = time.time()
    while time.time()-start < length:
        #DONT TRY TO DO THIS WITHOUT THE DELAY HOLY SHIT
        time.sleep(1)
        resp = r.get("https://coinmarketcap.com/currencies/bitcoin")

        html = resp.content
        soup = BeautifulSoup(html) #soupify
        price = soup.find(class_="priceValue") #grab the element we want

        
        priceValue = int(price.string[1:3]+price.string[4:7])
        print(priceValue)
        p.pretty_print(str(priceValue))
        

        if priceValue == prev_priceValue:
            continue
        print("  :  "+str(datetime.fromtimestamp(time.time()))[:-7]+" ("+str(priceValue-prev_priceValue)+")"+"\n")
    
        prev_priceValue = priceValue
       
        prices.append(price.string+"  :  "+str(datetime.fromtimestamp(time.time()))[:-7]+" ("+str(priceValue-prev_priceValue)+")"+"\n")        

    fout.writelines(prices)





