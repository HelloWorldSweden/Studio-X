# Laboration 3 - Ordträd

**Mål:** implementation av binärt söträd, rekursion, abstraktion.
Laborationens tema är binära sökträd.
- **Första uppgiften** är att skriva en klass för binära sökträd och testa den.
- **Andra uppgiften** är att bygga upp ett sökträd från en fil med svenska ord. Alla dubbletter ska skrivas ut.
- **Tredje uppgiften** är att kolla orden i en engelsk text mot det svenska sökträdet. Finns det några skenbart svenska ord ska dom skrivas ut, men bara den första förekomsten av varje svenskt ord. (För att veta vilka ord man redan hittat sparar man förstås dom i ett extra sökträd.)

### Experiment
Gå in på Liangs [binärträdsanimation](http://www.cs.armstrong.edu/liang/animation/web/BST.html) och gör följande:
- Skapa ett balanserat binärträd med sju noder
- Skriv ut trädet i inorder
- Skriv ut trädet i preorder
- Skriv ut trädet i postorder

## Skriv en klass för binära sökträd
Nu ska du implementera ett binärt sökträd som en klass.
Tänk dig först ett abstrakt binärt sökträd. Eftersom man med Python kan jämföra ord (bokstavsordning) så går det bra att lagra ord i sökträdet, t ex så här:
```
   swedish = Bintree()              # Skapa ett trädobjekt
   swedish.put("gurka")		    # Sortera in "gurka" i trädet	
   - - -
   if "gurka" in swedish:      # Kolla om "gurka" finns i trädet
      - - -
   swedish.write()                  # Skriver alla ord i bokstavsordning
```
Klassen Bintree ska alltså ha tre metoder:
- put(x) som sorterar in x i trädet
- \_\_contains\_\_(x) som kollar om x finns i trädet (anropas av operatorn in)
- write() som skriver ut trädet i inorder
Men i filen bintreeFile.py ska du dessutom definiera tre hjälpfunktioner. När trädobjektets put("gurka") anropas skickar trädet sin rotpekare och det nya ordet till en rekursiv funktion putta som ser till att en ny nod skapas på rätt ställe. Analogt gör de övriga anropen, alltså så här. 
```
class Bintree:
    def __init__(self):
        self.root=None

    def put(self,newvalue):
        self.root=addToTree(self.root,newvalue)

    def __contains__(self,value):
        return exists(self.root,value)

    def write(self):
        printOut(self.root)
        print("\n")
```

Här är klassen slut men sedan kommer definitionerna av funktionerna addToTree, exists och printOut. Trädet ska bara lagra en upplaga av varje objekt som läggs in.
Det finns förstås också en class Node i bintreefilen som innehåller ett värde och två pekare: left och right.
## Andra uppgiften: Bygg träd och skriv ut dubbletter

Nu ska du läsa in ett ord i taget från filen word3.txt och lägga in det ditt binära sökträd. Ord som förekommer flera gånger (dubbletter) ska skrivas ut. 
```
from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")
```

Om du gjort rätt kommer dom dubblettord som spottas ut att bilda ett viktigt budskap.
## Tredje uppgiften: Två binära sökträd med ordlistor
När du nu har ett sökträd med alla svenska trebokstavsord kan du blixtsnabbt kolla om ett givet ord finns med. Du ska nu läsa filen engelska.txt ord för ord och putta in orden i ett annat sökträd. Nu vill du inte ha dubbletterna utskrivna, så kolla först if engelska.exists(...). Om ordet redan fanns gör du ingenting, men om det är nytt ska du också kolla om det råkar finnas som svenskt ord. I så fall ska det skrivas ut på skärmen.
Om du har gjort rätt kommer dom utskrivna orden att bilda ännu ett hemligt budskap!
## Frågor
Efter labben ska du
- kunna rita och berätta hur binärträdet byggs upp,
- visa hur du testat din klass för binära träd,
- förklara varför det går snabbt att söka i ett binärträd,
- förklara idén bakom att ha put som anropar putta, etc
