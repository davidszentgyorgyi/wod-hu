# Kontribútor útmutató

Köszönjük, hogy segítenél a World of Darkness magyar wiki felépítésében! Ez az útmutató lépésről
lépésre elmagyarázza, hogyan tudsz csatlakozni — akár vagy fejlesztő, akár "csak" fordítani szeretnél
böngészőből, technikai háttér nélkül.

## Tartalomjegyzék

1. [Mit lehet csinálni?](#mit-lehet-csinálni)
2. [Gyors út: fordítás böngészőből, Git nélkül](#gyors-út-fordítás-böngészőből-git-nélkül)
3. [Teljes workflow: lokális fejlesztéssel](#teljes-workflow-lokális-fejlesztéssel)
4. [Terminológiai konvenciók](#terminológiai-konvenciók)
5. [Cikk-sablon és formázási szabályok](#cikk-sablon-és-formázási-szabályok)
6. [Hogyan válassz cikket?](#hogyan-válassz-cikket)
7. [Review folyamat](#review-folyamat)
8. [Viselkedési alapelvek](#viselkedési-alapelvek)

---

## Mit lehet csinálni?

Nem kell programozónak lenni ahhoz, hogy segíts. Néhány példa:

- **Fordítás**: egy angol fandom-wiki cikk magyarra fordítása.
- **Lektorálás**: egy már lefordított cikk nyelvi/tartalmi ellenőrzése.
- **Terminológia**: javaslat egy szakszó magyar megfelelőjére, vita eldöntése.
- **Strukturálás**: új kategória/cikk felvétele a [`CONTENT_MAP.md`](CONTENT_MAP.md) priorizálásba.
- **Technikai fejlesztés**: a MkDocs konfiguráció, design, automatizálás javítása.

## Gyors út: fordítás böngészőből, Git nélkül

Ha nincs kedved/időd Git-et telepíteni, teljesen jó megoldás a böngészős szerkesztés:

1. Nyisd meg a GitHub repót, és navigálj a `docs/` mappában a játékvilághoz, amit fordítani szeretnél
   (pl. `docs/vampire-a-maszkabal/`).
2. Kattints a fordítani kívánt `.md` fájlra (vagy ha még nincs ilyen cikk, egy hasonló meglévőre
   mintaként).
3. Kattints a ceruza ikonra (**"Edit this file"**) a fájl jobb felső sarkában.
4. Szerkeszd a tartalmat a [cikk-sablon](#cikk-sablon-és-formázási-szabályok) szerint.
5. Lapozz le az oldal aljára: a GitHub automatikusan létrehoz neked egy új branch-et és egy
   **Pull Requestet** ("Propose changes" gomb) — nem kell tudnod, mi az a branch, a GitHub intézi.
6. Írj egy rövid leírást, mit fordítottál, és nyomd meg a **"Create pull request"** gombot.
7. Valaki a projektből átnézi, esetleg kér egy-két javítást, majd jóváhagyja — ekkor a fordításod
   automatikusan megjelenik az élő site-on.

## Teljes workflow: lokális fejlesztéssel

Ha szeretnéd lokálisan is látni az eredményt (ajánlott, ha több cikket fordítanál egyszerre):

```bash
# 1. Repó klónozása
git clone https://github.com/davidszentgyorgyi/wod-hu.git
cd wod-hu

# 2. A dev branch-re állunk — minden munka ide kerül, ne dolgozz direktben a main-en
git checkout dev

# 3. Új branch a munkádhoz, a dev-ből kiágazva
git checkout -b forditas/vampire-klanok

# 3. Python környezet + függőségek
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt

# 4. Dev szerver — élőben látod a változást böngészőben
mkdocs serve
# → http://127.0.0.1:8000

# 5. Szerkeszd a docs/ mappában a megfelelő .md fájlt, mentsd el

# 6. Commit és push
git add docs/vampire-a-maszkabal/klanok.md
git commit -m "Vampire klánok cikk fordítása"
git push origin forditas/vampire-klanok

# 7. Nyiss Pull Requestet a GitHub felületén a saját branch-edből a dev-be
#    (NE a main-be — a main csak jóváhagyott, kész állapotot kap)
```

## Terminológiai konvenciók

!!! tip "Claude Code / Claude skill"
    Ha Claude Code-dal (vagy más Claude-alapú eszközzel) dolgozol ebben a repóban, a
    `.claude/skills/wod-forditas/SKILL.md` automatikusan betöltődik, amikor cikket fordítasz —
    ez kodifikálja az alábbi szabályokat és a kutatási protokollt, hogy az AI se találjon ki
    terminológiát megerősítés nélkül.

A World of Darkness tele van visszatérő szakszavakkal, és **van hivatalos magyar kiadása** —
a [Delta Vision](https://www.deltavision.hu) *"Vámpír: A Maszkabál"* címmel jelentette meg a Vampire:
The Masquerade szabálykönyvét (2010, 2023). **Elsődlegesen ezt a hivatalos fordítást követjük**, nem
saját/kitalált megoldást — ez a konzisztencia és a hitelesség miatt fontos.

A **[TERMINOLOGY.md](TERMINOLOGY.md)** tartalmazza a kötelező, forrásokkal alátámasztott
terminológiai táblázatot. A **konzisztencia fontosabb, mint a tökéletes egyéni fordítás** — ha egy
fogalomnak már van rögzített magyar megfelelője a TERMINOLOGY.md-ben vagy a
[Glosszáriumban](docs/glosszarium/index.md), azt használd, még akkor is, ha szerinted lenne jobb
megoldás.

**Szabály új fogalom fordításakor:**

1. Nézd meg, szerepel-e már a [TERMINOLOGY.md](TERMINOLOGY.md)-ben vagy a
   [Glosszáriumban](docs/glosszarium/index.md).
2. Ha nem, nézd meg, van-e hivatalos Delta Vision fordítás rá (ha a Vampire-n kívüli játékvilághoz
   kapcsolódik, előfordulhat, hogy nincs hivatalos magyar kiadás — ezt is jelezd).
3. Javasolj egy fordítást egy `terminológia` Issue-ban vagy a Pull Request leírásában, forrással
   alátámasztva, hogy mások is véleményezhessék.
4. Minden fogalmat így jelölj első előfordulásnál egy cikkben: **Magyar terminus (angol eredeti)** —
   pl. *"Az Ölelés (Embrace) rituáléja során..."*.
5. A klánnevek (Brujah, Toreador, Ventrue stb.) tulajdonnevek, ezeket nem fordítjuk. Más fogalmakra
   viszont, ha van hivatalos magyar fordítás (pl. "Camarilla" → "Kamarilla"), azt kell használni —
   ne hagyd angolul csak azért, mert megszokottabbnak tűnik.

Vitás terminológiai kérdéseket GitHub Issue-ban nyitunk meg, `terminológia` címkével.

## Cikk-sablon és formázási szabályok

Minden cikk `.md` fájl **front matterrel** (YAML fejléc) kezdődik — ez SEO és keresőmotor
szempontból kötelező:

```markdown
---
title: Cikk címe — rövid, kereső-barát
description: >-
  1-2 mondatos összefoglaló, 150-160 karakter. Ez jelenik meg a Google találatokban
  és az AI keresők (ChatGPT, Perplexity) is ezt használják kontextusként.
status: stub  # csak akkor add hozzá, ha ez egy stúb (lásd lejjebb) — kész cikknél hagyd ki
---

# Cikk főcíme (egyezzen meg a title mezővel)

Az első bekezdés legyen egy **önmagában is érthető definíció** — 40-60 szó, ami megválaszolja
"mi ez?" kérdést kontextus nélkül is. Ez segít abban, hogy AI keresőmotorok és a Google is
helyesen idézzék a cikket.

## Alcímek (H2)

A tartalom logikus alcímekre bontva, nem egy hosszú szövegfolyam.

### Mélyebb részletek (H3)

...
```

**Fontos formázási szabályok:**

- Egy `<h1>` / `#` cím legyen a cikkben (a főcím), minden más H2/H3.
- Kerüld a "kattogj ide" típusú linkszövegeket — a link szövege legyen leíró (pl.
  `[a Camarilla szekta](...)`, nem `[ide](...)`).
- Táblázatot használj összehasonlításhoz (pl. klánok diszciplínái), nem hosszú felsorolást.
- Minden képhez adj `alt` szöveget, ami leírja a kép tartalmát.
- Hivatkozz a forrásra, ha egy állítás a whitewolf.fandom.com-ról származik (licenc miatt is
  kötelező, lásd [LICENSE.md](LICENSE.md)).

## Kereszthivatkozások — stúb-konvenció

Egy cikk gyakran hivatkozik olyan fogalomra, amit még nem fordítottunk le (pl. a Brujah klán
cikkében megemlítjük a Kamarillát, de a Kamarilla cikk még nem létezik). Ilyenkor:

1. **Hozz létre egy stúb oldalt** a hivatkozott fogalomnak, ne hagyd linkeletlenül és ne mutass az
   angol fandom wikire. A link soha nem törhet el, és a stúb maga is belépési pont lesz egy
   jövőbeli kontributornak.
2. A stúb tartalma minimum: a cím, a front matter (`title`, `description`), egy 1-2 mondatos,
   önmagában érthető definíció, és egy jelzés, hogy a cikk bővítésre vár.

**Stúb-sablon:**

```markdown
---
title: "Kamarilla — World of Darkness szekta"
description: >-
  A Kamarilla a World of Darkness legnagyobb vámpírszektája, amely a Maszkabál betartását és a
  hagyományos vámpír-társadalmi rendet védi.
---

# Kamarilla

A **Kamarilla** (Camarilla) a legnagyobb és legszervezettebb vámpírszekta a World of Darkness
univerzumban, amely a Maszkabál betartását és a hagyományos vámpír-társadalmi rendet védi.

!!! note "Ez a cikk bővítésre vár"
    Ez egy stúb — csak a legszükségesebb definíciót tartalmazza. Ha szeretnéd bővíteni, nézd meg a
    [CONTENT_MAP.md](CONTENT_MAP.md) priorizálását és a forrást a
    [whitewolf.fandom.com](https://whitewolf.fandom.com)-on.
```

3. Amikor a stúbot bővíti valaki teljes cikké, egyszerűen törli a "bővítésre vár" admonitiont, és a
   link, amit mások már használtak rá, érintetlen marad.

## Hogyan válassz cikket?

A [`CONTENT_MAP.md`](CONTENT_MAP.md) tartalmazza a priorizálási elvet:

1. **Glosszárium / alapfogalmak** — legmagasabb prioritás, ezekre minden más épül.
2. **Setting-struktúra** (klánok, szekták, törzsek, rendek).
3. **Mechanikai fogalmak** (diszciplínák, ajándékok, varázslattípusok).
4. **Mellékvérvonalak, altípusok**.
5. **Karakterek, események, kiadványok** — legalacsonyabb prioritás, de szabadon választható,
   ha valakinek ez a kedvence.

Ha nem tudod, mibe kezdj, nézd meg a GitHub Issues listát `jó-első-kontribúció` címkével, vagy
kérdezz nyugodtan egy Issue-ban.

## Review folyamat

- Minden Pull Request kap egy automatikus **Netlify preview linket** — a reviewer megnézheti a
  renderelt eredményt, mielőtt jóváhagyja.
- Legalább **egy jóváhagyás** szükséges a `main`-be mergeléshez.
- Terminológiai vagy tartalmi vita esetén a Pull Requesten belül, kommentben beszéljük át.

## Viselkedési alapelvek

- Légy türelmes és támogató más kontributorokkal, főleg kezdőkkel.
- A World of Darkness tartalma sötét témákat (erőszak, horror) feszeget — a fordításban tartsuk
  meg a hangulatot, de kerüljük a szükségtelenül explicit megfogalmazást.
- Ha bizonytalan vagy egy fordításban, inkább kérdezz, mint hogy találgatva rossz terminológiát
  vezess be.
