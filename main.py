import traceback

import request as r
import sender as s
import json

import time

token = {type_token}
main_peer_id = "2000000003"
test_peer_id = "2000000002"

def fol():
    s.send_message(main_peer_id,"Какое нахер дз? К ЕГЭ готовься", token)
def pol():
    s.send_message(main_peer_id, "Исаев Артём Сергеевич", token)

def send_dz():
    response = r.get_history(test_peer_id, token)
    jsos = json.loads(response.content)
    dz = jsos["response"]["items"][0]["text"]
    s.send_message(main_peer_id, dz, token)


while True:
    mes_id = 0
    try:
        response = r.get_history(main_peer_id, token)

        jsos = json.loads(response.content)
        text = jsos["response"]["items"][0]["text"]
        new_mes_id = jsos["response"]["items"][0]["conversation_message_id"]
        if new_mes_id != mes_id:
            if text == "/дзф":
                mes_id = new_mes_id
                s.send_message(test_peer_id, "/дз", token)
                time.sleep(2)
                send_dz()
            if text == "/дзплиз":
                fol()
            if text == "/и":
                pol();
    except Exception as e:

        s.send_message(test_peer_id,"Ошибка: " + traceback.format_exc(),token)

    time.sleep(5)

