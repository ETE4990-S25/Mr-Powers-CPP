#from condenced from Lecture 11
import threading
import requests
import json
def fetch_rate(bases, symbols =['eur','jpy','usd'] ):
    for base in bases:
        web = "http://www.floatrates.com/daily/"+str(base)+".json"
        response = requests.get(web)
        rate = response.json()
        rate[base]= {'rate':1}
        
        #create a line to output the rate
        rates_line = ", ".join(
            [f"{symbol}{float(rate[symbol]['rate']):10.04}" 
             for symbol in symbols]
        )
        print(f"{base} = {rates_line}")
