import json
import requests

from userbot import CMD_HELP
from userbot.events import register

TEMPAT = ''


@register(pattern="^.adzan(?: |$)(.*)")
async def get_adzan(adzan):
    if not adzan.text.startswith("."):
        return ""

    if not adzan.pattern_match.group(1):
        LOKASI = TEMPAT
        if not LOKASI:
            await adzan.edit("Please specify a city or a state.")
            return
    else:
        LOKASI = adzan.pattern_match.group(1)

    url = f'http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc'
    request = requests.get(url)
    result = json.loads(request.text)

    if request.status_code != 200:
        await adzan.edit(f"{result['status_description']}")
        return

    tanggal = result["items"][0]["date_for"]
    lokasi = result["query"]
    lokasi2 = result["country"]
    lokasi3 = result["address"]
    lokasi4 = result["state"]

    subuh = result["items"][0]["fajr"]
    syuruk = result["items"][0]["shurooq"]
    zuhur = result["items"][0]["dhuhr"]
    ashar = result["items"][0]["asr"]
    maghrib = result["items"][0]["maghrib"]
    isya = result["items"][0]["isha"]

    textkirim = (f"⏱  **Jadwal Sholat Pada ** `{tanggal}`:\n" +
                 f"`{lokasi} | {lokasi2} | {lokasi3} | {lokasi4}`\n\n" +
                 f"**Subuh :** `{subuh}`\n" +
                 f"**Syuruk :** `{syuruk}`\n" +
                 f"**Zuhur :** `{zuhur}`\n" +
                 f"**Ashar :** `{ashar}`\n" +
                 f"**Maghrib :** `{maghrib}`\n" +
                 f"**Isya :** `{isya}`\n")

    await adzan.edit(textkirim)


@register(pattern="adzan(?: |$)(.*)")
async def ambiladzan(adzan1):
    if 'adzan' in adzan1.raw_text:
        if not adzan1.pattern_match.group(1):
            LOKASI = TEMPAT
            if not LOKASI:
                await adzan1.edit("Please specify a city or a state.")
                return
        else:
            LOKASI = adzan1.pattern_match.group(1)

        url = f'http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc'
        request = requests.get(url)
        result = json.loads(request.text)

        if request.status_code != 200:
            await adzan1.edit(f"{result['status_description']}")
            return

        tanggal = result["items"][0]["date_for"]
        lokasi = result["query"]
        lokasi2 = result["country"]
        lokasi3 = result["address"]
        lokasi4 = result["state"]

        subuh = result["items"][0]["fajr"]
        syuruk = result["items"][0]["shurooq"]
        zuhur = result["items"][0]["dhuhr"]
        ashar = result["items"][0]["asr"]
        maghrib = result["items"][0]["maghrib"]
        isya = result["items"][0]["isha"]

        textkirim = (f"⏱  **Jadwal Sholat Pada ** `{tanggal}`:\n" +
                     f"`{lokasi} | {lokasi2} | {lokasi3} | {lokasi4}`\n\n" +
                     f"**Subuh :** `{subuh}`\n" +
                     f"**Syuruk :** `{syuruk}`\n" +
                     f"**Zuhur :** `{zuhur}`\n" +
                     f"**Ashar :** `{ashar}`\n" +
                     f"**Maghrib :** `{maghrib}`\n" +
                     f"**Isya :** `{isya}`\n")

        await adzan1.reply(textkirim)

@register(pattern="!sholat(?: |$)(.*)")
async def ambiladzan(adzan12):
    if 'sholat' in adzan12.raw_text:
        if not adzan12.pattern_match.group(1):
            LOKASI = TEMPAT
            if not LOKASI:
                await adzan12.edit("Please specify a city or a state.")
                return
        else:
            LOKASI = adzan12.pattern_match.group(1)

        url = f'http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc'
        request = requests.get(url)
        result = json.loads(request.text)

        if request.status_code != 200:
            await adzan12.edit(f"{result['status_description']}")
            return

        tanggal = result["items"][0]["date_for"]
        lokasi = result["query"]
        lokasi2 = result["country"]
        lokasi3 = result["address"]
        lokasi4 = result["state"]

        subuh = result["items"][0]["fajr"]
        syuruk = result["items"][0]["shurooq"]
        zuhur = result["items"][0]["dhuhr"]
        ashar = result["items"][0]["asr"]
        maghrib = result["items"][0]["maghrib"]
        isya = result["items"][0]["isha"]

        textkirim = (f"⏱  **Jadwal Sholat Pada ** `{tanggal}`:\n" +
                         f"`{lokasi} | {lokasi2} | {lokasi3} | {lokasi4}`\n\n" +
                         f"**Subuh :** `{subuh}`\n" +
                         f"**Syuruk :** `{syuruk}`\n" +
                         f"**Zuhur :** `{zuhur}`\n" +
                         f"**Ashar :** `{ashar}`\n" +
                         f"**Maghrib :** `{maghrib}`\n" +
                         f"**Isya :** `{isya}`\n")

        await adzan12.reply(textkirim)

CMD_HELP.update({
        "adzan": ".adzan <city> or .adzan <country>\
        \nUsage: Gets the prayer time for moslem.\n"
    })
