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

import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import os
root = tk.Tk()

from_mp4 = 'jpg'
from_ogg = 'png'

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
                               title = 'Где сохранить расшифрованный файл?')
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

lb_output = tk.Label(text = 'Где сохранить расшифрованный файл?:')
lb_output.place(y = 10, x = 300)

bt_output = tk.Button(root, text = '   ...   ', command = f_out)
bt_output.place(y = 10, x = 545)


lb_format_info = tk.Label(text = 'Выберите метод расшифровки')
lb_format_info.place(y = 40, x = 10)

list_format_file = ttk.Combobox(root,
                                values = [from_mp4, from_ogg],
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

if os.path.exists('itog.png'):

	im = Image.open("itog.png")
	im = im.transpose(Image.FLIP_LEFT_RIGHT)

	im.save("QR_petsss_two.png")
	inverted_image.save('itog.png')

	fudalit = 'C:/Users/FuryAdmin/Desktop/задание_для_иб/QR_petsss_two.png'
	os.remove(fudalit)

################

	krasota = Image.open('itog.png')

	inverted_image = PIL.ImageOps.invert(krasota)

	inverted_image.save('itog.png')

	qr_shifr = cv2.imread('itog.png')
	detector = cv2.QRCodeDetector()
	data, bbox, clear_qrcode = detector.detectAndDecode(qr_shifr)
	
	text_iz_qrcoda = data
	datas = open('data.txt', 'w')
	datas.write(text_iz_qrcoda)

	text_iz_qrcoda = text_iz_qrcoda.encode('UTF-8')
	decrypt = base64.b64decode(text_iz_qrcoda)
	decrypt = decrypt.decode('UTF-8')

	if os.path.exists('itog.jpg'):
		os.remove(itog.jpg)

	else:
		print()


######

if os.path.exists('itog.jpg'):

	im = Image.open("itog.jpg")
	im = im.transpose(Image.FLIP_LEFT_RIGHT)
	im.save("QR_petsss_two.jpg")

	inverted_image.save('itog.jpg')

	fudalit = 'C:/Users/FuryAdmin/Desktop/задание_для_иб/QR_petsss_two.jpg'
	os.remove(fudalit)

################

	krasota = Image.open('itog.jpg')

	inverted_image = PIL.ImageOps.invert(krasota)

	inverted_image.save('itog.jpg')

	qr_shifr = cv2.imread('itog.jpg')
	detector = cv2.QRCodeDetector()
	data, bbox, clear_qrcode = detector.detectAndDecode(qr_shifr)
	
	text_iz_qrcoda = data
	datas = open('data.txt', 'w')
	datas.write(text_iz_qrcoda)

	text_iz_qrcoda = text_iz_qrcoda.encode('UTF-8')
	decrypt = base64.b64decode(text_iz_qrcoda)
	decrypt = decrypt.decode('UTF-8')


	if os.path.exists('itog.png'):
		os.remove(itog.png)

	else:
		print()

################
