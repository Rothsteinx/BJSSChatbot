import logging
import pandas as pd
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    empfile = pd.read_csv('https://empteststoragev1.blob.core.windows.net/empcsv/Employee.csv').to_dict()
    
    return func.HttpRequest(readfile(empfile), mimetype='application/json', status_code=200)


def readfile(empfile):
    
    for emp in empfile:
        print(empfile[emp])
        
        return json.dumps(empfile)
    