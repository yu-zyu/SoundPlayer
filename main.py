from kivy.app import App
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
import os
import glob
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
import sqlite3
from enum import Enum

# デフォルトに使用するフォントを変更する
resource_add_path('./IPAexfont00301')
resource_add_path('./rounded-mgenplus-20150602')

LabelBase.register(DEFAULT_FONT, 'rounded-mgenplus-1c-black.ttf') #日本語が使用できるように日本語フォントを指定する


conn = sqlite3.connect("benri.db")
curs = conn.cursor()
curs.execute('SELECT * FROM tasks')
rows = curs.fetchall()
print(rows[0])


#テーブルの変更を確定
#conn.commit()

#データベースを閉じる
#conn.close()

class Label(Label):
     pass

class FloatLayout(FloatLayout):
    
    count = 0
    soundcount = 0
    sound = []
    soundsarg = glob.glob('Sound\*.mp3')
    S1 = len(soundsarg)
    Sfull = S1
    print("総音源数%d" % Sfull)
    pitch = 1
    volume = 0.5
    soundclone = None
    timer = None
    print(soundsarg)
    print(len(soundsarg))
    flag = 0


    
    #　音楽の再生
    def sounds(self):

        if self.flag == 0 : 
           self.soundclone = SoundLoader.load(self.soundsarg[self.soundcount])
           print("音源数%d" % len(self.soundsarg))
           print("現在の再生中『 %s 』" % self.soundsarg[self.soundcount])
           print(vars(self.soundclone))
           #print(self.sound.__name__)

        elif self.flag == 1:
             self.sound = SoundLoader.load(self.soundsarg2[self.soundcount])
             print("音源数%d" % len(self.soundsarg2))
             print("現在の再生中『 %s 』" % self.soundsarg2[self.soundcount])

        elif self.flag == 2:
             self.sound = SoundLoader.load(self.soundsarg3[self.soundcount])
             print("音源数%d" % len(self.soundsarg3))
             print("現在の再生中『 %s 』" % self.soundsarg3[self.soundcount])

        elif self.flag == 3:
             self.sound = SoundLoader.load(self.soundsarg4[self.soundcount])
             print("音源数%d" % len(self.soundsarg4))
             print("現在の再生中『 %s 』" % self.soundsarg4[self.soundcount])

        elif self.flag == 4:
             self.sound = SoundLoader.load(self.soundsarg5[self.soundcount])
             print("音源数%d" % len(self.soundsarg5))
             print("現在の再生中『 %s 』" % self.soundsarg5[self.soundcount])

        elif self.flag == 5:
             self.sound = SoundLoader.load(self.soundsarg6[self.soundcount])
             print("音源数%d" % len(self.soundsarg6))
             print("現在の再生中『 %s 』" % self.soundsarg6[self.soundcount])

        elif self.flag == 6:
             self.sound = SoundLoader.load(self.soundsarg7[self.soundcount])
             print("音源数%d" % len(self.soundsarg7))
             print("現在の再生中『 %s 』" % self.soundsarg7[self.soundcount])

        elif self.flag == 7:
             self.sound = SoundLoader.load(self.soundsarg8[self.soundcount])
             print("音源数%d" % len(self.soundsarg8))
             print("現在の再生中『 %s 』" % self.soundsarg8[self.soundcount])


        if self.soundclone:
            print("Sound is %.3f seconds" % self.soundclone.length)
            self.soundclone.pitch = self.pitch
            self.soundclone.volume = self.volume
            self.soundclone.play()
            self.soundclone.seek(0.1)
            return self.soundclone

    def script(self):
        if self.flag == 0 :
           r = open('script.txt', 'r')
           no1 = r.readlines()
           str = no1[self.count].replace(",", ",\n")
           str = str.replace("?!", "!")
           str = str.replace("!!!", "!")
           str = str.replace("!", "!\n")
           str = str.replace("?", "?\n")
           str = str.replace(".)", ")\n")
           str = str.replace("...", ".")
           str = str.replace("..", ".")
           str = str.replace(".", ".\n")
           self.ids.LB.text = str
           print("カウント %d " %self.count)
           r.close()
        elif self.flag >= 1:
             str = rows[self.count][1].replace(",", ",\n")
             str = str.replace("?!", "!")
             str = str.replace("!!!", "!")
             str = str.replace("!", "!\n")
             str = str.replace("?", "?\n")
             str = str.replace(".)", ")\n")
             str = str.replace("...", ".")
             str = str.replace("..", ".")
             str = str.replace(".", ".\n")
             str = str.replace(".]", "]\n")
             self.ids.LB.text = str
             print("カウント %d " %self.count)

    def script2(self):
        if self.flag == 0 :
           self.ids.LB.text = ""
           r = open('script.txt', 'r')
           no1 = r.readlines()
           str = no1[self.count+1].replace("、、、", "、")
           str = str.replace("、", "、\n")
           str = str.replace("？！", "！")
           str = str.replace("！！！", "！")
           str = str.replace("！", "！\n")
           str = str.replace("？", "？\n")
           str = str.replace("。。。", "。")
           str = str.replace("。", "。\n")
           self.ids.LB.text += str
           print("カウント %d " %self.count)
           r.close()

        elif self.flag >= 1:
             str = rows[self.count][2].replace("、、、", "、")
             str = str.replace("、", "、\n")
             str = str.replace("？！", "！")
             str = str.replace("！！！", "！")
             str = str.replace("！", "！\n")
             str = str.replace("？", "？\n")
             str = str.replace("。。。", "。")
             str = str.replace("。", "。\n")
             str = str.replace("]", "]\n")
             self.ids.LB.text = str
             print("カウント %d " %self.count)

    def next(self):
        if self.flag == 0 :
           self.ids.LB.text =""
           if len(self.soundsarg)-1 <= self.soundcount:
              self.count = self.count
              self.soundcount = self.soundcount
           else :
              self.count += 2
              self.soundcount += 1
        elif self.flag >= 1:
           self.ids.LB.text =""
           if len(self.soundsarg)-1 <= self.soundcount:
              self.count = self.count
              self.soundcount = self.soundcount
           else :
              self.count += 1
              self.soundcount += 1
           
        print("カウント %d " %self.count)
        print("音源カウント %d " %self.soundcount )

    def Previous(self):
        if self.flag == 0 :
           self.ids.LB.text =""
           if self.count <= 0:
              self.count = 0
           else:
              self.count -= 2
              self.soundcount -= 1
        elif self.flag >= 1:
           self.ids.LB.text =""
           if self.count <= 0:
              self.count = 0
           else:
              self.count -= 1
              self.soundcount -= 1

        print("カウント %d " %self.count)
        print("音源カウント %d " %self.soundcount )

    def PitchP(self):
        self.pitch += 0.1
        print("ピッチ %f " %self.pitch)

    def PitchM(self):
        if self.pitch >= 0.2:
           self.pitch -= 0.1
           print("ピッチ %f " %self.pitch)

    def VolumeP(self):
        if self.volume <= 1.9:
           self.volume += 0.1
           print("音量 %f " %self.volume)

    def VolumeM(self):
        if self.volume >= 0.1:
           self.volume -= 0.1
           print("音量 %f " %self.volume)

    def Change(self,kazu):
           self.flag = kazu
           self.count = kazu
           if kazu == 0:
              self.count = 0
           elif kazu == 1:
              self.count = 0
           elif kazu == 2:
              self.count = 83
           elif kazu == 3:
              self.count = 129
           elif kazu == 4:
              self.count = 140
           elif kazu == 5:
              self.count = 147
           elif kazu == 6:
              self.count = 154
           elif kazu == 7:
              self.count = 161
           self.soundcount = 0
           self.ids.LB.text = ""


#　KVファイルクラスを読む
class kvfile(App):
    def build(self):
        return FloatLayout()



 
if __name__ == "__main__":
    kvfile().run()
