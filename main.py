from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from math import pi, sin, cos, tan, asin, acos



Builder.load_file('myapp.kv')
class main_window(TabbedPanel):   
    def czysc(self):
        self.ids.ramka_1.text = '0'
        self.ids.ramka_2.text = '0'

    def backspace(self):
        self.ids.ramka_1.text = self.ids.ramka_1.text[:-1]
        self.ids.ramka_2.text = self.ids.ramka_2.text[:-1]
 
    def press_digit(self, znak):
        numbers = ("0","1","2")
        marks = ("+","-","/","*")
        if self.ids.ramka_1.text == "0":
            self.ids.ramka_1.text = str(znak)
        elif self.ids.ramka_1.text[-1] == numbers and self.ids.ramka_1.text[-1] != marks:
            self.ids.ramka_1.text += str(znak)
        elif self.ids.ramka_1.text[-1] == marks:
            self.ids.ramka_1.text += ""  

        if self.ids.ramka_2.text == "0":
            self.ids.ramka_2.text = str(znak)
        else:
            self.ids.ramka_2.text += str(znak)

    def count(self):
        dzialanie = self.ids.ramka_1.text
        wynik = eval(dzialanie)
        self.ids.ramka_1.text = str(wynik)

    def pierwiastkuj(self):
        liczba = int(self.ids.ramka_1.text)
        wynik = str(liczba**(1/2))
        wynik_lista = wynik.split(".")  #2.0
        if wynik_lista[1] != "0":
            self.ids.ramka_1.text = wynik
        else:
            self.ids.ramka_1.text = wynik_lista[0] 

    def kwadrat(self):
        liczba = int(self.ids.ramka_1.text)
        self.ids.ramka_1.text = str(liczba**2)
    
    def sinus(self):
        dzialanie_sin = self.ids.ramka_2.text
        dzialanie_sin = float(dzialanie_sin)
        dzialanie_sin = dzialanie_sin * pi / 180
        wynik_sin = sin(dzialanie_sin)
        wynik_sin = str(wynik_sin)
        self.ids.ramka_2.text = wynik_sin

    def cosinus(self):
        dzialanie_cos = self.ids.ramka_2.text
        dzialanie_cos = float(dzialanie_cos)
        dzialanie_cos = dzialanie_cos * pi / 180
        wynik_cos = cos(dzialanie_cos)
        wynik_cos = round(wynik_cos, 2)
        wynik_cos = str(wynik_cos)
        self.ids.ramka_2.text = wynik_cos
        
    def tangens(self):
        dzialanie_tan = self.ids.ramka_2.text
        dzialanie_tan = float(dzialanie_tan)
        dzialanie_tan = dzialanie_tan * pi / 180
        wynik_tan = tan(dzialanie_tan)
        wynik_tan = round(wynik_tan, 2)
        wynik_tan = str(wynik_tan)
        self.ids.ramka_2.text = wynik_tan

    def cotangens(self):
        dzialane_cot = self.ids.ramka_2.text
        dzialane_cot = float(dzialane_cot)
        dzialane_cot = dzialane_cot * pi / 180
        wynik_cot = 1 / (tan(dzialane_cot))
        wynik_cot = round(wynik_cot, 2)
        wynik_cot = str(wynik_cot)
        self.ids.ramka_2.text = wynik_cot

    def arcus_sinus(self):
        dzialanie_asin = self.ids.ramka_2.text
        dzialanie_asin = float(dzialanie_asin)
        wynik_asin = asin(dzialanie_asin)
        wynik_asin = wynik_asin * 180 / pi
        wynik_asin = round(wynik_asin)
        wynik_asin = str(wynik_asin)
        self.ids.ramka_2.text = wynik_asin

    def arcus_cosinus(self):
        dzialanie_acos = self.ids.ramka_2.text
        dzialanie_acos = float(dzialanie_acos)
        wynik_acos = asin(dzialanie_acos)
        wynik_acos = wynik_acos * 180 / pi
        wynik_acos = round(wynik_acos)
        wynik_acos = str(wynik_acos)
        self.ids.ramka_2.text = wynik_acos

class MyApp(App):
    def build(self):
        return main_window()
    
aplikacja = MyApp()
aplikacja.run()