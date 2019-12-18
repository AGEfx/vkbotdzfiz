import requests as r
def send_message(peer_id,text,token):
    r.get("https://api.vk.com/method/messages.send?"
          "random_id=0"
          "&peer_id={}"
          "&message={}"
          "&dont_parse_links=0"
          "&disable_mentions=0"
          "&v=5.103&"
          "access_token={}".format(peer_id, text, token))