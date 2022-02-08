
import requests


def waifu_sfw():
    res = requests.get("https://api.waifu.pics/sfw/waifu")
    print(res.status_code)
    return res.status_code