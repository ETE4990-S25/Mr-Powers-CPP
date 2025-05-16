import asyncio
import time
import requests

SYMBOLS = ['eur','jpy','usd','rub','cad']
BASES = ['eur','gbp','aud','chf','cad','jpy','kes','bhd','egp','krw','mro','cop','bbd','djf','hnl','ugx']



async def fetch_rate(base):
    loop = asyncio.get_event_loop()
    web = "http://www.floatrates.com/daily/"+str(base)+".json"
    response = await loop.run_in_executor(
        None, requests.get,web
    )
    response.raise_for_status()
    rates = response.json()
    # note: same currency exchanges to itself 1:1
    rates[base]= {'rate':1}
    return base, rates






async def present_result(result):
    base, rates = (await result)
    rates_line = ", ".join(
        [f"{symbol}{float(rates[symbol]['rate']):10.04}" 
         for symbol in SYMBOLS]
    )
    print(f"1 {base} = {rates_line}")


async def main():
    await asyncio.wait([
        present_result(fetch_rate(base))
        for base in BASES
    ])


if __name__ == "__main__":
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    elapsed = time.time() - started

    print()
    print("time elapsed: {:.2f}s".format(elapsed))