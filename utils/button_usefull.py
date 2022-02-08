from nextcord.ui import Button, View


def button_link_manhwa():
    btn = Button(label="MangeKakalot", url="https://mangakakalot.com/")
    btn2 = Button(label="TopToon",  url="https://toptoon.com/")
    btn3 = Button(label="ManhwaHentai", url="https://manhwahentai.me/")
    view = View()
    view.add_item(btn)
    view.add_item(btn2)
    view.add_item(btn3)
    return view
    
    