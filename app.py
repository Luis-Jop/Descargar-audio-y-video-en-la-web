from flask import Flask, render_template, request
#pytube es una biblioteca de Python para descargar videos desde Youtube
from pytube import YouTube
#El módulo os en Python proporciona los detalles y la funcionalidad del sistema operativo.
import os

#E Modulo pathlib sirve para manipular las rutas de sistemas de archivos
from pathlib import Path

#Declarando nombre de la aplicación e inicializando
app = Flask(__name__)


#Creando un Decorador
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('pagina.html')



@app.route("/submit", methods=['GET', 'POST'])
def descargarVideo():
    if request.method == 'POST':
        urlVideo              = request.form['urlVideo']
        videoYT = YouTube(urlVideo)

        if  request.form['submit_btn'] == 'boton1':
         path   = "Downloads" #Downloads, Documentos, Videos
         folder = "VideosYT"
         #Directorio para almacenar las descargas
         url_Descargas = str(Path.home() / path)
         print(url_Descargas) #C:\Users\urian\Documentos
         print(Path.home()) #C:\Users\urian
        
        #Descarga el video y lo guardo en "VideosYT" dentro de la carpeta de descargas
        
         videoYT.streams.get_highest_resolution().download(output_path=os.path.join(url_Descargas, folder))
         titulo=print(f"Titulo .........: {videoYT.title}")
         print(videoYT)
        
         return render_template('pagina.html')
        elif request.form['submit_btn'] == 'boton2':
            path   = "Downloads"
 #Downloads, Documentos, Videos
        folder = "MusicaYT"
 #Directorio para almacenar las descargas
        url_Descargas = str(Path.home() / path)
        print(url_Descargas) #C:\Users\urian\Documentos
        print(Path.home()) #C:\Users\uria

#Download mp3
        yt = YouTube(urlVideo)
        audio_file = yt.streams.filter(only_audio=True).first().download(output_path=os.path.join(url_Descargas, folder))
        base, ext = os.path.splitext(audio_file)
        new_file = base + '.mp3'
        os.rename(audio_file, new_file)
        
        print(f"se descargo en ....: {url_Descargas}")
        name=  print(f"Titulo .........: {yt.title}")
        print(f"Titulo .........: {yt.title}")
        print(f"Duracion (seg)..: {yt.length}")
        print(f"Descripcion.....: {yt.description}")
        return render_template('pagina.html')

    else:
        return render_template('pagina.html')

    
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return render_template('pagina.html')


if __name__ == '__main__':
    app.run()