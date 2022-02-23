# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:40:05 2021

@author: voxies
"""

# ------------- LIBRARIES ------------- #
import speech_recognition as sr #çevrimiçi ve çevrim dışı bir şekilde çalışan konuşma tanıma kütüphanesi
from datetime import datetime #anlık zamanı öğrenmek için
import webbrowser # web browser açmak için
import time #bilgisayrı uyutmak için
from gtts import gTTS #text i ses e çevirmek için
from playsound import playsound#ses dosyasını çalmak için
import random#random bir sayı üretmek için
from random import choice#random bir değer seçmek için
import os#sistem ayarları değiştirmk için
import lxml
from lxml import html#html dosyasını okumak için
import requests #istek göndermek için
import json # json dosyalarını okumak için
import feedparser #hava  durumunu çekmek için
import colorama #terminal ekranını özelleştirmek için
from colorama import Fore, Back, Style #Gerekli dosya ve sabitleri projemize dahil ettiğimize göre kullanım için gerekli init() fonksiyonunun çağırılması için.
import wikipedia
import wolframalpha
import goslate
from textblob import TextBlob
import urllib
from bs4 import BeautifulSoup
from apiclient.discovery import build
import strings
# ------------- LIBRARIES ------------- #

#------------------------------------------------
r=sr.Recognizer()
colorama.init()

#------------------------------------------------
print("""
      Tüm komutları öğrenmek için "komutlar" komutunu kullanabilirsiniz
      """)
      

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.Recognizer:
            speak('sistem çalışmıyor')
        return voice
#------------------------------------------------
        
def speak(string):
    tts = gTTS(string,lang='tr')
    rand=random.randint(1,1000000)
    file= 'ses.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
#------------------------------------------------
def speak_en(string):
    tts = gTTS(string,lang='en')
    rand=random.randint(1,100)
    file= 'ses-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
#------------------------------------------------
def response(voice):
   
    if 'nasılsın' in voice:
        secim = choice(strings.sozler)
        speak(secim)
        print(Fore.GREEN)
        print("Voxistan: "+secim)#
    
    elif "komutlar" in voice:
        print("""
              --KOMUT LİSTESİ--
              -nasılsın
              -fıkra anlat
              -tekerleme
              -hikaye anlat
              -neler yapabilirsin
              -sen kimsin
              -saat kaç
              -arama yap (Google aramaları)
              -youtube (YouTUBE aramaları)
              -hava durumu
              -araştır/hesapla (wolframalpha aramaları)
              -konum bul
              -sistemi kapat (sistemi durdurur)
              """)
    elif "selam" in voice or "merhaba" in voice:
        print(Fore.GREEN)
        speak("Merhaba. Konya Bilim Merkezine Hoşgeldin. Nasılsın?")
    elif "kaç yaşındasın" in voice or "yaşın kaç" in voice or "Yaşın kaç" in voice or "Kaç yaşındasın" in voice:
        print(Fore.GREEN)
        print("Voxistan: 2021 yılında kodlandım, Ve asistan olarak çalışmaya başladım")
        speak("2021 yılında kodlandım, Ve asistan olarak çalışmaya başladım")
           
            
    elif "nerede" in voice or "konum bul" in voice or "Konum bul" in voice or "Nerede" in voice:
        loc = record("Konumunu bulmak istediğin yer nedir?")
        print(Fore.GREEN)
        print("Voxistan: Konumunu bulmak istediğin yer nedir?")
        webbrowser.open_new_tab("https://www.google.com/maps/place/"+loc+"/&amp;")
        print("Voxistan: {} Yerinin konumunu açıyorum.".format(loc))
        speak(loc+"Yerinin Konumunu açıyorum.")
            
    elif 'teşekkür ederim'  in voice:
        print(Fore.GREEN)
        print("Voxistan: ne demek her zaman")
        speak("ne demek her zaman")
    
    elif 'iyiyim' in voice:
        print(Fore.GREEN)
        print("Voxistan: iyi olmana sevindim senin için ne yapabilirim")
        speak("iyi olmana sevindim senin için ne yapabilirim")
    
    elif 'kötüyüm'  in voice:
        secimolumsuz=choice(strings.sozlerOlumsuz)
        print(Fore.GREEN)
        print("Voxistan: "+secimolumsuz)
        speak(secimolumsuz)
        
    elif 'fıkra anlat' in voice:       
        secimfık=choice(strings.fıkralar)
        speak(secimfık)
        print(Fore.GREEN)
        print("Voxistan: "+secimfık)
    
    elif "tekerleme" in voice:
        secimtekerleme=choice(strings.tekerlemeler)
        speak(secimtekerleme)
        print(Fore.GREEN)
        print("Voxistan: "+secimtekerleme)
        
    elif 'Hikaye anlat' in voice:
        secimhikaye=choice(strings.hikayeler)
        speak(secimhikaye)#
        print(Fore.GREEN)
        print("Voxistan: "+secimhikaye)
    
    elif 'Neler yapabilirsin' in voice:
        speak('seninle sohbet edebilirim , saati söyleyebiilirim , hava durumunu söylerim ,senin yerine googleda arama yaparım ,canın sıkıldıysa fıkra anlatabilirim yada hikaye anlatabilirim , youtube dan birşeyler aratabilirim . peki sen ne yapmamı istersin')
        print(Fore.GREEN)
        print('seninle sohbet edebilirim , saati söyleyebilirim , hava durumunu söylerim ,senin yerine googleda arama yaparım ,canın sıkıldıysa fıkra anlatabilirim yada hikaye anlatabilirim , youtube dan birşeyler aratabilirim . peki sen ne yapmamı istersin')

    elif 'Sen kimsin' in voice or 'sen kimsin' in voice:
        print(Fore.GREEN)
        speak('Benim adım Voxistan. Luna ve Venti tarafından Konya Bilim Merkezinde kodlandım. 7 24 çalışıyorum')
        print('Voxistan: Benim adım Voxistan. Luna ve Venti tarafıdan Konya Bilim Merkezinde kodlandım. 7 24 çalışıyorum')
        print(Fore.GREEN)
        print("Voxistan: Daha seninle tanışmadık. Kendini bana tanıtır mısın?")
        speak("Daha seninle tanışmadık. Kendini bana tanıtır mısın?")
        ad = record("Adın ne?")
        print("Voxistan: Tanıştığıma memnun oldum {}. Ben de Voxistan".format(ad))
        speak("tanıştığıma memnun oldum {}. Ben de Voxistan".format(ad))
        
        print(f"Voxistan: Kaç yaşındasın {ad}?")
        age = record(f"Kaç yaşındasın {ad}?")
        if 0<age<=10:
            ch = random.choice(strings.child)
            print(f"Voxistan: {ch} ")
            speak(ch)
            if ch == strings.child[2]:
                job = record("")
                if job != "":
                    print("Voxistan: Vay canına mükemmel bir meslek.")
                    speak("Vay canına mükemmel bir meslek.")
        elif 10<age<=18:
            yn = random.choice(strings.young)
            print(f"Voxistan: {yn} ")
            speak(yn)
        elif 18<age<=30:
            ynpls = random.choice(strings.youngPlus)
            print(f"Voxistan: {ynpls} ")
            speak(ynpls)
        elif 30<age<70:
            adult = strings.adult[0]
            print(f"Voxistan: {adult} ")
            speak(adult)
        else:
            print(f"Voxistan: Hiç {age} yıl yaşayanı görmemiştim. ")
            speak(f"Hiç {age} yıl yaşayanı görmemiştim. ")
            
    elif 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
        print(Fore.GREEN)
        print("Voxistan: "+datetime.now().strftime('%H:%M:%S'))

    elif 'arama yap' in voice:
        search = record('ne aramamı istersin')
        url ='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search+' için bulduğum sonuçlar')
        print(Fore.GREEN)
        print("Voxistan: "+search+' için bulduğum sonuçlar')
    
    elif "YouTube" in voice:
        searchy = record('ne aramamı istersin')   
        urly ='https://www.youtube.com/results?search_query='+searchy
        webbrowser.get().open(urly)
        speak(searchy+' için bulduğum sonuçlar')
        yanit = record("İlk videoyu açmak ister misin")
        print(yanit)
        if yanit == "evet" or yanit == "Evet" or yanit == "aç" or yanit == "Aç" :
            speak("Video Açılıyor")
            print("Voxistan: Video Açılıyor")
            api_key = "AIzaSyCZyrMj2k9a_zQkJMi8xfN6i3ioxvoqUks"
            youtube = build("youtube","v3",developerKey=api_key)           
            try:
                req = youtube.search().list(q=searchy,part="snippet",type="video")           
                res = req.execute()
                ids = []
                for item in res["items"]:
                    ids.append(item["id"]["videoId"])
                firstid = ids[0]
                video = "https://www.youtube.com/watch?v="+firstid
                webbrowser.get().open(video)
            except AttributeError:
                speak("Şu anda videoyu açamıyorum. Lütfen başka bir şey dene.") 
        print(Fore.GREEN)
        print("Voxistan: "+searchy+' için bulduğum sonuçlar')
    
    elif "canının sağlığı" in voice or "Canının sağlığı" in voice:     
        cansagligi=random.choice(strings.cansagligi)
        print(cansagligi)
        speak(cansagligi)
    elif 'hava durumu' in voice:
        city = record("hangi şehir için hava durumunu öğrenmek istiyorsun")
        if city == "":
            city = record("Anlayamadım. Hangi şehir demek istedin.")
        v_city = city
        city = city.upper()
        city = city.replace("Ş","S")
        city = city.replace("İ","I")
        city = city.replace("Ü","U")
        city = city.replace("Ç","C")
        city = city.replace("Ö","O")
        city = city.replace("Ğ","G")
        parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|71100|{}|".format(city))
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        havadetay=parse[4]
        speak(v_city+" için hava"+havadetay+" derece")
        print(Fore.GREEN)
       
        print("Voxistan: "+v_city+" için hava "+ havadetay+" derece")
        
    elif "araştır" in voice or "hesapla" in voice:
        question = record('ne öğrenmek istersin')
        try:
            blob = TextBlob(question)
            b = blob.translate(to='en')
        except:
            pass
        app_id = "WHTYET-7XAYUHG379"
        client = wolframalpha.Client(app_id)
        try:
            res = client.query(b)
            answer = next(res.results).text
            try:
                blob = TextBlob(answer)
                a = blob.translate(to='tr')
            except:
                pass
            a=str(a)
            speak(a)
        except:
            speak("Araştırmalarımda bunu bulamadım.")
    
    elif "selamınaleyküm" in voice or "selamünaleyküm" in voice or "Selamınaleyküm" in voice or "Selamünaleyküm" in voice:
        print("Voxistan: Aleyküm Selam")
        speak("Aleyküm Selam")
    elif "film öner" in voice or "bana bir film söyle" in voice or "Bana bir film söyle" in voice:
        url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "lxml")
        top_250 = soup.find("tbody",attrs={"class":"lister-list"}).find_all("tr")
        film_sira = 1
        ad = []
        for film in top_250:
            adi = film.find("td",attrs={"class":"titleColumn"}).a.text    
            ad.append(adi)
        tr=[]
        print("Voxistan: İşte senin için bir film.")
        speak("İşte senin için bir film.")
        film = random.choice(ad)
        print("Voxistan: {}".format(film))
        speak_en(film)
    elif 'kendini kapat' in voice or 'sistemi durdur' in voice:
        speak('görüşürüz')
        print(Fore.GREEN)
        print('Voxistan: görüşürüz')
        exit()
time.sleep(1)

# while True:
#     voice=record()
#     voice = voice.lower()
#     if "selam" in voice:
#         n = 1
#         break
    
while 1:
    speak("Oooo Mustafa Bey Hoş Geldiniz Efenim. Sıhattesiniz inşallah")
    speak("""Başak bi sus be kadın be bi sus be
          """)
    voice=record()
    voice = voice.lower()
    print(Fore.BLUE)
    print(voice)
    response(voice)
    print(Fore.GREEN)
    istek = random.choice(strings.istek)
    if voice!= "":
        print(istek)
        speak(istek)
    
    if "güle güle" in voice or "hoşça kal" in voice :
        break
    