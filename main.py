from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from math import pi, sin, cos, tan, asin, acos, log, e

is_deegris = True


Builder.load_file('app.kv')
class main_window(TabbedPanel):   
    def czysc(self):
        self.ids.ramka_1.text = '0'
        self.ids.ramka_2.text = '0'
        self.ids.ramka_3.text = '0'

    def backspace(self):
        if len(self.ids.ramka_1.text) == 1:
            self.ids.ramka_1.text = '0'
            self.ids.ramka_2.text = '0'
            self.ids.ramka_3.text = '0'
        else:
            self.ids.ramka_1.text = self.ids.ramka_1.text[:-1]
            self.ids.ramka_2.text = self.ids.ramka_2.text[:-1]
            self.ids.ramka_3.text = self.ids.ramka_3.text[:-1]
 
    def press_digit(self, znak):
        marks = ("+","-","/","*",".")
        try:
            if self.ids.ramka_1.text == "0" and str(znak) != ".":
                self.ids.ramka_1.text = str(znak)
            elif self.ids.ramka_1.text[-1] in marks and znak in marks:
                pass
            else:
                self.ids.ramka_1.text += str(znak)
        except IndexError:
            pass 

        try:
            if self.ids.ramka_2.text == "0" and str(znak) != ".":
                self.ids.ramka_2.text = str(znak)
            elif self.ids.ramka_2.text[-1] in marks and znak in marks:
                pass
            else:
                self.ids.ramka_2.text += str(znak)
        except IndexError:
            pass 

        try:
            if self.ids.ramka_3.text == "0" and str(znak) != ".":
                self.ids.ramka_3.text = str(znak)
            elif self.ids.ramka_3.text[-1] in marks and znak in marks:
                pass
            else:
                self.ids.ramka_3.text += str(znak)
        except IndexError:
            pass 

    def count(self):
        dzialanie = self.ids.ramka_1.text
        wynik = eval(dzialanie)
        self.ids.ramka_1.text = str(wynik)

    def pierwiastkuj(self):
        liczba = float(self.ids.ramka_3.text)
        wynik = str(liczba**(1/2))
        wynik_lista = wynik.split(".")
        if wynik_lista[1] != "":
            self.ids.ramka_3.text = wynik
        else:
            self.ids.ramka_3.text = wynik_lista[0] 

    def kwadrat(self):
        liczba = float(self.ids.ramka_3.text)
        self.ids.ramka_3.text = str(liczba**2)
    
    def sinus(self):
        dzialanie_sin = self.ids.ramka_2.text
        dzialanie_sin = float(dzialanie_sin)
        if is_deegris == True:
            dzialanie_sin = dzialanie_sin * pi / 180
        wynik_sin = sin(dzialanie_sin)
        wynik_sin = str(wynik_sin)
        self.ids.ramka_2.text = wynik_sin

    def cosinus(self):
        dzialanie_cos = self.ids.ramka_2.text
        dzialanie_cos = float(dzialanie_cos)
        if is_deegris == True:
            dzialanie_cos = dzialanie_cos * pi / 180
        wynik_cos = cos(dzialanie_cos)
        wynik_cos = round(wynik_cos, 2)
        wynik_cos = str(wynik_cos)
        self.ids.ramka_2.text = wynik_cos
        
    def tangens(self):
        dzialanie_tan = self.ids.ramka_2.text
        dzialanie_tan = float(dzialanie_tan)
        if is_deegris == True:
            dzialanie_tan = dzialanie_tan * pi / 180
        wynik_tan = tan(dzialanie_tan)
        wynik_tan = round(wynik_tan, 2)
        wynik_tan = str(wynik_tan)
        self.ids.ramka_2.text = wynik_tan

    def cotangens(self):
        dzialane_cot = self.ids.ramka_2.text
        dzialane_cot = float(dzialane_cot)
        if is_deegris == True:
            dzialane_cot = dzialane_cot * pi / 180
        wynik_cot = 1 / (tan(dzialane_cot))
        wynik_cot = round(wynik_cot, 2)
        wynik_cot = str(wynik_cot)
        self.ids.ramka_2.text = wynik_cot

    def arcus_sinus(self):
        dzialanie_asin = self.ids.ramka_2.text
        dzialanie_asin = float(dzialanie_asin)
        print(dzialanie_asin)
        wynik_asin = asin(dzialanie_asin)
        if is_deegris == True:
            wynik_asin = wynik_asin * 180 / pi
        wynik_asin = round(wynik_asin, 2)
        wynik_asin = str(wynik_asin)
        self.ids.ramka_2.text = wynik_asin

    def arcus_cosinus(self):
        dzialanie_acos = self.ids.ramka_2.text
        dzialanie_acos = float(dzialanie_acos)
        wynik_acos = acos(dzialanie_acos)
        if is_deegris == True:
            wynik_acos = wynik_acos * 180 / pi
        wynik_acos = round(wynik_acos, 2)
        wynik_acos = str(wynik_acos)
        self.ids.ramka_2.text = wynik_acos

    def spinner_clicked(self, value):
        global is_deegris
        value = self.ids.spinner_id.text
        if value == "°":
            is_deegris = True
        if value == "π":
            is_deegris = False


    def logarytm_2(self):
        liczba_1 = self.ids.ramka_3.text
        liczba_1 = float(liczba_1)
        wynik_log2 = log(liczba_1, 2)
        wynik_log2 = str(wynik_log2)
        self.ids.ramka_3.text = wynik_log2

    def logarytm_3(self):
        liczba_1 = self.ids.ramka_3.text
        liczba_1 = float(liczba_1)
        wynik_log3 = log(liczba_1, 3)
        wynik_log3 = str(wynik_log3)
        self.ids.ramka_3.text = wynik_log3

    def logarytm_5(self):
        liczba_1 = self.ids.ramka_3.text
        liczba_1 = float(liczba_1)
        wynik_log5 = log(liczba_1, 5)
        wynik_log5 = str(wynik_log5)
        self.ids.ramka_3.text = wynik_log5

    def logarytm_10 (self):
        liczba_1 = self.ids.ramka_3.text
        liczba_1 = float(liczba_1)
        wynik_log10 = log(liczba_1, 10)
        wynik_log10 = str(wynik_log10)
        self.ids.ramka_3.text = wynik_log10

    def logarytm_e (self):
        liczba_1 = self.ids.ramka_3.text
        liczba_1 = float(liczba_1)
        wynik_log = log(liczba_1, e)
        wynik_log = str(wynik_log)
        self.ids.ramka_3.text = wynik_log


class MyApp(App):
    def build(self):
        return main_window()
    
aplikacja = MyApp()
aplikacja.run()