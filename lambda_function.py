import json

def lambda_handler(event, context):

    
    if event["Bank Client ID"] == "000":
        return "Bank Client ID 000: Name David"
    elif event["Bank Client ID"] == "001":
        return "Bank Client ID 000: Name Gihan"
    elif event["Bank Client ID"] == "002":
        return "Bank Client ID 000: Name Thushan"
        
    else:
        return "ID is not recongnized"
