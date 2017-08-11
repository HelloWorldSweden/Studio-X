# Sammanfattning Studio X Vecka 32
## Måndag - Algoritmer och datastrukturer
Vi har arbetat med:
- Klasser, listor och läsning från fil
- Abstrakta datastrukturer
- Länkade listor (LinkedList)
- Köer
## Tisdag - Defold med King
* Ladda ned Defold 2 (Pre release version), den har mörkt tema.
* Bra inspiration finns på [Defolds hemsida](https://www.defold.com/)
* Vi arbetade vidare med de länkade listorna och kikade även på binära sökträd
## Onsdag - Säkerhet med Cybercom
* [VMware Workstation Player](https://www.vmware.com/go/tryplayerpro-win-64)
* [Kali linux](https://images.offensive-security.com/virtual-images/Kali-Linux-2017.1-vm-amd64.7z)
* [Vulnerable Web Apps](https://sourceforge.net/projects/vapps/files/VMAppliance/V3/vapps.7z/download)

Datorn kan behöva ha ”Intel VT-x” påslaget i BIOS.
Kali linux och Vulnerable Web Apps ska packas upp med [7-zip](http://www.7-zip.org/a/7z1700-x64.exe) och läggas i en katalog, förslagsvis på skrivbordet.
Ni kommer ha två kataloger när ni har packat upp allt.
 
Första gången vmware startas kommer programmet att begära en e-postadress, en random email funkar utmärkt här, exempelvis dsa@ds.co.
Nästa steg är att öppna upp vmware och lägga till Kali linux och Vulnerable Web Apps i i vmwarelistan.
Detta görs under menyn ”Open a virtual Machine”
 
Testa att starta kali linux och Vulnerable Web Apps.
När Kali och webservern startas första gången kommer en popupruta komma fram. Tryck då på ”I copied it.”
 
För att kontrollera att allting funkar, navigera till ”Vulnerable Web Apps” när datorn är startad.

Logga in med:

**Login för Kali:**
Login: root
Password: toor
 
**Vulnerable Web Apps:**
Login: va
Password: vulnerablewebapps
MySQL:
Login: root
Password: vulnerablewebapps
 
Nu behöver vi ta reda på ip-adressen för webbservern.
Skriv följande i terminalen.
sudo su              lösenordet är vulnerablewebapps
ifconfig

Gå till kalimaskinen och öppna upp Firefox.
Skriv in den funna ip-adressen i webbläsaren.

## Torsdag - Kryptering med Klarna
* Uppgifterna finns på [Google Drive](https://drive.google.com/open?id=0Bxp470g2qYkXVVhXcXFyWXRfOUE)
* Lösningsförslag finns på [GitHub](https://github.com/mikaelsvensson/helloworld-spychallenge)
## Fredag
* Gjorde klart

# Hur går man vidare?
Labbarna är tagna från [Kurs på KTH](https://www.kth.se/social/course/DD1320/subgroup/vt-2017-298/page/laborationer-188/)
De kan ni fortsätta göra. Jag rekommenderar att undersöka:
* Grafer: breddenförstsökning, djupetförstsökning
* Hashtabeller
* Sökning och sortering - bubble sort, binary sort, merge sort
* [Kattis](https://open.kattis.com/) - En domare på webben dit man kan ladda upp lösningar på problem

## Använda Python på webben
* **Flask** är ett bibliotek för att kunna skriva API:er med Python, för att kunna hämta data. Tips är att börja med att lagra information på fil som ni nu kan läsa. För vidare utmaningar läs på om databaser, exempelvis PostgreSQL.
* **Django** är ett ramverk för att göra hela webbplatser