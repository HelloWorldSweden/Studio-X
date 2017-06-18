# Uppgift 2 - Köer
Denna uppgift går ut på att implementera en kö på två olika sätt, först med hjälp av Pythons inbyggda Array och därefter som en länkad lista

```
"Trollkarlen tar ut de tretton spaderna ur leken, håller dem som en
kortlek med baksidan upp och lägger ut dem på följande sätt: Översta
kortet stoppas underst, nästa kort läggs ut med framsidan upp, nästa
kort stoppas underst, nästa kort läggs ut osv.  Till publikens
häpnad kommer korten upp i ordning ess, tvåa, trea...
Utförande: Man ordnar i hemlighet korten enligt följande..."
```
Citatet kommer från Liberg: Trolleri för alla. Uppgiften går ut på att ta reda på kortkonstens hemlighet!
Ni ska därför göra ett program som kan _simulera_ korttricket enligt följande:
```
Vilken ordning ligger korten i? 3 1 4 2 5
De kommer ut i denna ordning: 1 2 3 5 4
```

I denna labb ska ni implementera en kö på två olika sätt. Med den abstrakta datastrukturen kö kan man göra tre saker:
  * enqueue(x)				# stoppa in något sist
  * x = dequeue()			# plocka ut det som står först
  * isEmpty()				# kolla om kön är tom

## 1. Kör en kö med Pythons array
Leta rätt på dokumentationen för Pythons array. 
  * Börja med att importera modulen array med `from array import array`
  * Bestäm vilken typ av data du vill lagra.
  * Skapa en array och experimentera med array-metoderna append, insert, remove och pop. Rita bilder som illustrerar vad metoderna gör. Vilka vill du använda i din enqueue respektive dequeue? 
  * Nu är du redo att skriva din egen klass ArrayQ.
  * Attribut: En array (och ev andra attribut som du vill ha med). Alla attribut ska vara privata.
  * Metoder:  _ _init_ _, enqueue, dequeue och isEmpty (men inga andra metoder).
  * Spara klassen i en egen fil som du kallar ArrayQ.py

## 2. Testa ArrayQ
Prova din kö med följande testprogram:
```
q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
print(x,y)   # 1 2 ska komma ut
```
Spara programmet i en egen fil och importera din kö med `from ArrayQ import ArrayQ`

## 3. Skriv trollkarlsprogrammet
Skriv ett program som simulerar korttricket (se exemplet högst upp)
Inmatningstips är att använda input() för att läsa in hela raden, split() för att dela upp den och int() för att konvertera till heltal. Experimentera sedan med olika inmatade ordningar och se om du kan lista ut i vilken ordning korten ska ligga innan man börjar trolla för att man ska få ut alla tretton i rätt ordning

## 4. LinkedQ - en kö av noder (länkad lista)
Nu ska du istället implementera kön som en länkad lista. Då behövs två nya klasser: _Node_ och _LinkedQ_.  Skriv in bägge klasserna i samma fil: _LinkedQ.py_. Noderna i listan är objekt som vardera innehåller två (privata) attribut: ett värde (value) och en referens till nästa objekt (next).
Själva LinkedQ-klassen ska ha två attribut: first som håller reda på den första noden i kön och last som pekar ut den sista. Använd samma gränssnitt som i uppgift 1:
  * enqueue(x)
  * x = dequeue()
  * isEmpty()
Det är extra knepigt att programmera enqueue(x) eftersom det blir två fall, beroende på om kön är tom eller inte. Rita upp bägge fallen (lådor med pilar) innan du skriver koden!

## 5. Trollkarlsprogrammet med LinkedQ
Ändra din import så du nu istället använder den länkade listan för att simulera trolleritricket. Provkör. Fungerade det? Då har du lyckats implementera den abstrakta datastrukturen kö på två olika sätt.

När allt fungerar som det ska bör du ta en extra titt på koden. Är den kommenterad och begriplig? 

## Frågor
  * Berätta vad array-metoderna append, insert, remove och pop gör, vilka du valt att använda, och varför.
  * Förklara varför attributen ska vara privata.
  * Rita upp hur dina metoder fungerar för bägge implementationerna av kön.
  * Fungerar de två implementationerna likadant? Förklara eventuella skillnader.