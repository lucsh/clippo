# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List, BinaryIO

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
from string import Template
from dotenv import load_dotenv

import os
import datetime as dt
import requests

load_dotenv()

# Get environment variables
API_AP_URL = os.getenv('API_AP_URL')
AUTH_KEY = os.environ.get('AUTH_KEY')

class ActionRespondTime(Action):

    def name(self) -> Text:
        return "action_respond_time"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
        dispatcher.utter_message("Mmmm, a ver...")
        now = dt.datetime.now()
        message = now.strftime("%H:%M:%S")
        dispatcher.utter_message("Acá son las " + message)
        return []

class ActionRespondAddress(Action):

    def name(self) -> Text:
        return "action_respond_address"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

        dependencia = next(tracker.get_latest_entity_values("dependencia"), None)

        if dependencia:
            headers = {"Authorization": "Bearer " + AUTH_KEY}
            def run_query(query):
                request = requests.post(API_AP_URL, json={'query': query}, headers=headers, timeout=(30, 30))
                if request.status_code == 200:
                    return request.json()
                else:
                    raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

            queryTemplate = Template(
            """{
                 dependencias(filtros:{busqueda:"$query"}){
                   nombre
                   edificio{
                     direccion
                   }
                 }
               }"""
            )

            query = queryTemplate.substitute(query=dependencia)
            dispatcher.utter_message("Mmmm, a ver...")
            result = run_query(query)
            data = result["data"]["dependencias"]

            if data == []:
              message = "Disculpá, no encontré la dependencia que buscas"
            else:
              message = "Encontré los siguientes resultados:\n"
              for dep in data:
                 message = message + " " + dep["nombre"] + ": " + dep["edificio"]["direccion"] + "\n"

        else:
            message = "Disculpá, no entiendio la dependencia que buscas"

        dispatcher.utter_message(message)
        return []

class ActionRespondDay(Action):

    def name(self) -> Text:
        return "action_respond_date"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

        now = dt.datetime.now()
        message = now.strftime("%m/%d/%Y")
        dispatcher.utter_message("Hoy es " + message)
        return []
