# 🚢 Den Helder Navigator

Een interactieve maritieme routeplanner en bereikanalyse tool voor Den Helder, gebouwd met Leaflet.js en OpenRouteService.

## 🌐 Live Demo

👉 [https://azahed0.github.io/den-helder/](https://azahed0.github.io/den-helder/)

---

## ✨ Functies

- **Routeplanning** — Bereken routes voor auto, fiets, lopen en vrachtwagen
- **Bereikanalyse (Isochronen)** — Toon welk gebied bereikbaar is binnen een bepaalde reistijd
- **Zoekbalk** — Zoek adressen in Den Helder met automatische suggesties via Nominatim
- **Meerdere kaartstijlen** — CartoDB Positron, Dark en Voyager
- **Dark mode** — Schakel tussen licht en donker thema
- **GeoJSON export** — Download of kopieer route- en bereikdata
- **Interactieve markers** — Klik op de kaart om routepunten toe te voegen, sleep om te verplaatsen

---

## 🛠️ Technologieën

| Technologie | Gebruik |
|---|---|
| [Leaflet.js](https://leafletjs.com/) | Interactieve kaart |
| [OpenRouteService API](https://openrouteservice.org/) | Routes en isochronen |
| [Turf.js](https://turfjs.org/) | Oppervlakteberekening |
| [Nominatim / OSM](https://nominatim.org/) | Adreszoekfunctie |
| [Cloudflare Workers](https://workers.cloudflare.com/) | API proxy (sleutel verborgen) |
| [GitHub Pages](https://pages.github.com/) | Hosting |
| [Tailwind CSS](https://tailwindcss.com/) | Styling |

---

## 🔒 Beveiliging

De OpenRouteService API-sleutel is **niet zichtbaar** in de broncode. Alle API-verzoeken worden via een **Cloudflare Worker proxy** gestuurd, zodat de sleutel veilig op de server blijft.

---

## 🚀 Lokaal uitvoeren

1. Clone de repository:
   ```bash
   git clone https://github.com/AZahed0/den-helder.git
   cd den-helder
   ```

2. Open `index.html` direct in je browser — geen installatie nodig.

> ⚠️ Voor volledige functionaliteit (routes en isochronen) is een actieve Cloudflare Worker proxy vereist.

---

## 📁 Projectstructuur

```
den-helder/
├── index.html              # Hoofdpagina
├── inject_key.py           # Script voor API-sleutelinjectie (CI/CD)
├── .gitignore
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions deployment
```

---

## 📄 Licentie

MIT — vrij te gebruiken en aan te passen.
