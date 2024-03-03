# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            dispatcher.utter_message(text="Hallo, ik ben een student-service bot van de AdeKUS. "
                                          "U kunt hier uw vragen stellen")
            return []








class ActionHandlePayload1(Action):
    def name(self) -> Text:
        return "action_handle_button"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the payload from the user's message
        payload = tracker.latest_message['text']

        # Perform actions based on the payload
        if payload == "/link_bachelor_opleidingen":
            # Open the link for bachelor opleidingen
            dispatcher.utter_message(text="Hier is de link naar de webpage voor  bachelor opleidingen: https://www.uvs.edu/studie/aanbod/bacheloropleidingen/")
        elif payload == "/link_master_opleidingen":
            # Open the link for masteropleidingen
            dispatcher.utter_message(text="Hier is de link naar de webpage voor masteropleidingen: https://www.uvs.edu/studie/aanbod/masteropleidingen/")
        return []

# code voor contanct info(buttons)
class ActionHandlePayload2(Action):
    def name(self) -> Text:
        return "action_handle_button_contactinfo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the payload from the user's message
        payload = tracker.latest_message['text']

        # Perform actions based on the payload
        if payload == "/link_secretaris_et":
            dispatcher.utter_message(text="De scretaris van ET is mevr. Inez Cameron. Mail: inez.cameron-tilborg@uvs.edu")
        elif payload == "/link_De_studentendecaan":
            dispatcher.utter_message(text="De studentendecaan is mw. drs. D. Sumter. Zij is te bereiken via 465558 toestel # 2314. E-mail: denise.sumter@uvs.edu")
        elif payload == "/link_Het_faculteitsbureau":
            dispatcher.utter_message(text="Het faculteitsbureau is te bereiken via de centrale telefoonlijn, 465558 op toestel # 2298/2299 (gebouw 17) en toestel # 2356/2357 (gebouw 16). Het decanaat is te bereiken op toestel #2317")
        elif payload == "/link_examencommissie":
            dispatcher.utter_message(text=" De examencommissie-administratie is te bereiken via de centrale telefoonlijn, 465558 op toestel # 2315 en op 8873951, en per email via examencie-ftew@uvs.edu")
        elif payload == "/link_rc":
            dispatcher.utter_message(text="Coördinator (RC) van de richting Elektrotechniek (ET) is Dhr. A. Rampadarath,en de waarnemend RC is Mevr. A. Raghoebarsing. De contactgegevens zijn als volgt:E-mail: anand.rampadarath@uvs.edu voor Dhr. A. Rampadarath en E-mail: amrita.raghoebarsing@uvs.edu voor Mevr. A. Raghoebarsing")
        return []






#1 energielab
class SendMultipleImages1(Action):
    def name(self) -> Text:
        return "action_send_energieLab_Pics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        payload = tracker.latest_message['text']

        # Define images based on payload
        if payload == "/ingang_energie_lab33":
            images = [
                {"url": "https://i.imgur.com/OtpsXXa.png?1", "text": "Het Energie Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit ingang. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/wukJ2GA.png?1", "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Energie Lab te bereiken"},
                {"url": "https://i.imgur.com/IfRkmvR.jpg", "text": "Dit is hoe het Energie Lab in het echt eruit ziet"}
            ]
        elif payload == "/geb17_energie_lab_3338880":
            images = [
                {"url": "https://i.imgur.com/7IH379G.png?1", "text": "Het Energie Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 17. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/wukJ2GA.png?1", "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Energie Lab te bereiken"},
                {"url": "https://i.imgur.com/IfRkmvR.jpg", "text": "Dit is hoe het Energie Lab in het echt eruit ziet"}
            ]
        elif payload == "/geb19_energie_lab_29292929":
            images = [
                {"url": "https://i.imgur.com/mrayVr1.png?1", "text": "Het Energie Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 19. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/wukJ2GA.png?1", "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Energie Lab te bereiken"},
                {"url": "https://i.imgur.com/IfRkmvR.jpg", "text": "Dit is hoe het Energie Lab in het echt eruit ziet"}
            ]
        else:
            # Default images if no specific payload matches
            images = []

        # Send each image with its corresponding text as a separate message
        for image_data in images:
            dispatcher.utter_message(text=image_data["text"], image=image_data["url"])

        return []

