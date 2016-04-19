from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import json
common_SUCCESS_STR ="success string"
RESPONSE_JSON_TYPE = "json response"
XML_TAG = "xmltag"
RESPONSE_XML_TYPE = "XMl type"
RESPONSE_CODE_POSTPARAMS_ERROR = "1"
RESPONSE_STRING_POST_PARAMS ="Error"


def updateSuccessString(respCode, respStr, apiName):
    if respCode == '0':
        return eval(apiName + '_SUCCESS_STR')
    return respStr

def modifyJson(jsonObj, key, value):
    if value !=  None and  value !=  'None':
        jsonObj[key] = value
    return jsonObj


def prepareFinalResponse(response, responseCode, responseString, details):
    response = modifyJson(response, "resCode", responseCode)
    response = modifyJson(response, "resStr", responseString)
    response = modifyJson(response, "resDet", details)
    return response

def returnResponse(responseCode, responseString, apiName, response, details, responseType):
    responseString = updateSuccessString(responseCode, responseString, apiName)
    response = prepareFinalResponse(response, responseCode, responseString, details)
    response = json.dumps(response)
    responseTypeHeader = RESPONSE_JSON_TYPE
    if responseType == XML_TAG:
        responseTypeHeader = RESPONSE_XML_TYPE
        response = dicttoxml.dicttoxml(json.loads(response))
    return response, responseTypeHeader

def authenticatev1(username,password):
    user = authenticate(username=username, password=password)
    try:
        user_name = user.username
    except Exception,e:
        user_name = ""
        print str(e)
    return user_name,user


