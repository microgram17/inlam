import io
#Jag behövde importera io, för att utf-8 skulle fungera ifrån filen. Annars så kunde den inte printa "åäö".
#Jag behövde även skriva med hela pathen för filen, för att jag inte har den på samma plats som kör koden ifrån

with io.open("C:\\Users\\TheIm\\source\\repos\\yh repo\\svenskt_text.txt", mode="r", encoding="utf-8") as file: # här läser jag in filen
    text = file.read() #konverterar filen till en sträng

text = text.lower()#konverterar allting till småbokstäver så att jag slipper ha flera if statements
consonants = "bcdfghjklmnpqrstvwxz"
rövartext = "" # en sträng där jag sparar all "översatt text"

for i in range (0, len(text)): #for loop som itererar för varje element i strängen(filen)
    if text[i] in consonants:#kollar ifall det elementet är en konsonant och ifall den är det så lägger den till konsonanten, ett "o" och sedan konsonanten igen till "rövertext"
        rövartext = rövartext + text[i] + "o" + text[i]
    else:
        rövartext = rövartext + text[i] #ifall det inte är en konsonant, så läggs elementet till vanligt till "rövartext"
        
with open("rövartext.txt", mode="w", encoding="utf-8") as nytextfil:
    nytextfil = nytextfil.write(rövartext)
