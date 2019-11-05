 # WhenShouldiBuy  
 analyze and predict after how many days  
 from premiere of mobile phone price is drop to80% from start price  
 Historical Price data are from https://pricespy.co.uk.  
 Prices are in British pounds.
 
 - Polynomial regression is used
 - 7 price ranges used(image below)
 ![alt text](charts.png "Title Text")
 
 
Results :<br />
 **RMSE** of polynomial regression is 1734.4589431839693 <br />
 **R2** of polynomial regression is 0.9333360342522857


For new data<br />
data_begining: 528<br />
percent_treshold 80%: <br />
Begining price( 528 )  should drop to 80% ( 421.96564126781067 )  in  **153** day

 




**TO DO:**  
- convert prices to PLN
- clean code  
- make tests  
- error handling
- GUI
- pep8