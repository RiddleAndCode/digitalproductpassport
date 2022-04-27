# Digital Product Passport Demo

This repository's purpose is to demonstrate the basic capabilites which become available through the integration of the Digital Product Passport on the distributed ledger.

Trusted entities can interact with the Planetmint distributed ledger by attesting data that represents the actual products which are produced in batch sizes and can be processed/transferred partially.
Depending on the status for the physical product itself, a trusted entity can attest relevant data for; 

* Either representing the production/creation of the asset when a physical product is produced or 
* Representing the current status of the physical product when a portion is seperated from the physical product batch for any purpose, such as selling an amount from the batch to another entity.

Thus, representing the physical products digitally through their Digital Product Passport on the distributed ledger with up-to-date information which can be traced back to the origin/provenance, every entity that participating in the distributed ledger is ensured that they interact with the correct and authentic products.
Also, certificates and any required document can be issued digitally so that the authenticity of the data therefore the product is notarized.

With this repository the following functions can be performed on the Planetmint distributed ledger for demonstrating the capabilites explained above: 

* Demonstration on how any product and assets are attested on Planetmint with relevant data in the form of batch sizes
* Demonstration on how any product is sold to resellers, meaning transferring some portion of the original product which is in the form of a batch size
* Demonstration on how a the proof of origin and provenance is conducted

## Digital Product Passport Asset Producing
An entity participating on the Planetmint distributed ledger can perform the attestation for the product specific information along with certificates to a Digital Product Passport.
Attestable data for this function along with asset information has the parameter of unit and type for representing the physical product in the batch form.
Thus, the information then can be used for transferring a portion from the total amount of the batch.

## Digital Product Passport Selling of Assets
An entity participating on the Planetmint distributed ledger can also perform a transfer operation for a portion/fraction of the total batch amount of the physical product.
Along with transferred amount previous owner information is also carried out inside the operation making the product traceable to it's origin of the attestation, therefore the Proof of Origin is provided.
Remainder amount from the transfer operation is kept at the original producer. This operation can be used for selling or transferring a portion of the total batch to a reseller or to an end customer.

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
