# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from papers import paper
from books import book


class ActionGetBooks(Action):

    def name(self) -> Text:
        return "action_get_books"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        temp = book()
        dispatcher.utter_template("utter_books", tracker, books = temp)

        return []

class ActionGetPapers(Action):

    def name(self) -> Text:
        return "action_get_papers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        subj = tracker.latest_message['text']
        temp2 = paper(subj)
        dispatcher.utter_template("utter_subjects", tracker, papers = temp2)

        return []