#2 voor infolab
class SendMultipleImages2(Action):
    def name(self) -> Text:
        return "action_send_infoLab_Pics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        payload = tracker.latest_message['text']

        # Define images based on payload
        if payload == "/ingang_Informatie_lab12":
            images = [
                {"url": "https://i.imgur.com/OtpsXXa.png?1",
                 "text": "Het Informatie Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit ingang. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/ecbkoh7.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Informatie Lab te bereiken"},
                {"url": "https://i.imgur.com/Kt8afkf.jpg", "text": "Dit is hoe het Informatie Lab in het echt eruit ziet"}
            ]
        elif payload == "/geb17_Informatie_lab1345":
            images = [
                {"url": "https://i.imgur.com/7IH379G.png?1",
                 "text": "Het Informatie Lab  zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 17. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/ecbkoh7.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Informatie Lab te bereiken"},
                {"url": "https://i.imgur.com/Kt8afkf.jpg",
                 "text": "Dit is hoe het Informatie Lab in het echt eruit ziet"}
            ]
        elif payload == "/geb19_Informatie_lab00789":
            images = [
                {"url": "https://i.imgur.com/mrayVr1.png?1",
                 "text": "Het Informatie Lab  zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 19. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/ecbkoh7.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Informatie Lab te bereiken"},
                {"url": "https://i.imgur.com/Kt8afkf.jpg",
                 "text": "Dit is hoe het Informatie Lab in het echt eruit ziet"}
            ]
        else:
            # Default images if no specific payload matches
            images = []

        # Send each image with its corresponding text as a separate message
        for image_data in images:
            dispatcher.utter_message(text=image_data["text"], image=image_data["url"])

        return []

#3 voor CEL
class SendMultipleImages3(Action):
    def name(self) -> Text:
        return "action_send_celLab_Pics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        payload = tracker.latest_message['text']

        # Define images based on payload
        if payload == "/ingang_Computer_educatief_Lab":
            images = [
                {"url": "https://i.imgur.com/OtpsXXa.png?1",
                 "text": "Het Computer Educatief Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit ingang. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/Wp2wYW7.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Computer Educatief Lab te bereiken"},
                {"url": "https://i.imgur.com/JzWBM71.jpg", "text": "Dit is hoe Computer Educatief Lab  in het echt eruit ziet"}
            ]
        elif payload == "/geb17_Computer_educatief_Lab_6969696":
            images = [
                {"url": "https://i.imgur.com/7IH379G.png?1",
                 "text": "Het Computer Educatief Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 17. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/Wp2wYW7.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Computer Educatief Lab te bereiken"},
                {"url": "https://i.imgur.com/JzWBM71.jpg",
                 "text": "Dit is hoe Computer Educatief Lab  in het echt eruit ziet"}
            ]
        elif payload == "/geb19_Computer_educatief_Lab_01010":
            images = [
                {"url": "https://i.imgur.com/mrayVr1.png?1",
                 "text": "Het Computer Educatief Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 19. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/Wp2wYW7.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Computer Educatief Lab te bereiken"},
                {"url": "https://i.imgur.com/JzWBM71.jpg",
                 "text": "Dit is hoe Computer Educatief Lab  in het echt eruit ziet"}
            ]
        else:
            # Default images if no specific payload matches
            images = []

        # Send each image with its corresponding text as a separate message
        for image_data in images:
            dispatcher.utter_message(text=image_data["text"], image=image_data["url"])

        return []

#4 voor TelecomLab

class SendMultipleImages4(Action):
    def name(self) -> Text:
        return "action_send_telecomLab_Pics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        payload = tracker.latest_message['text']

        # Define images based on payload
        if payload == "/ingang_Telecom_Lab_100999":
            images = [
                {"url": "https://i.imgur.com/OtpsXXa.png?1",
                 "text": "Het Telecom Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit ingang. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/GDPAApS.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Telecom Lab te bereiken"},
                {"url": "https://i.imgur.com/7rpCs5g.jpg", "text": "Dit is hoe het Telecom Lab in het echt eruit ziet"}
            ]
        elif payload == "/geb17_Telecom_Lab_00066000700":
            images = [
                {"url": "https://i.imgur.com/7IH379G.png?1",
                 "text": "Het Telecom Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 17. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/GDPAApS.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Telecom Lab te bereiken"},
                {"url": "https://i.imgur.com/7rpCs5g.jpg", "text": "Dit is hoe het Telecom Lab in het echt eruit ziet"}
            ]
        elif payload == "/geb19__Telecom_Lab_444000777":
            images = [
                {"url": "https://i.imgur.com/mrayVr1.png?1",
                 "text": "Het Telecom Lab zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 19. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/GDPAApS.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om het Telecom Lab te bereiken"},
                {"url": "https://i.imgur.com/7rpCs5g.jpg", "text": "Dit is hoe het Telecom Lab in het echt eruit ziet"}
            ]
        else:
            # Default images if no specific payload matches
            images = []

        # Send each image with its corresponding text as a separate message
        for image_data in images:
            dispatcher.utter_message(text=image_data["text"], image=image_data["url"])

        return []

