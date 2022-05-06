from planetmint_driver import Planetmint
from planetmint_driver.crypto import generate_keypair

# create wallets for all involved parties

# producer
# buyer
# reseller
producer, buyer, reseller = generate_keypair(), generate_keypair(), generate_keypair()


# create certificate

asset = {
    'data': {
        "GTIN":{
            "GIAI":"(8004)9010381300003022",
            "ManufacturingSerialID":"141-09-061",
            "RefurbishmentLotNumber":"EHZ COMPOUND MnEDH",
            "ManufacturingLotID":"'L ' SBBVI-30",
            "DataMatrix":"ipld:QmRPa4pQRPQeEKUUktkonkpG8EUZUgufw415Jxd3t4VNQm"
        },
        "Certificate": {
        "A03": "0000001",
        "A01": {
            "CompanyName": "voestalpine Weichensysteme GmbH",
            "AddressLine": "Schmidhüttenstrasse 5",
            "ZipCode": "8740",
            "City": "Zeltweg",
            "Country": "AT",
            "VAT_Id": "U36909609"
        },
        "A06": {
            "CompanyName": "König Stahl Sp.z.o.o",
            "Street": "Cybernetyki 10",
            "ZipCode": "02-677",
            "City": "Warszawa",
            "Country": "PL",
            "VAT_Id": "5270103379"
        },
        "B01": "EN10025",
        "B02": "S275J2H",
        "B07": "175508",
        "B13": "24000",
        "C71": "0.1500",
        "C72": "0.0050",
        "C73": "1.0000",
        "C74": "0.0018",
        "C75": "0.2086",
        "C76": "0.0389",
        "C77": "0.0122",
        "C78": "0.0226",
        "C79": "0.0081",
        "C80": "0.0029",
        "C81": "0.0403",
        "C82": "0.0031",
        "C83": "0.0024",
        "C86": "0.017",
        "C93": "0.3361",
        "Z02": "2019-05-30T09:30:10-01:00"
        }
    }
}

metadata = {
    'units': '300',
    'carbonOffset': '560',
    'type': 'KG'
}

# alternatively asset as ipld link

'''
    asset = {
    'ns': "ipld.bigchaindb.com",
    'did': "did:ipld:QmSvFxoRrJnd1r8N28U7DcEfKmSgSZvDgdDj7JLMP74PMX,type=blinded-zenroom-cid",
    'blindKeyPath': 'm/"SLIP-0021"/"Authentication key":47194e938ab24cc82bfa25f6486ed54bebe79c40ae2a5a32ea6db294d81861a6'

 }
'''

server = 'https://test.ipdb.io'
api = 'api/v1/transactions'
plmnt = Planetmint(server)

prepared_token_tx = plmnt.transactions.prepare(
            operation='CREATE',
            signers=producer.public_key,
            recipients=[([producer.public_key], 3000)],
            asset=asset,
            metadata=metadata)

signed_asset_creation = plmnt.transactions.fulfill(
            prepared_token_tx,
            private_keys=producer.private_key)

response = plmnt.transactions.send_commit(signed_asset_creation)
print( f"\nProduced assets: {server}/{api}/{response['id']}")
