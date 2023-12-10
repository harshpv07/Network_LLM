
import json
import apiai
import urllib.request
import pprint
from urllib.parse import quote_plus

CLIENT_ACCESS_TOKEN = 'AIzaSyDY2Bd2eFi42KAzngZxIY8O8xvdVp0NVxU'



def botResponseReciever(queryMessage):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.query = queryMessage

    response = request.getresponse()

    rawData = str(response.read())
    rawData = rawData.replace(r"\n" , "")       #Remove \n 
    rawData = rawData.replace(r"b'" , "" , 1)   #Remove b'
    rawData = rawData.replace(r"\'" , "")   #Remove \' which causes prob in the bot message
    #rawData = r"Sorry I didn\u0027t get that..."
    rawData = rawData.replace(r"\u0027" , r"'") # Replaces the decoded message with '
    jsonData = rawData[0:-1]                        #Remove ' in the end

    data = json.loads(jsonData)
    #pprint.pprint(data)

    #textToSpeech(data['result']['fulfillment']['speech'])
    
    
    print(data)

if __name__ == '__main__':
    botResponseReciever("Hey this is Harsh here")
    