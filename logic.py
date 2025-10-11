from discord import ui,ButtonStyle

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        butonlar= []
        for indeks, cevap in enumerate(self.options):
            if indeks == self.__answer_id:
                butonlar.append(ui.Button(label= cevap, style=ButtonStyle.primary, custom_id=f'correct_{indeks}'))
            else:
                butonlar.append(ui.Button(label= cevap, style=ButtonStyle.primary, custom_id=f'wrong_{indeks}'))
        return butonlar

# Görev 4 - Listeyi sorularınızla doldurun
quiz_questions = [
   Question("Kediler onları kimse görmediğinde ne yapar?", 1, "Uyurlar", "Espri yazarlar"),
   Question("Kediler sevgilerini nasıl ifade ederler?", 0, "Yüksek sesle mırıldanırlar", "Sevimli fotoğraflar", "Havlar"),
   Question("Kediler hangi kitapları okumayı sever?", 3, "Kişisel gelişim kitapları", "Zaman yönetimi: Günde 18 saat nasıl uyunur","Sahibinizden 5 dakika erken uyumanın 101 yolu", "İnsan yönetimi rehberi"),
   Question("Kediler nereye tuvalet yapar?", 0, "Kumlarına", "Klozet","Sahibinin Yatağına", "Balkona")
   ]

