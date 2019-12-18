import requests as r

def get_history(peer_id,token):
    response = r.get("https://api.vk.com/method/messages.getHistory?"
                     "count=1&"
                     "peer_id={}&"
                     "v=5.103&"
                     "access_token={}".format(peer_id, token))
    return response