import eel
from pytube import YouTube
import os
from win10toast import ToastNotifier

eel.init('web')

        
@eel.expose
def download_video(url):
    try:
        #преврашаем в список
        url_list = url.split(' ')

        #скачиваем несколько аудио если много ссылок
        for link in url_list:
            yt_video = YouTube(link)
            video = yt_video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video.download('./video')

        #выводим сообщ об успехе
            toas = ToastNotifier()
            toas.show_toast('SUCCESS!',
                            'The Video loaded',
                            icon_path='web/img/logo.ico',
                            duration=2)
        os.startfile('video')
    except Exception:
        #выводим сообщ об ошибке
        toas = ToastNotifier()
        toas.show_toast('The url is not correct',
                        'Please enter a valid link',
                        icon_path='web/img/logo.ico',
                        duration=8)

@eel.expose
def download_audio(url):
    try:
        #преврашаем в список
        url_list = url.split(' ')

        #скачиваем несколько аудио если много ссылок
        for link in url_list:
            yt_audio = YouTube(link)
            audio = yt_audio.streams.filter(only_audio=True).first()
            audio.download('./audio')
            name = yt_audio.title

            #если эти символы есть в имени то удаляем их из имени
            chars = ['$', ',', '"', "'", '?', '|', '%', '.']
            for char in chars:
                name = name.replace(char, '')
            
            #переименовываем файл в audio file
            if os.path.exists(f'audio/{name}.mp4'):
                os.rename('audio/'+ name +'.mp4', 'audio/'+ name +'.mp3')

        #выводим сообщ об успехе
            toas = ToastNotifier()
            toas.show_toast('SUCCESS!',
                            'The Audio loaded',
                            icon_path='web/img/logo.ico',
                            duration=2)
        os.startfile('audio')

    except Exception:
        #выводим сообщ об ошибке
        toas = ToastNotifier()
        toas.show_toast('The url is not correct',
                        'Please enter a valid link',
                        icon_path='web/img/logo.ico',
                        duration=4)

eel.start('index.html', size=(400, 600))