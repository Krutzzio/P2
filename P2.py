# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
import time

def Ex1():

    Ip = input("Quin vols que sigui el primer segon del tall?   ")
    N = input("Quan vols que duri el tall?  ")
    command = ["ffmpeg", "-ss", Ip, "-i", "BBB.mp4", "-c", "copy", "-t", N, "BBBcuted.mp4"]
    subprocess.call(command)

    rep = input("Vols reproduir el video (Y/N)\t")
    if (rep == "Y" or rep == "y"):
        com = ["ffplay", "BBBcuted.mp4"]
        subprocess.call(com)

def Ex2():
    command = ["ffmpeg", "-i", "BBBcuted.mp4", "-vf", \
              "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay", "BBBhistoYUV.mp4"]
    subprocess.call(command)

    rep = input("Vols reproduir el video (Y/N)\t")
    if (rep == "Y" or rep == "y"):
        com = ["ffplay", "BBBhistoYUV.mp4"]
        subprocess.call(com)

def Ex3():
    opt = int(input("Quina resolució vols? \n\n\t [1] 720p\n\n\t [2] 480p\n\n\t [3] 360x240\n\n\t [4] 160x1S20p\n\n\t"))

    if(opt == 1):
        #1280x720
        command = ["ffmpeg", "-i", "BBBcuted.mp4", "-s", "1280x720", "-c:a", "copy", "BBB720p.mp4"]
        subprocess.call(command)

    elif(opt == 2):
        #852x480
        command = ["ffmpeg", "-i", "BBBcuted.mp4", "-s", "852x480", "-c:a", "copy", "BBB480p.mp4"]
        subprocess.call(command)

    elif(opt == 3):
        # 360x240
        command = ["ffmpeg", "-i", "BBBcuted.mp4", "-s", "360x240", "-c:a", "copy", "BBB360x240.mp4"]
        subprocess.call(command)

    elif(opt == 4):
        # 160x120
        command = ["ffmpeg", "-i", "BBBcuted.mp4", "-s", "160x120", "-c:a", "copy", "BBB160x120.mp4"]
        subprocess.call(command)
    else:
        print("\nEscull una opció vàlida\n")

    rep = input("Vols reproduir el video (Y/N)\t")
    if (rep == "Y" or rep == "y"):
        if (opt == 1):
            # 1280x720
            com = ["ffplay", "BBB720p.mp4"]
            subprocess.call(com)

        elif (opt == 2):
            # 852x480
            com = ["ffplay", "BBB480p.mp4"]
            subprocess.call(com)

        elif (opt == 3):
            # 360x240
            com = ["ffplay", "BBB360x240.mp4"]
            subprocess.call(com)

        elif (opt == 4):
            # 160x120
            com = ["ffplay", "BBB160x120.mp4"]
            subprocess.call(com)



def Ex4():

    print("\nEs canviarà el canal d'audio de estereo a mono")
    opt = int(input("\nQuin codec vols per el audio:\n\n\t [1] -Alac"
                    "\n\n\t [2] -MP2\n\n\t"))
    command = ["ffmpeg", "-i", "BBBcuted.mp4", "-ac", "1", "BBBAudioMono.mp4"]
    subprocess.call(command)

    if (opt == 1):
        #Alac codec
        command = ["ffmpeg", "-i", "BBBcuted.mp4", "-acodec", "alac", "-vcodec", "copy", "BBBAudioMono.mp4"]
        subprocess.call(command)

    elif (opt == 2):
        # MP2 codec
        command = ["ffmpeg", "-i", "BBBcuted.mp4", "-acodec", "mp2", "-vcodec", "copy", "BBBAudioMono.mp4"]
        subprocess.call(command)

    rep = input("Vols reproduir el video (Y/N)\t")
    if (rep == "Y" or rep == "y"):
        com = ["ffplay", "BBBAudioMono.mp4"]
        subprocess.call(com)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    Option = 0
    fp = 1
    while(Option != 6):
        if(fp == 1):
            Option = int(input("BENVINGUT A LA PRACTICA 2 DE SCAV\n\nSiusplau, selecciona la opció que vulguis"
                               "\n\n\t [1] -Retallar un video"
                   "\n\n\t [2] -Visualitzar els valors YUV de cada frame\n\n\t [3] -Cambiar la resolució del video"
                   "\n\n\t [4] -Canviar el codec i canals del audio \n\n\t [5] -No fer res\n\n\t [6] -Sortir\n\n\t"))

            fp = 0

            if(Option == 1):
                Ex1()
            elif(Option == 2):
                Ex2()
            elif(Option == 3):
                Ex3()
            elif (Option == 4):
                Ex4()
            elif (Option == 5):
                time.sleep(2)
                print("Content?")
                time.sleep(2)
        else:
            Option = int(input("\n\nSiusplau, selecciona la opció que vulguis"
                               "\n\n\t [1] -Retallar un video"
                               "\n\n\t [2] -Visualitzar els valors YUV de cada frame\n\n\t [3] -Cambiar la resolució del video"
                               "\n\n\t [4] -Canviar el codec i canals del audio \n\n\t [5] -No fer res\n\n\t [6] -Sortir\n\n\t"))


            if (Option == 1):
                Ex1()
            elif (Option == 2):
                Ex2()
            elif (Option == 3):
                Ex3()
            elif (Option == 4):
                Ex4()
            elif (Option == 5):
                time.sleep(2)
                print("Content?")
                time.sleep(2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
