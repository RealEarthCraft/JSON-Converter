import json
import geography
from pprint import pprint

inputJSON = json.loads(open(r"inputJSON.json").read())
outputJSON = {}

for objectJSON in inputJSON:
    country = objectJSON["Country"]
    alpha3 = geography.Countries.getRedirectedNameToAlpha3(country)
    if alpha3 is None:
        outputJSON[objectJSON["Country"]] = float(objectJSON["Obesity rate"])
    else:
        outputJSON[alpha3] = float(objectJSON["Obesity rate"])
pprint(outputJSON)
