# World of Darkness Wiki Magyarul

[![Netlify Status](https://img.shields.io/badge/deploy-netlify-00C7B7)](https://wod-hu.netlify.app/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/content-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

A **World of Darkness** (Vampire: The Masquerade, Werewolf: The Apocalypse, Mage: The Ascension
és a többi WoD-játékvilág) közösségi, **magyar nyelvű** enciklopédiája. A cél: a
[whitewolf.fandom.com](https://whitewolf.fandom.com) tartalmának strukturált, priorizált fordítása,
amibe bárki csatlakozhat kontributorként.

🔗 **Élő site:** https://wod-hu.netlify.app/

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
- A hosting **[Netlify](https://netlify.com)**. Ha kódot pusholunk a `main` branch-re, Netlify
  automatikusan újraépíti és frissíti az élő site-ot. Emellett minden Pull Requesthez külön,
  ideiglenes előnézeti linket (preview) is generál, így a reviewer megnézheti a kész, renderelt
  eredményt a böngészőben, mielőtt jóváhagyná és mergelné a változást.
- A fordítási munka **GitHub Issues és Pull Requestek** keretében zajlik — lásd [CONTRIBUTING.md](CONTRIBUTING.md).

### Projekt felépítése

```
WOD/
├── .claude/
│   └── skills/
│       └── wod-forditas/        # Claude Code skill: terminológia-kutatási protokoll fordításhoz
│           └── SKILL.md
├── docs/                       # A wiki tartalma — ide kerülnek a Markdown cikkek
│   ├── index.md                # Kezdőlap
│   ├── robots.txt              # Keresőmotor/AI-bot crawler szabályok
│   ├── glosszarium/            # Alapfogalmak (Ölelés, Emberség, Őrjöngés, stb.)
│   ├── vampire-a-maszkabal/     # Vampire: The Masquerade tartalom
│   ├── werewolf-az-apokalipszis/
│   ├── mage-az-eksztazis/
│   ├── wraith-a-feledes/
│   └── changeling-az-almok/
├── scripts/                     # update_stats.py, check_terminology.py, fetch_source.py
├── mkdocs.yml                  # Site konfiguráció (navigáció, SEO beállítások, téma)
├── netlify.toml                 # Netlify build konfiguráció
├── requirements.txt             # Python függőségek (mkdocs, mkdocs-material)
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

## Szkriptek

A projekt minden automatizálása a `scripts/` mappában van, sima Python szkriptként — nincs
rejtett lépés, nincs külső szolgáltatás, amit meg kellene bízni. Ez a lista **minden** szkriptet
felsorol, amit a projekt használ, azzal, hogy pontosan mit csinál és mit **nem** csinál — ez a
közösségi transzparencia miatt fontos: bárki, aki kontribúció előtt ellenőrizni akarja, mit futtat
a gépén, itt megtalálja a teljes listát.

| Szkript | Mit csinál | Mit NEM csinál |
|---|---|---|
| `update_stats.py` | Megszámolja a kész/stúb cikkeket és a hiányzó belső linkeket a `docs/`-ban, beírja a kezdőlap `<!-- STATS:START/END -->` blokkjába. | Nem ír semmilyen más fájlt, nem küld adatot sehova. |
| `fetch_source.py` | Lekéri egy whitewolf.fandom.com cikk nyers wikitext-jét a MediaWiki API-n, és megtisztítja sablonoktól/galériáktól/hivatkozásoktól. | Nem módosít semmit a whitewolf.fandom.com-on (csak olvas), nem ment semmit automatikusan a `docs/`-ba. |
| `lookup_term.py` | A `TERMINOLOGY.md` táblázataiban keres egy szóra (angolul vagy `--hu` kapcsolóval magyarul), kiírja a teljes találati sort forrással. | Nem módosítja a `TERMINOLOGY.md`-t, csak olvas. |
| `check_terminology.py` | Minden `docs/` cikkben megnézi, szerepel-e egy `TERMINOLOGY.md`-ben rögzített angol szó anélkül, hogy a magyar megfelelője is előfordulna a fájlban — ez heurisztika, nem szigorú szabály (márkanevek, tulajdonnevek, duális alakok ki vannak zárva, és automatikusan felismeri az "X: The Y" játékcím-mintát is). | Nem módosít semmit automatikusan — az eredmény emberi átnézésre szánt munkalista. Nincs beépítve a Netlify build-be, mert a hamis pozitívjai blokkolnák a deploy-t. |
| `check_content_map.py` | Összeveti a `CONTENT_MAP.md` táblázataiban hivatkozott fájlutakat a `docs/` valós tartalmával, jelzi, ha egy sor állapota (✅/🟡/🔲) nem egyezik a fájl létezésével. | Nem módosítja a `CONTENT_MAP.md`-t automatikusan. |
| `precommit.py` | Egy parancsban lefuttatja a fenti négy ellenőrzést sorban (`check_terminology.py` → `check_content_map.py` → `update_stats.py` → `mkdocs build --strict`), megáll az első hibánál. **Ezt futtasd commit előtt**, ne a négyet külön-külön. | Nem commitol és nem pushol semmit — csak ellenőriz. |
| `safe_fetch.py` | Lekér egy URL-t sima HTTP GET-tel (böngésző User-Agent-tel), és kiírja/elmenti a **nyers** HTML/szöveg tartalmat, opcionálisan egy `--grep` szűrővel. Azért létezik, hogy kutatás közben ellenőrizhető legyen egy AI-összegzés állítása a tényleges, nyers szerver-válasz ellenében. | Nem rendereli a JavaScript-et (statikus HTML-t lát, nem azt, amit egy böngésző futtatás után mutatna), nem lép be sehova, nem küld semmilyen adatot a megadott URL-en kívül. |
| `fetch_wiki_image.py` | Megkeresi (`--list-for`) és letölti (`--download` + `--out`) egy whitewolf.fandom.com képfájlt a MediaWiki API-n keresztül. Automatikusan észleli és jelzi, ha a Wikia CDN valójában WebP-t szolgál ki `.png`/`.jpg` néven (ezt mi is megtapasztaltuk), és korrigálja a kiterjesztést. | Nem generál automatikusan attribúciót a cikkbe — a forrás-URL-t és licencet kézzel (vagy AI segítségével) be kell írni a képaláírásba, lásd `STRATEGY.md` fair-use mitigációs szabályait. |
| `termlib.py` | Nem önálló szkript — a `check_terminology.py` és `lookup_term.py` közös, megosztott kódja (a `TERMINOLOGY.md` táblázat-elemzése). Nincs önálló futtatási módja. | — |

### Fordítási állapot statisztika

A kezdőlapon (`docs/index.md`) egy automatikusan generált blokk mutatja, hány cikk van kész, hány
stúb, és hány belső link mutat még nem létező cikkre. Ez minden Netlify deploy előtt automatikusan
frissül (`netlify.toml`), de lokálisan is futtathatod `python scripts/update_stats.py`-vel. Új stúb
cikk létrehozásakor tedd be a `status: stub` mezőt a front matterbe — lásd
[CONTRIBUTING.md — Kereszthivatkozások](CONTRIBUTING.md#kereszthivatkozások-stúb-konvenció).

### Claude Code skill a fordításhoz

A `.claude/skills/wod-forditas/SKILL.md` egy Claude Code skill, amely automatikusan betöltődik,
amikor Claude Code-dal (vagy más Claude-alapú eszközzel) cikket fordítasz vagy írsz a `docs/`
mappában. Kodifikálja a terminológiai kutatási protokollt: előbb a `TERMINOLOGY.md`-t nézd át
(`lookup_term.py`-vel), új fogalomnál kövesd a megadott forráskeresési sorrendet (hivatalos kiadás
→ valódi magyar fan-közösség → jelölt, forrás nélküli munkafordítás), és soha ne fogadj el egy
AI-összegzést bejelentkezés-védett vagy üres oldalról `safe_fetch.py`-s ellenőrzés nélkül. Emberi
kontributoroknak is érdemes elolvasni — ugyanaz a munkafolyamat, amit kézzel is követnünk kell.

### Gyors parancsok

```bash
python scripts/lookup_term.py Masquerade        # terminológia gyors kikeresése
python scripts/fetch_source.py "Camarilla (VTM)" --out scratch/camarilla.txt  # forrás lekérése
python scripts/safe_fetch.py "https://url" --grep "keresett-szöveg"           # nyers HTML-ellenőrzés
python scripts/fetch_wiki_image.py --list-for "Brujah"                        # kép-kandidátusok egy cikkhez
python scripts/fetch_wiki_image.py --download "File:ClanBrujahTitleV5.png" --out docs/assets/logos/brujah.webp
python scripts/precommit.py                      # minden ellenőrzés egyben, commit előtt
```

### Automatikus ellenőrzés minden commit előtt (ajánlott, egyszeri beállítás)

A `.githooks/pre-commit` automatikusan lefuttatja a `precommit.py`-t minden commit előtt, ha
`docs/`, `TERMINOLOGY.md` vagy `CONTENT_MAP.md` változott — így nem kell emlékezni rá. Mivel a
git alapértelmezés szerint nem használja a repóban lévő hook-okat, egyszer be kell kapcsolni
(klónozás után):

```bash
git config core.hooksPath .githooks
```

Ezután minden commit előtt automatikusan lefut a terminológia-, `CONTENT_MAP.md`- és build-
ellenőrzés, és megállítja a commitot, ha valami nincs rendben (vagy ha a `check_content_map.py`
automatikusan javított valamit — ilyenkor `git add`-old a módosítást és commitolj újra).

### Mi automatizált, és mi nem (őszintén)

- **Automatikus, build-enként**: a kezdőlap státusz-blokkja (`update_stats.py`), és a
  navigáció (mkdocs most a `docs/` mappastruktúrából generálja, `.pages` fájllal vezérelt
  sorrendben — új cikk automatikusan megjelenik, nincs manuális `mkdocs.yml` szerkesztés).
- **Automatikusan ellenőrzött és részben auto-javított, ha bekapcsolod a git hook-ot**: a
  `CONTENT_MAP.md` állapot-oszlopa (🔲 → ✅ irányban auto-javítva, ✅ → 🔲 irányban csak jelezve,
  sosem auto-javítva — egy hiányzó fájl lehet véletlen törlés, azt ember nézze át).
- **Sosem lesz teljesen automatikus, mert ítélet/kutatás kell hozzá**: a `TERMINOLOGY.md` új
  sorai (egy fogalom fordítását és megbízhatósági szintjét nem lehet a fájlrendszerből
  levezetni), és a `CONTENT_MAP.md` priorizálási megjegyzései.

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
- Terminológia: ahol van hivatalos magyar kiadás (Delta Vision), azt követjük saját fordítás helyett.
- "Setting" → "játékvilág" (nem "szetting") — a magyar RPG-közösség natív szóhasználatát követve.

### [Unreleased] — fordítási munka elindítva

#### Added
- `CONTENT_MAP.md`: konkrét, sorszámozott 1. hullám fordítási lista a Vampire: A Maszkabál
  játékvilághoz (20 tétel, glosszárium → szekták → klánok → mechanika → mellékágak sorrendben).
- Stúb-konvenció dokumentálva a `CONTRIBUTING.md`-ben: kereszthivatkozás egy még nem lefordított
  cikkre mindig egy minimális, `status: stub` front matterrel jelölt stúb oldalt kap, sosem törött
  linket vagy az angol fandom wikire mutató ideiglenes linket.
- Három valódi stúb oldal elkészült mintaként: Kamarilla, Szabbat, Brujah (klán).
- `scripts/update_stats.py`: automatikusan generált fordítási állapot statisztika (kész cikkek,
  stúbok, hiányzó belső linkek száma) a kezdőlapon — minden Netlify deploy előtt frissül.
- `scripts/fetch_source.py`: whitewolf.fandom.com cikkek lekérése és sablon-/hivatkozás-mentes
  megtisztítása fordításhoz, token-/idő-takarékosabb munkafolyamathoz.
- A Kamarilla és a Szabbat cikkek elkészültek teljes terjedelemben (történet, felépítés, kultúra),
  forrás: whitewolf.fandom.com, CC BY-SA attribúcióval.
- `TERMINOLOGY.md`: megerősítve, hogy a "Sect" fogalomra a valódi magyar WoD fan-közösség (két
  független forrás: wodhu.blogspot.com, worldofdarkness.hungarianforum.net) a **"szekta"** szót
  használja — a korábban megfontolt "frakció" saját következtetés volt, nem közösségi forrás.
