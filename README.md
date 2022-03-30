# Tinkoff USD/RUB exchange rate

Because of the rapid change in the exchange rate, I decided to implement my own script to track the USD/RUB on the Tinkoff bank platform. The script shows the buy/sell rate every 30 seconds in the console, meanwhile saving all data with time metadata into database files with the name of the exchange rate's date. 

Here is the used source for exchange rate data pulling:

- https://www.tinkoff.ru/api/v1/currency_rates/

If you want to SELL Russian roubles on a suitable time, run the following script and track the rates:

```
$ ./sell.py
```

![](https://github.com/KerimKochekov/tinkoff_USD-RUB/blob/main/sell.png)

If you want to BUY Russian roubles on a suitable time, run the following script and track the rates:

```
$ ./buy.py
```
