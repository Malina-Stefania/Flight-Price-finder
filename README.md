# Flight Finder

# Descriere

**Flight Finder** este o aplicație Python care caută oferte de zboruri de pe site-ul *TheFlightDeal* folosind web scraping.  
Utilizatorul introduce un oraș de plecare și o destinație, iar aplicația returnează cele mai ieftine zboruri disponibile.

Dacă nu există rezultate exacte, aplicația încearcă automat:
- orașe de plecare similare (origin fallback)
- destinații similare (destination fallback)

# Concepte folosite

Acest proiect este construit pentru a exersa concepte fundamentale din Python:

1. Programare Orientată pe Obiecte (OOP)
- Clasa `Flight` modelează un zbor
- Clasa `SearchEngine` gestionează logica de căutare
- Obiectele permit organizarea clară a datelor

2. Web Scraping
- `requests` este folosit pentru a descărca paginile web
- `BeautifulSoup` parsează HTML-ul
- Datele sunt extrase din structura site-ului *TheFlightDeal*

3. Colecții (Data Structures)
Proiectul folosește intens structuri de date Python:
- **dicționare** → pentru puncte de plecare și prețuri
- **liste** → pentru zboruri și rezultate
