# BDL currencies

## Description
This tool fetches the currencies from <ins>[bdl.dz](bdl.dz)</ins> and returns them.

![bdllogo](https://i.ibb.co/vZ9jLZB/t-l-chargement.png)

Currencies fetched are : 

* EUR (EURO)
* USD (US DOLLAR)
* GBP (GREAT BRITAIN POUND)
* JPY (JAPAN YEN)

## Installation
**Selenium** is <ins>**mandatory**</ins> for the functionnality of this tool  

* To install **Selenium**, run the following command

```bash
pip install Selenium
``` 

**NOTE :** You have to download your default browser's webdriver inorder to use this tool as it's <ins>essential</ins> for the usage of **Selenium**  


* Clone this repository via the following command
```bash
git clone https://github.com/Sko-P/BDL-currencies
```

## Usage
1. Import the solution's class (bdl) in your project

```python
from bdl import bdl
```
2. Copy the path to your Webdriver in the *webdriver_* variable and  Instantiate your bdl object and call the main
```bash
username = "machine" #your username here
webdriver_ = f'C:\\Users\\{username}\\Downloads\\chromedriver_win32\\chromedriver'.format(username) 
a = bdl(webdriver_) #Pass the webdriver
currencies = a.main() #returns an array of currencies
```
Calling the main returns an array of currencies (See Demonstration section below for an exemple)

## Demonstration

1. Calling the main and printing it directly in the terminal

```python
a = bdl(webdriver_)
print(a.main())
```
2. Result in the terminal 
```bash
['1 USD 128.4954/128.5104', '1 EURO 152.4983/152.5675', '1 GBP 165.6723/165.7343', '100 JPY 122.0975/122.1582']
```

# DISCLAIMER
This solution is **NOT** provided by BDL nor one of its employees.

# Contribution
If the solution gets you an error, returns you nothing or gives you  incorrect results, this means the structure of [bdl.dz](bdl.dz) has <ins>changed</ins>.  
Feel free to raise an issue or make a pull request to fix that.
# Contact
email : kmedelbachir@gmail.com