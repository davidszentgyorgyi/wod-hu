# World of Darkness Wiki Magyarul

[![Netlify Status](https://img.shields.io/badge/deploy-netlify-00C7B7)](https://wod-wiki-hu.netlify.app/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/content-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

A **World of Darkness** (Vampire: The Masquerade, Werewolf: The Apocalypse, Mage: The Ascension
és a többi WoD-játékvilág) közösségi, **magyar nyelvű** enciklopédiája. A cél: a
[whitewolf.fandom.com](https://whitewolf.fandom.com) tartalmának strukturált, priorizált fordítása,
amibe bárki csatlakozhat kontributorként.

🔗 **Élő site:** https://wod-wiki-hu.netlify.app/ *(véglegesítés után cserélendő)*

---

## Miért ez a projekt?

A World of Darkness univerzumnak nincs átfogó, minőségi magyar nyelvű forrása. Ez a projekt ezt a
hiányt tölti be: közösségi fordítók, szerkesztők és WoD-ismerők munkájával épül fel, nyíltan,
GitHub-on keresztül.

## Hogy működik a rendszer?

- A tartalom **Markdown fájlokban** él a [`docs/`](docs/) mappában — nincs adatbázis, nincs admin
  felület, maga a git repó a "CMS".
- A site generátor a **[MkDocs Material](https://squidfunk.github.io/mkdocs-material/)**, ami a
  Markdown fájlokból statikus HTML oldalakat épít.
- A hosting **[Netlify](https://netlify.com)** — minden `main` branch-re történő push automatikusan
  újra deployolja az élő site-ot, és minden Pull Request kap egy saját preview linket, hogy a
  reviewer megnézhesse a végeredményt kattogás előtt.
- A fordítási munka **GitHub Issues és Pull Requestek** keretében zajlik — lásd [CONTRIBUTING.md](CONTRIBUTING.md).

### Projekt felépítése

```
WOD/
├── docs/                       # A wiki tartalma — ide kerülnek a Markdown cikkek
│   ├── index.md                # Kezdőlap
│   ├── robots.txt              # Keresőmotor/AI-bot crawler szabályok
│   ├── glosszarium/            # Alapfogalmak (Ölelés, Emberség, Őrjöngés, stb.)
│   ├── vampire-a-maszkabal/     # Vampire: The Masquerade tartalom
│   ├── werewolf-az-apokalipszis/
│   ├── mage-az-eksztazis/
│   ├── wraith-a-feledes/
│   └── changeling-az-almok/
├── mkdocs.yml                  # Site konfiguráció (navigáció, SEO beállítások, téma)
├── netlify.toml                 # Netlify build konfiguráció
├── requirements.txt             # Python függőségek (mkdocs, mkdocs-material)
├── STRATEGY.md                  # Stratégiai döntések és háttér (platform, licenc, monetizáció)
├── CONTENT_MAP.md                # A forrás wiki (whitewolf.fandom.com) feltérképezése, priorizálás
├── TERMINOLOGY.md                 # Kötelező terminológiai táblázat — hivatalos magyar fordítások forrásokkal
└── CONTRIBUTING.md                # Kontribútor útmutató — ERRE KATTINTS, HA SEGÍTENI SZERETNÉL
```

## Gyors start — helyi fejlesztés

```bash
# 1. Python virtuális környezet (ajánlott)
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# 2. Függőségek telepítése
pip install -r requirements.txt

# 3. Lokális dev szerver indítása (élő reload)
mkdocs serve
# → http://127.0.0.1:8000
```

Ha csak egy cikket szeretnél szerkeszteni vagy hozzáadni, **nem kötelező** lokálisan futtatni a
szervert — a GitHub-on keresztül, böngészőből is szerkeszthetsz egy Markdown fájlt és nyithatsz
Pull Requestet. Részletek: [CONTRIBUTING.md](CONTRIBUTING.md).

## Csatlakozás, kontribúció

Minden segítség jól jön: fordítás, lektorálás, terminológiai egységesítés, technikai fejlesztés.
Kezdésként olvasd el a **[CONTRIBUTING.md](CONTRIBUTING.md)** fájlt — ez lépésről lépésre elmagyarázza,
hogyan válassz cikket, hogyan nyiss Pull Requestet, és milyen terminológiai konvenciókat kövess.

A fordítási prioritásokat (mi a sürgős, mi várhat) a **[CONTENT_MAP.md](CONTENT_MAP.md)** tartalmazza.

A kötelező terminológiát (a hivatalos Delta Vision kiadás és a magyar RPG-közösség fordításai
alapján, forrásokkal) a **[TERMINOLOGY.md](TERMINOLOGY.md)** tartalmazza.

## Licenc

A tartalom a [whitewolf.fandom.com](https://whitewolf.fandom.com) World of Darkness Wiki
fordítása/adaptációja, **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)** licenc
alatt — ez azt jelenti, hogy bárki szabadon felhasználhatja és továbbfejlesztheti a tartalmat,
amíg attribúciót ad és azonos licenc alatt tartja. A World of Darkness név és a kapcsolódó
márkanevek a **Paradox Interactive** tulajdonát képezik; ez egy nem hivatalos, közösségi fan-projekt.

---

## Changelog

A projekt verziótörténete. Formátum: [Keep a Changelog](https://keepachangelog.com/hu/1.0.0/) elvei alapján.

### [Unreleased]

#### Added
- Projekt alapstruktúra felépítve: MkDocs Material konfiguráció, Netlify build pipeline.
- `STRATEGY.md` — platform-, licenc- és monetizációs döntések dokumentálva.
- `CONTENT_MAP.md` — forrás wiki (whitewolf.fandom.com) feltérképezve, kategória-struktúra és
  fordítási priorizálási elv rögzítve.
- Kezdő tartalmi sablonok: kezdőlap, glosszárium, Vampire: A Maszkabál szekció.
- SEO/GEO-barát konfiguráció: `robots.txt` AI-crawlerekkel, sitemap generálás, social card plugin,
  strukturált front matter (title/description minden laphoz).
- `.gitignore` és `.env.example` — biztonságos fejlesztési alapok, env fájlok kizárva a verziókezelésből.

- `TERMINOLOGY.md` — kötelező terminológiai táblázat a hivatalos Delta Vision kiadás ("Vámpír: A
  Maszkabál") és magyar RPG-közösségi recenziók (lfg.hu, radavit.blogspot.com) alapján; javítva a
  korábban hibásan használt "Maskara" szót "Maszkabál"-ra.
- `dev` és `main` branch szétválasztva — a fejlesztés `dev`-en zajlik, `main`-re csak explicit
  jóváhagyással kerül kód.

#### Fixed
- Korábban hibás, kitalált terminológia ("Maskara", "Emberiesség", "Dühroham", "Rokon") javítva a
  hivatalos magyar fordításra ("Maszkabál", "Emberség", "Őrjöngés", "Vértestvér") a Glosszáriumban
  és a Vampire: A Maszkabál szekcióban.

#### Decided
- Forrás: [whitewolf.fandom.com](https://whitewolf.fandom.com) (nem a worldofdarkness.fandom.com —
  lásd `CONTENT_MAP.md` indoklást).
- Platform: MkDocs Material (Docusaurus helyett — egynyelvű projektnél alacsonyabb belépési küszöb).
- Monetizáció: hirdetés/donation most, prémium (nem-WoD-IP) eszközök később — részletek `STRATEGY.md`.
- Terminológia: ahol van hivatalos magyar kiadás (Delta Vision), azt követjük saját fordítás helyett.
