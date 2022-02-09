from nextcord.ui import Button, View
from utils import scrap_blog


def button_link_manhwa():
    btn = Button(label="MangeKakalot", url="https://mangakakalot.com/")
    btn2 = Button(label="TopToon",  url="https://toptoon.com/")
    btn3 = Button(label="ManhwaHentai", url="https://manhwahentai.me/")
    view = View()
    view.add_item(btn)
    view.add_item(btn2)
    view.add_item(btn3)
    return view

def button_read_article():
    btn_ok = Button(label="Oui", emoji="✅")
    btn_nok = Button(label="Non", emoji="❌")
    
    async def btn_ok_callback(interaction):
        article = scrap_blog.blog_discord_last_article()
        await interaction.response.send_message(f"Link Below Oppa : 📰 {article} 📰 ")
        
    async def btn_nok_callback(interaction):
        await interaction.response.send_message(f"No Problem Oppa, SeeYa! 👋")
    
        
    btn_ok.callback = btn_ok_callback
    btn_nok.callback = btn_nok_callback
    
    view = View()
    view.add_item(btn_ok)
    view.add_item(btn_nok)
    return view
    
    