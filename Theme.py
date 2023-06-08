import math

class M13(Theme):
    discipline = "Математика"
    topic = "ÍÑÄ äâîõ ÷èñåë"
    def realisation(self):
        a = int(myinput("Ââåä³òü îäíå ÷èñëî :"))
        b = int(myinput("Ââåä³òü äðóãå ÷èñëî :"))
        while a * b != 0:
            if a >= b:
                a = a % b
            else:
                b = b % a
        if a<b:
            a=b
        myprint("ÍÑÄ:"+str(a))

class M17(Theme):
    discipline = "Ìàòåìàòèêà"
    topic = "Ñêàëÿðíèé äîáóòîê âåêòîð³â"
    def realisation(self):
        a = int(myinput("Ââåä³òü |a|:"))
        b = int(myinput("Ââåä³òü |b|:"))
        r = int(myinput("Ââåä³òü êóò:"))
        myprint(self.topic+": "+str(a*b*math.cos(r)))

class M21(Theme):
    discipline = "Ìàòåìàòèêà"
    topic = "Äîâæèíà â³äð³çêà"
    def realisation(self):
        x1 = int(myinput("Ââåä³òü x1:"))
        y1 = int(myinput("Ââåä³òü y1:"))
        x2 = int(myinput("Ââåä³òü x2:"))
        y2 = int(myinput("Ââåä³òü y2:"))
        myprint(self.topic+": "+str(((x1-x2)^2+(y1-y2)^2)^0.5))

class M25(Theme):
    discipline = "Ìàòåìàòèêà"
    topic = "Ïëîùà òðàïåö³¿"
    def realisation(self):
        a = int(myinput("Ââåä³òü a:"))
        b = int(myinput("Ââåä³òü b:"))
        h = int(myinput("Ââåä³òü h:"))
        myprint(self.topic+": "+str((a+b)/2*h))

class M29(Theme):
    discipline = "Ìàòåìàòèêà"
    topic = "Öåíòð êîëà çà òðüîìà òî÷êàìè êîëà"
    def realisation(self):
        x1 = int(myinput("Ââåä³òü x1:"))
        y1 = int(myinput("Ââåä³òü y1:"))
        x2 = int(myinput("Ââåä³òü x2:"))
        y2 = int(myinput("Ââåä³òü y2:"))
        x3 = int(myinput("Ââåä³òü x3:"))
        y3 = int(myinput("Ââåä³òü y3:"))
        xc1=(x1+x2)/2
        yc1=(y1+y2)/2
        xc2=(x1+x3)/2
        yc2=(y1+y3)/2
        nx1=x2-x1
        ny1=y2-y1
        nx2=x3-x1
        ny2=y3-y1
        n1=nx1/ny1
        n2=nx2/ny2
        if (n1-n2) == 0:
            n1=n2+1
        y = (n1*yc1-n2*yc2)/(n1-n2)
        x = (nx1*y-nx1*yc1)/ny1+xc1
        myprint("("+str(x)+";"+str(y)+")")

class G33(Theme):
    discipline = "Ãåîãðàô³ÿ"
    topic = "ßêèé îêåàí íàéá³ëüøèé çà ïëîùåþ?"
    def realisation(self):
        myprint("Òèõèé îêåàí")

class G37(Theme):
    discipline = "Ãåîãðàô³ÿ"
    topic = "ßêà äåðæàâà ìàº íàéá³ëüøó ê³ëüê³ñòü îçåð â ñâ³ò³?"
    def realisation(self):
        myprint("Êàíàäà")

class G41(Theme):
    discipline = "Ãåîãðàô³ÿ"
    topic = "Äâ³ äåðæàâè, ÿê³ ìàþòü íàéá³ëüøó ê³ëüê³ñòü âîäîñõîâèù â ñâ³ò³."
    def realisation(self):
        myprint("")

class F50(Theme):
    discipline = "Ô³ëîëîã³ÿ"
    topic = "ßê³ â³äì³íêè º â óêðà¿íñüê³é ìîâ³?"
    def realisation(self):
        myprint("íàçèâíèé, ðîäîâèé, äàâàëüíèé, çíàõ³äíèé, îðóäíèé, ì³ñöåâèé ³ êëè÷íèé")

class T54(Theme):
    discipline = "Ðîáîòà ç òåêñòîì"
    topic = "Äëÿ êîæíîãî ç³ ñë³â òåêñòó ï³äðàõóâàòè, ñê³ëüêè ðàç³â âîíî çóñòð³÷àºòüñÿ ó òåêñò³"
    def realisation(self):
        f1 = myinput("Âêàæ³òü íàçâó âõ³äíîãî ôàéëó")
        f2 = myinput("Âêàæ³òü íàçâó âèõ³äíîãî ôàéëó")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if i not in list2:
                list2.append(i)
        for i in list2:
            file2.write(str(i) + " " + str(list1.count(i))+"\n")

class T58(Theme):
    discipline = "Ðîáîòà ç òåêñòîì"
    topic = "Çíàéòè âñ³ ñëîâà, ùî ì³ñòÿòü ïåâíó ë³òåðó"
    def realisation(self):
        s = myinput("Âêàæ³òü ë³òåðó")
        f1 = myinput("Âêàæ³òü íàçâó âõ³äíîãî ôàéëó")
        f2 = myinput("Âêàæ³òü íàçâó âèõ³äíîãî ôàéëó")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if i not in list2:
                list2.append(i)
        for i in list2:
            if s in i:
                file2.write(str(i)+"\n")

