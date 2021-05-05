import boto3
import json
import logging
from collections import defaultdict
import argparse

client = boto3.client('dynamodb', region_name='us-east-1')

def getMyPetsJson(items):
    myPetList = defaultdict(list)

    for item in items:
        mypet= {}

        mypet["PetId"] = item["PetId"]["S"]
        mypet["PetName"] = item["PetName"]["S"]
        mypet["PetOwner"] = item["PetOwner"]["S"]
        mypet["PetSpecies"] = item["PetSpecies"]["S"]
        mypet["PetAge"] = int(item["PetAge"]["S"])
        mypet["PetImages"] = item["PetImages"]["S"]

        myPetList["mypets"].append(mypet)

    return myPetList

def getAllMyPets():
    response = client.scan(
        TableName='MyPets'
    )

    logging.info(response["Items"])

    myPetList = getMyPetsJson(response["Items"])

    return json.dumps(myPetList)


if __name__ == "__main__":
    
    print("Getting all values")
    items = getAllMyPets()

    print(items)
