from PySimpleGUI import PySimpleGUI as sg
from PIL import Image, ImageTk
import os
import ctypes

user32 = ctypes.windll.user32
height, width = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
side = int(width*3/4)    
size = (side , side)

imglocation = {
    1 : '1 - Ano do Unicórnio.png',
    2 : '2 - Ano do Centauro.png',
    3 : '3 - Ano do Pégaso.png',
    4 : '4 - Ano do Sátiro.png',
    5 : '5 - Ano do Kraken.png',
    6 : '6 - Ano do Pesadelo.png',
    7 : '7 - Ano do Oni.png',
    0 : '8 - Ano do Azer.png'
}

def tryImage():
    im = Image.open('imgs/'+imglocation[1])
    im.show()

def resizedimg(img):
   im = Image.open(img)
   im = im.resize(size=size)
   im = ImageTk.PhotoImage(image=im)
   return im 
                

def calculate_horoscopo(ano):
    return ano % 8


   

def main():
    display = calculate_horoscopo(1)
    sg.theme('Dark Blue 3')
    layout = [[sg.Text("Ano:"), sg.Input(key="ano", enable_events=True, size = (10, 120))],
          [sg.Image(key = '-image', size=size)]
          ]
    window = sg.Window("Constelações",layout, finalize = True)
    image = resizedimg('imgs/1 - Ano do Unicórnio.png')
    window['-image'].update(data=image)
    
    while True:
        event, values = window.read()
            
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'ano':
            try:
                display = calculate_horoscopo(int(values['ano']))
            except:
                display = calculate_horoscopo(1) 
            path = 'imgs/' + imglocation[display]    
            image = resizedimg(path)
            window['-image'].update(data=image)
                
            
        
    
if __name__ == '__main__':
    main()
   