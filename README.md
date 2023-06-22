# **Naziv projekta je Hotel**

## Relacijski model ima 6 tablica (entiteta), a to su:
- Soba, 
- Tip sobe,
- Rezervacija,
- Racun,
- Osoblje,
- Gost.

### _Relacijski model baze podataka implementiran u SQLAlchemy programskom okruženju:_
![REH](reh.png) 
---
## Tehnologije koje su korištene u ovom projektu su:
- Python 
  - programski jezik opće namjene
- Docker 
  - skup platformi kao uslužnih proizvoda koji koriste virtualizaciju na nivou OS za isporuku softvera u paketima koji se nazivaju kontejneri
- Kafka 
  - uz Redis uspješna komunikacija i smanjenje opterećenja na sustav
  - korištena za komunikaciju u stvarnom vremenu
  - može se koristiti za komunikaciju sa više klasa
- MySQL 
  - osigurava trajnost podataka
  - besplatan sustav za upravljanje bazom podataka otvorenog koda.
- Redis 
  - uz Kafku uspješna komunikacija i smanjenje opterećenja na sustav
  - skladište strukture podataka u memoriji, koje se koristi kao distribuirana baza podataka ključ/vrijednost u memoriji, keš i posrednik poruka, s opcionom izdržljivošću
  - vrlo brzo dohvata podatke
  - privremena pohrana podataka
- Flask 
  - uz JQuery tehnologija za rad s podacima u stvarnom vremenu
  - mikro web okvir napisan u Pythonu. Klasifikovan je kao mikrookvir jer ne zahteva posebne alate ili biblioteke.
- JQuery 
  - uz Flask tehnologija za rad s podacima u stvarnom vremenu
  - JavaScript okvir dizajniran da pojednostavi HTML DOM obilazak i manipulaciju stablom, kao i rukovanje događajima, CSS animaciju i Ajax
---
## Cilj projekta je:
- Razvoj sustava baziranih na web tehnologijama za upravljanje podacima u bazi podataka,
- Korištenje Docker tehnologije,
- Razvoj aplikacija korištenjem Docker platforme,
- Korištenje JQuery i Flask tehnologija za rad s podacima u stvarnom vremenu,
- Korištenje Kafka i Redis za uspješnu komunikaciju i smanjenje opterećenja na sustav.

### Za gost su korišteni Kafka i JQuery za komunikaciju u stvarnom vremenu.
---
### Aplikacija kroz MySQL bazu podataka osigurava trajnost podataka, a kroz Redis sustav osigurava cache-ing za brzo dohvaćanje podataka. 
### Za komunikaciju u stvarnom vremenu korištena je Kafka.