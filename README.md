# 🚢 Den Helder Navigator
 
> **Maritieme routeplanner & bereikanalyse voor Den Helder**  
> Gebouwd met moderne webtechnologieën voor nauwkeurige navigatie en gebiedsanalyse.

 
## 🌐 Live Demo
 
<div align="center">
### 👉 [azahed0.github.io/den-helder](https://azahed0.github.io/den-helder/) 👈
 
</div>
---
 
## ✨ Functies
 
| Functie | Beschrijving |
|---|---|
| 🗺️ **Routeplanning** | Bereken optimale routes tussen meerdere punten |
| ⏱️ **Bereikanalyse** | Visualiseer bereikbaar gebied binnen een ingestelde reistijd |
| 🔍 **Adreszoeker** | Zoek adressen met automatische suggesties |
| 🎨 **Kaartstijlen** | Kies tussen meerdere kaartweergaven |
| 🌙 **Dark mode** | Schakel tussen licht en donker thema |
| 📦 **GeoJSON export** | Download of kopieer route- en bereikdata |
| 📍 **Interactieve markers** | Klik, sleep en herorden routepunten |
| 🔄 **Route omkeren** | Wissel start- en eindpunt met één klik |
 
---
 
## 🛠️ Technologieën
 
| | Technologie | Gebruik |
|---|---|---|
| 🍃 | [Leaflet.js](https://leafletjs.com/) | Interactieve kaartweergave |
| 🛣️ | [OpenRouteService](https://openrouteservice.org/) | Routes & isochronen |
| 📐 | [Turf.js](https://turfjs.org/) | Geografische berekeningen |
| 🔎 | [Nominatim / OSM](https://nominatim.org/) | Adreszoekfunctie |
| ☁️ | [Cloudflare Workers](https://workers.cloudflare.com/) | Serverless proxy |
| 📄 | [GitHub Pages](https://pages.github.com/) | Gratis hosting |
| 🎨 | [Tailwind CSS](https://tailwindcss.com/) | Moderne styling |
| 💪 | [Font Awesome](https://fontawesome.com/) | Iconen |
 
---
 
## 🚀 Lokaal uitvoeren
 
```bash
# 1. Clone de repository
git clone https://github.com/AZahed0/den-helder.git
 
# 2. Open de map
cd den-helder
 
# 3. Open index.html in je browser
open index.html
```
 
> Geen installatie of build-stap vereist.
 
---
 
## 📁 Projectstructuur
 
```
den-helder/
├── 📄 index.html           # Hoofdapplicatie
├── 🐍 inject_key.py        # CI/CD hulpscript
├── 🚫 .gitignore
└── ⚙️ .github/
    └── workflows/
        └── deploy.yml      # Automatische deployment
```
 
---
 
## 🔒 Beveiliging
 
Alle externe API-verzoeken worden veilig verwerkt via een **serverless proxy**.  
De broncode bevat **geen gevoelige gegevens**.
 
---
 
## 🌍 Talen & Tools
 
🟧 HTML5 &nbsp;•&nbsp; 🟨 JavaScript &nbsp;•&nbsp; 🐍 Python &nbsp;•&nbsp; ☁️ Cloudflare &nbsp;•&nbsp; 🐙 GitHub Actions
 
---
 
## 📄 Licentie
 
MIT © [AZahed0](https://github.com/AZahed0) — vrij te gebruiken en aan te passen.
 
