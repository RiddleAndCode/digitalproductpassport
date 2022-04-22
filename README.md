# digital product passport

This repository contains a sample integraiton of a digital product passport (DPP).
The following use cases are contained:
* demonstrate how products and assets can be attested on Planetmint with relevant data and in batch sizes
* demonstrate products being sold to resellers
* demonstrate proof of origin and provenance
  



## DPP produce assets
Asset producers are able to attest certificates and production specifcs similar to a product passport to a DLT. 

## DPP sell assets
Fractions of a production batch can be sold to a reseller or end consumers.

# Using the demo code

## installing system dependencies
```
sudo apt install zsh pipenv make
```

## preparing your environment
```
git clone git clone https://github.com/RiddleAndCode/digitalproductpassport.git
cd digitalproductpassport
pipenv --python 3.9 shell
pipenv install -r requirements.txt
```


## producing assets
```
python dpp_produce.py
```

## reselling assets
```
python dpp_sell_to_reseller.py
```