#5 voor admin
class SendMultipleImages5(Action):
    def name(self) -> Text:
        return "action_send_admin_Pics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        payload = tracker.latest_message['text']

        # Define images based on payload
        if payload == "/ingang_naar_administratie":
            images = [
                {"url": "https://i.imgur.com/OtpsXXa.png?1",
                 "text": "De Administratie zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit ingang. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/LLGPlSc.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om de Administratie te bereiken"},
                {"url": "https://i.imgur.com/zCxTf0t.jpg", "text": "Dit is hoe de Administratie in het echt eruit ziet"}
            ]
        elif payload == "/geb17_naar_administratie_565656565":
            images = [
                {"url": "https://i.imgur.com/7IH379G.png?1",
                 "text": "De Administratie zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 17. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/LLGPlSc.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om de Administratie te bereiken"},
                {"url": "https://i.imgur.com/zCxTf0t.jpg", "text": "Dit is hoe de Administratie in het echt eruit ziet"}
            ]
        elif payload == "/geb19_naar_administratie_464646469898":
            images = [
                {"url": "https://i.imgur.com/mrayVr1.png?1",
                 "text": "De Administratie zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 19. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/LLGPlSc.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om de Administratie te bereiken"},
                {"url": "https://i.imgur.com/zCxTf0t.jpg", "text": "Dit is hoe de Administratie in het echt eruit ziet"}
            ]
        else:
            # Default images if no specific payload matches
            images = []

        # Send each image with its corresponding text as a separate message
        for image_data in images:
            dispatcher.utter_message(text=image_data["text"], image=image_data["url"])

        return []

#6 voor Lok 23

class SendMultipleImages6(Action):
    def name(self) -> Text:
        return "action_send_Lok23_Pics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        payload = tracker.latest_message['text']

        # Define images based on payload
        if payload == "/ingang_tot_lokaal_23_8989":
            images = [
                {"url": "https://i.imgur.com/OtpsXXa.png?1",
                 "text": "Lokaal 23 zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit ingang. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/QCD57gr.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om Lokaal 23 te bereiken"},
                {"url": "https://i.imgur.com/5w4aZOd.jpg", "text": "Dit is hoe Lokaal 23 in het echt eruit ziet"}
            ]
        elif payload == "/geb17_tot_lokaal_23_575757574546":
            images = [
                {"url": "https://i.imgur.com/7IH379G.png?1",
                 "text": "Lokaal 23 zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 17. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/QCD57gr.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om Lokaal 23 te bereiken"},
                {"url": "https://i.imgur.com/5w4aZOd.jpg", "text": "Dit is hoe Lokaal 23 in het echt eruit ziet"}
            ]
        elif payload == "/geb19_tot_lokaal_23_3834949495670":
            images = [
                {"url": "https://i.imgur.com/mrayVr1.png?1",
                 "text": "Lokaal 23 zit in gebouw 16. Dit is de weg naar gebouw 16 vanuit gebouw 19. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
                {"url": "https://i.imgur.com/QCD57gr.png?1",
                 "text": "Indien u al bij gebouw 16 bent aangekomen, kunt u lopen volgens de rode lijn om Lokaal 23 te bereiken"},
                {"url": "https://i.imgur.com/5w4aZOd.jpg", "text": "Dit is hoe Lokaal 23 in het echt eruit ziet"}
            ]
        else:
            # Default images if no specific payload matches
            images = []

        # Send each image with its corresponding text as a separate message
        for image_data in images:
            dispatcher.utter_message(text=image_data["text"], image=image_data["url"])

        return []


class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_name = next(tracker.get_latest_entity_values("name"), None)
        if user_name:
            response = f"Dag {user_name}, waarmee kan ik u vandaag mee helpen?"
        else:
            response = "Hallo! Hoe kan ik u van dienst zijn?"
        dispatcher.utter_message(text=response)
        return []

# 7 Gebouw 16
class SendMultipleImages7(Action):
    def name(self) -> Text:
        return "action_send_Geb16_Pics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        payload = tracker.latest_message['text']

        # Define images based on payload
        if payload == "/find_geb16_from_entrance":
            images = [
                {"url": "https://i.imgur.com/OtpsXXa.png?1",
                 "text": "Dit is de weg naar gebouw 16 vanuit ingang. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},

            ]
        elif payload == "/find_geb16_from_building17-565656":
            images = [
                {"url": "https://i.imgur.com/7IH379G.png?1",
                 "text": "Dit is de weg naar gebouw 16 vanuit gebouw 17. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
            ]
        elif payload == "/find_geb16_van_grbouw19-7878":
            images = [
                {"url": "https://i.imgur.com/mrayVr1.png?1 ",
                 "text": "Dit is de weg naar gebouw 16 vanuit gebouw 19. Volg de rode lijn om gebouw 16 te bereiken"},
                {"url": "https://i.imgur.com/4kpoJR7.jpg", "text": "Zo ziet de voorkant van gebouw 16 eruit"},
            ]
        else:
            # Default images if no specific payload matches
            images = []

        # Send each image with its corresponding text as a separate message
        for image_data in images:
            dispatcher.utter_message(text=image_data["text"], image=image_data["url"])

        return []