class T62(Theme):
    discipline = "Ðîáîòà ç òåêñòîì"
    topic = "Çíàéòè ê³ëüê³ñòü ñë³â ó òåêñò³"
    def realisation(self):
        f1 = myinput("Âêàæ³òü íàçâó âõ³äíîãî ôàéëó")
        f2 = myinput("Âêàæ³òü íàçâó âèõ³äíîãî ôàéëó")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        file2.write(str(len(list1))+"\n")

class T66(Theme):
    discipline = "Ðîáîòà ç òåêñòîì"
    topic = "Ïåðåâåñòè òåêñò â âåðõí³é ðåã³ñòð"
    def realisation(self):
        f1 = myinput("Âêàæ³òü íàçâó âõ³äíîãî ôàéëó")
        f2 = myinput("Âêàæ³òü íàçâó âèõ³äíîãî ôàéëó")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        s2 = s1.upper()
        file2.write(s2+"\n")

class T70(Theme):
    discipline = "Ðîáîòà ç òåêñòîì"
    topic = "Çíàéòè íàéäîâø³ ñëîâà, ÿê³ ïî÷èíàþòüñÿ ç ãîëîñíî¿ ë³òåðè"
    def realisation(self):
        f1 = myinput("Âêàæ³òü íàçâó âõ³äíîãî ôàéëó")
        f2 = myinput("Âêàæ³òü íàçâó âèõ³äíîãî ôàéëó")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if (i not in list2) and (i[0] in "ÀàÓóÅå²³ÎîªºßÿÈèÞþ¯¿"):
                list2.append(i)
        l = 0
        for i in list2:
            if len(i) > l:
                l = len(i)
        for i in list2:
            if l==len(i):
                file2.write(str(i)+"\n")

class T74(Theme):
    discipline = "Ðîáîòà ç òåêñòîì"
    topic = "Çíàéòè íàéäîâø³ ñëîâà, ÿê³ íå ì³ñòÿòü ãîëîñíèõ ë³òåð"
    def realisation(self):
        f1 = myinput("Âêàæ³òü íàçâó âõ³äíîãî ôàéëó")
        f2 = myinput("Âêàæ³òü íàçâó âèõ³äíîãî ôàéëó")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if i not in list2:
                for j in i:
                    if j not in "ÀàÓóÅå²³ÎîªºßÿÈèÞþ¯¿":
                        list2.append(i)
        l = 0
        for i in list2:
            if len(i) > l:
                l = len(i)
        for i in list2:
            if l == len(i):
                file2.write(str(l) + "\n")

class Z78(Theme):
    discipline = "Çàãàëüí³"
    topic = "Ñê³ëüêè äí³â äî Íîâîãî Ðîêó?"
    def realisation(self):
        start_date = date.today()
        end_date = date(2024,1,1)
        myprint(str((end_date - start_date).days))

class Z82(Theme):
    discipline = "Çàãàëüí³"
    topic = "Ïîãðàòè ó â³äãàäàé ÷èñëî ì³æ 1 òà 10."
    def realisation(self):
        a = randint(1, 10)
        b = myinput("ß çàãàäàâ ÷èñëî ì³æ 1 òà 10. Â³äãàäàé éîãî:")
        if a == b:
            myprint("Ìîëîäåöü")
        else:
            myprint("Íó í³÷îãî")

class Z91(Theme):
    discipline = "Çàãàëüí³"
    topic = "Ïåðåâ³ðêà òàáëè÷êè ìíîæåííÿ"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        ñ = myinput("Ñê³ëüêè áóäå "+str(a)+"*"+str(b)+":")
        if c == a*b:
            myprint("Ìîëîäåöü")
        else:
            myprint("Íó í³÷îãî")

class Z95(Theme):
    discipline = "Çàãàëüí³"
    topic = "Ïåðåâ³ðêà äîäàâàííÿ"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        ñ = myinput("Ñê³ëüêè áóäå "+str(a)+"+"+str(b)+":")
        if c == a+b:
            myprint("Ìîëîäåöü")
        else:
            myprint("Íó í³÷îãî")

class Z99(Theme):
    discipline = "Çàãàëüí³"
    topic = "Ïåðåâ³ðêà â³äí³ìàííÿ"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        ñ = myinput("Ñê³ëüêè áóäå "+str(a)+"-"+str(b)+":")
        if c == a-b:
            myprint("Ìîëîäåöü")
        else:
            myprint("Íó í³÷îãî")

class Z103(Theme):
    discipline = "Çàãàëüí³"
    topic = "Ïîñì³øêà"
    def realisation(self):
        myprint(")")

class Z107(Theme):
    discipline = "Çàãàëüí³"
    topic = """Õòî º âèêîíàâöåì êîìïîçèö³¿ "Call me"?"""
    def realisation(self):
        myprint("Blondie")

class Z111(Theme):
    discipline = "Çàãàëüí³"
    topic = """Ïðèñï³â "Call me" """
    def realisation(self):
        myprint("""Call me (call me) on the line
                Call me, call me any, anytime
                Call me (call me) I'll arrive
                You can call me any day or night
                Call me""")

class Z115(Theme):
    discipline = "Çàãàëüí³"
    topic = "Ñê³ëüêè äí³â ó âèñîêîñíîìó ðîö³?"
    def realisation(self):
        myprint("366")

class Z119(Theme):
    discipline = "Çàãàëüí³"
    topic = "ßê³ º çíàêè çîä³àêó?"
    def realisation(self):
        myprint("Îâåí, Òåëåöü, Áëèçíþêè, Ðàê, Ëåâ, Ä³âà, Òåðåçè, Ñêîðï³îí, Ñòð³ëåöü, Êîçåð³ã,Âîäîë³é, Ðèáè")

