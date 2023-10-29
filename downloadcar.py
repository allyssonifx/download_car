from pathlib import Path
import random
import shutil
from time import sleep
import io, requests, urllib.parse, os, zipfile
# import cv2
import pytesseract
# import regex
import unidecode
# import unicodedata


class Download:
    def requisitar_captcha(self,api_key, session, municipio_id):
        captcha = ""
        count = 1
        while(captcha=="" or len(captcha)<5 or len(captcha)>5):
            url_captcha = 'http://www.car.gov.br/publico/municipios/captcha?id={}'.format(municipio_id)
            request_url = session.get(url_captcha)
            img_data = request_url.content
            with open('captcha.png', 'wb') as handler:
                handler.write(img_data)
            with open('captchause.png', 'wb') as handler:
                handler.write(img_data)
            captcha_path = "zuzu"
            
            
            caminho2 = r"C:\\Program Files\\Tesseract-OCR"
            caminho = r"C:\\Users\\allysson.muniz\\AppData\\Local\\Programs\\Tesseract-OCR"
            pytesseract.pytesseract.tesseract_cmd = caminho + r"\\tesseract.exe"
            texto = pytesseract.image_to_string("captchause.png")
            texto = texto.replace(" ","")
            texto = texto.replace("\n","")
            print("TEXTO -->>"+texto+" "+ str(len(texto)))
            captcha = texto
            count += 1
            if count == 300:
                count = 0
                sleep(5)
        
        print("||"+captcha+"||")
        return captcha, captcha_path

    def requisitar_download(self,session, municipio_id, email_string, captcha, captcha_path,cidade):
        try:
            
            captcha, captcha_path = self.requisitar_captcha("barrabas", session, municipio_id)
            email = urllib.parse.quote(email_string)
            print("this is captcha: "+captcha)
            download_url = 'http://www.car.gov.br/publico/municipios/shapefile?municipio%5Bid%5D={}&email={}&captcha={}'.format(municipio_id, email,
                                                                                                                        captcha)
            print(download_url)
            request_url = session.get(download_url, stream=True)
            print(request_url)

        
            
            z = zipfile.ZipFile(io.BytesIO(request_url.content))
            z.extractall('.')
            municipio_id = str(municipio_id)
            cidade =  unidecode.unidecode(cidade)
            cidade = cidade.encode("ascii", "ignore")
            cidade = cidade.decode("utf-8")
            cidade = cidade.replace(" ","_")
            cidade = cidade.lower()
            try:
                os.makedirs('DATA\\'+cidade)
            except:
                pass
            z = zipfile.ZipFile('DATA\\'+cidade+'\\'+cidade+'.zip', 'w', zipfile.ZIP_DEFLATED)
            arquivos = os.listdir("./")
            for c in arquivos:
                print("Baixando...")
                if "zip" in c:
                    z.write(c)
                    os.remove(c)

            z.close()
            print("Download Finalizado!")
            return 0
        except:
            
            print("Error")
            return 1

    def download(self,session, api_key, email_string, municipio_id,cidade):
        captcha, captcha_path, = ["re","zuzu"]
        emails = ['pombo@gmail.com','serraleoa@outlook.com','carmelo123santos@yahoo.com','congodobolero@gmail.com','republicadacerejeira@yahoo.com']
        count = 0
        while(self.requisitar_download(session=session, municipio_id= municipio_id, email_string= email_string, captcha=captcha, captcha_path=captcha_path,cidade=cidade)==1):
            email_string = emails[count]
            count +=1
            if count == len(emails):
                count = 0
            sleep(3)
            
        

    def iniciar(self,codigo,cidade):

        api_key = 0
        email_string = 'email@com'
        #initialize session
        session = requests.Session()
        init_url = 'https://www.car.gov.br/publico/imoveis/index'
        req = session.get(init_url)
        #4214508
        municipios = [codigo]
        [self.download(session, api_key, email_string, municipio_id,cidade) for municipio_id in municipios]

# x = Download()
# x.iniciar(1200013,"Pinda manhâgbá")