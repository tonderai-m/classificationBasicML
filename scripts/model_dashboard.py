import ast
import urllib.request
import json
import os
import ssl
import gradio as gr
import pandas as pd
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
def make_payload(product_description):
    data =  {
        "Inputs": {
            "data": [
            {
            "description": product_description
            }
         ]
        },
        "GlobalParameters": 1.0
        }
    body = str.encode(json.dumps(data))
    return body

url = 'https://poc-endpoint.eastus.inference.ml.azure.com/score'
api_key = os.getenv('azure_api')


vertex_cats = pd.read_csv("data/combined_data.csv")
# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'poc-predict' }

def model_predict(product_description="chocolate bar 2-oz", url=url, headers=headers):
    body = make_payload(product_description)
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        result = ast.literal_eval(result.decode("utf-8"))
        result = result.get("Results")[0]
        return vertex_cats.loc[vertex_cats['Category Description'] == result, 'Category Code'].unique()[0]
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
        return error.info()


demo = gr.Interface(fn=model_predict, inputs="text", outputs="text")
demo.launch()

