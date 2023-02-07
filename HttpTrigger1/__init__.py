import sys, logging
import requests

import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, BlobType

def main(req: func.HttpRequest) -> func.HttpResponse:
    str_response = ""
    for p in sys.path:
        str_response += p
        str_response += '\n'
    str_response += '\n\n'
    str_response += str(BlobServiceClient)
    str_response += '\n\n'
    logging.info('Python HTTP trigger function processed a request.')
    logging.warning(str(requests))
    logging.warning(str(BlobServiceClient))

    return func.HttpResponse(str_response, status_code=200)
