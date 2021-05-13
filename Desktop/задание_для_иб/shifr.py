import base64
import colorama
import time
import cv2
import qrcode
import PIL
from PIL import Image
import PIL.ImageOps   
import pathlib
import os
from colorama import init 
init()

zakrypt = input('Введите ваши данные, они будут зашифрованы: ')

zakrypt = zakrypt.encode('utf-8')

b64kod = base64.b64encode(zakrypt)

b64kod = b64kod.decode('utf-8') 

#itog = open('prom_itog.txt', 'w')
#itog.write(b64kod)

img = qrcode.make(b64kod)
img.save("QR_step_two.jpg", "JPEG")

######

krasota = Image.open('QR_step_two.jpg')

inverted_image = PIL.ImageOps.invert(krasota)

inverted_image.save('QR_ssstep_two.jpg')

udalit = 'C:/Users/FuryAdmin/Desktop/задание_для_иб/QR_step_two.jpg'
os.remove(udalit)

######

im = Image.open("QR_ssstep_two.jpg")
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im.save("QR_petsss_two.jpg")

inverted_image.save('QR_ssstep_two.jpg')

fudalit = 'C:/Users/FuryAdmin/Desktop/задание_для_иб/QR_ssstep_two.jpg'
os.remove(fudalit)

################

img = Image.open('QR_petsss_two.jpg')
width = 64
height = 64
resized_img = img.resize((150, 150), Image.ANTIALIAS)
resized_img.save("testtest.jpg")

img = Image.open('testtest.jpg')
width = 64
height = 64
resized_img = img.resize((150, 150), Image.ANTIALIAS)
resized_img.save("itog.jpg")

dudalit = 'C:/Users/FuryAdmin/Desktop/задание_для_иб/QR_petsss_two.jpg'
os.remove(dudalit)

vandalit = 'C:/Users/FuryAdmin/Desktop/задание_для_иб/testtest.jpg'
os.remove(vandalit)

check = os.path.exists('itog.shifr')
if check == True:
	os.remove("itog.shifr")
else:
	time.sleep(3)

thisFile = "itog.jpg"
base = os.path.splitext(thisFile)[0]

import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import os
root = tk.Tk()

easy = 'mp4'
hard = 'ogg'

path_output = ''
list_format = ['mp4', 'avi', 'mkv']

def f_inp():
    '''
        Диалоговое окно выбора исходных файлов
    '''
    global path_output
    fd = tk.filedialog.askopenfilenames(title = "Выберите нужный файл",
                                        multiple=True)
    if fd:
        txt.config(state = 'normal')
        txt.delete(1.0, 'end')
        for i in fd:
            txt.insert('end', i +'\n')
            if path_output == '':
                path_output = os.path.dirname(i)
        txt.insert('end', '\n' + 'Конец списка' + '\n')
        txt.config(state = 'disable')
        bt_run.config(state = 'normal')


def f_out():
    '''
        Диалоговое окно выбора пути сохранения файлов
    '''
    global path_output
    path_output = tk.filedialog.askdirectory(
                               title = 'Где сохранить зашифрованный файл?')
    txt.config(state = 'normal')
    txt.insert('end', '\n' + 'Сохранить в: ' +'\n' + path_output +'\n')
    txt.config(state = 'disable')

def run():
    '''
        Команда выполнить конвертацию
    '''
    util_path = 'C:/Users/FuryAdmin/Desktop/ffmpeg-N-102494-g2899fb61d2-win64-gpl-shared/bin/ffmpeg.exe'

    if os.path.isfile(util_path):
        for i in txt.get(1.0, 'end').split('\n'):
            if i:
                output_file = (path_output
                               + '/' + os.path.basename(i).rsplit('.', 1)[0]
                               + '.' + list_format_file.get())
                txt.config(state = 'normal')
                txt.tag_add(i, 1.0, 'end')
                txt.tag_config(i, background ='yellow', underline=1)

                try:
                    os.system(util_path + ' -i ' + i +' ' + output_file)
                except:
                    txt.insert('end', '\n' +
                               'Упс! Не удается конвертировать файл: ')
                    txt.insert('end', '\n' + i)
            else:
                break
        txt.insert('end', '\n' + 'Операция завершена')
        txt.config(state = 'disable')


    else:
        txt.config(state = 'normal')
        txt.insert('end', '\n' + 'Не нейден файл "C:\\ffmpeg\\bin\\ffmpeg.exe"')
        txt.insert('end', '\n' + 'Убедитесь, что он доступен.')
        txt.config(state = 'disable')

lb_info = tk.Label(text = 'Выберите нужный файл: ')
lb_info.place(y = 10, x = 10)

bt_input = tk.Button(root, text = '   ...   ', command = f_inp)
bt_input.place(y = 10, x = 235)

txt = tk.Text(width = 70, state = 'disable')
txt.place(y = 80, x = 10)

lb_output = tk.Label(text = 'Где сохранить зашифрованный файл?:')
lb_output.place(y = 10, x = 300)

bt_output = tk.Button(root, text = '   ...   ', command = f_out)
bt_output.place(y = 10, x = 545)


lb_format_info = tk.Label(text = 'Выберите метод шифрования')
lb_format_info.place(y = 40, x = 10)

list_format_file = ttk.Combobox(root,
                                values = [easy, hard],
                                height=3, state = 'readonly')
list_format_file.current(0)
list_format_file.place(y = 40, x = 250)

bt_run = tk.Button(root, text = 'Выполнить', command = run, state = 'disable')
bt_run.place(y = 40, x = 510)


root.geometry('600x500')
root.iconbitmap(default='transparent.ico')
root.title('Encryptor by Arthur Boronenko v0.1 | IS/RO')
root.mainloop()
if __name__ == '__main__':
    pass


os.remove('itog.jpg')
