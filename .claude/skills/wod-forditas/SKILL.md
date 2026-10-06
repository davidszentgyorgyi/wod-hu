---
name: wod-forditas
description: Használd, amikor a World of Darkness magyar wiki (wod-hu) projektben cikket fordítasz, írsz vagy szerkesztesz a docs/ mappában. Célja a terminológiai konzisztencia: a TERMINOLOGY.md-ben rögzített fordítások követése, és új fogalom esetén a megfelelő kutatási protokoll lefuttatása, mielőtt bármit kitalálnál.
---

# WoD fordítási munkafolyamat

Ez a skill a World of Darkness magyar wiki (wod-hu) projekt kontribútori munkafolyamatát
kodifikálja. Mindig ezt kövesd, amikor a `docs/` alatt cikket írsz, fordítasz, vagy bővítesz.

## 0. Először olvasd el ezeket

- `TERMINOLOGY.md` — a kötelező terminológiai táblázat, forrásokkal és megbízhatósági szinttel.
- `CONTENT_MAP.md` — mi van már kész, mi a prioritás.
- `CONTRIBUTING.md` — cikk-sablon, stúb-konvenció, formázási szabályok.

Soha ne találj ki fordítást egy fogalomra, ami már szerepel a `TERMINOLOGY.md`-ben — azt kell
használni, még akkor is, ha szerinted lenne jobb megoldás.

## 1. Ha egy fogalom MÁR szerepel a TERMINOLOGY.md-ben

Ne grep-elj kézzel — használd a lookup szkriptet:

```bash
python scripts/lookup_term.py Masquerade
python scripts/lookup_term.py --hu Maszkabál   # fordított irányban, magyar szóra keresve
```

Ha van találat, használd azt a fordítást, pontosan úgy, ahogy rögzítve van (beleértve a
"fordítatlan, tulajdonnévként kezelve" döntéseket is — pl. Caitiff, Ghoul, Auspex nem
fordítjuk). Ha nincs találat, a szkript 1-es exit kóddal tér vissza, és emlékeztet a 2. pontra.

## 2. Ha egy fogalom MÉG NEM szerepel a TERMINOLOGY.md-ben — kutatási protokoll

Ne találj ki fordítást megerősítés nélkül. Kövesd ezt a sorrendet:

1. **Hivatalos magyar kiadás ellenőrzése.** A World of Darkness-nek van hivatalos magyar
   kiadása (Delta Vision, "Vámpír: A Maszkabál", 2010/2023) — csak a Vampire-vonalhoz. Ha a
   fogalom ebből a vonalból van, keress rá a Delta Vision oldalán
   (deltavision.hu) és termékleírásokban.
2. **Valódi magyar fan-közösségi forrás keresése.** Lásd lejjebb a **"Forrás-playbook
   játékvonalanként"** szekciót — ott van feljegyezve, melyik forrás melyik vonalhoz
   bizonyult hasznosnak eddig. Ha ott nincs elég, induló lista:
   - [lfg.hu](https://lfg.hu) — magyar szerepjátékos közösségi oldal, van V5 ismertető cikke
   - [radavit.blogspot.com](https://radavit.blogspot.com) — V5 ismertető
   - [wodhu.blogspot.com](https://wodhu.blogspot.com) — magyar WoD fan blog
   - [worldofdarkness.hungarianforum.net](https://worldofdarkness.hungarianforum.net) — aktív
     magyar WoD szerepjátékos fórum
   - Ha ezek nem elegendők, végezz új keresést hasonló magyar RPG-fórumokra, blogokra.
3. **KRITIKUS SZABÁLY — sose bízz AI-összegzésben bejelentkezés-védett vagy üres oldalról.**
   Ha egy forrás (pl. fórum-alkategória) tartalmát WebFetch-csel kéred le, és az eredmény
   gyanúsan részletes vagy "túl jó", **ellenőrizd a `scripts/safe_fetch.py`-vel**, hogy a
   tartalom valóban létezik, nem pedig az összegző modell találta ki. Ez már egyszer
   megtörtént ezen a projekten (lásd TERMINOLOGY.md figyelmeztetését) — egy
   bejelentkezés-képernyőt mutató oldalról a modell részletes alkategória-listát "olvasott ki",
   amit nem is látott. Minta ellenőrzésre:
   ```bash
   python scripts/safe_fetch.py "https://forum-url/" --grep "keresett-szlug"
   ```
   Ha nincs találat, az erős jel, hogy az AI-összegzés hallucinált.
4. **Legalább 2 egymástól független forrás egyezése esetén** jelöld a fordítást
   **"Megerősített"**-ként a `TERMINOLOGY.md`-ben, idézettel és linkkel.
5. **Ha nincs forrás, vagy csak egy van:** jelöld **"Döntés, nincs közvetlen forrás"**-ként —
   ez azt jelenti, hogy saját munkafordítást használsz, de ezt a cikkben is jelezni kell egy
   `!!! warning "Terminológia megjegyzés"` admonitionnal.
6. **Ha semmit nem találsz:** ne találj ki semmit — vedd fel a "Még nyitott / tisztázandó
   terminusok" listára a `TERMINOLOGY.md`-ben, és hagyd a fogalmat angolul a cikkben, jelezve a
   bizonytalanságot.

## 3. Soha ne fordítsd le ezeket (állandó lista)

- **Klánnevek** (Brujah, Toreador, Ventrue, Malkavian, Gangrel, Tremere, Lasombra, Tzimisce,
  Banu Haqim, Ravnos, Salubri) — tulajdonnevek.
- **Szervezeti/rang-címek** (Prince, Primogen, Justicar, Archon, ductus, Regent, Cardinal,
  Priscus, Consistory, regnant, antitribu) — kivéve ahol van egyértelmű, rövid magyar glossza:
  Prince → "Herceg", Archbishop → "Érsek", Inner Circle → "Belső Kör".
- **Márkanevek/cím-részek** futó szövegben: "World of Darkness", "Vampire: The Masquerade",
  "Wraith: The Oblivion" stb. — ne cseréld ki "Sötétség Világára" minden előfordulásnál, csak
  ha kifejezetten a hivatalos magyar nevet mutatod be egyszer, zárójelben.
- **Latin/idegen eredetű szakszavak**, amiket a magyar közösség is fordítatlanul használ:
  Caitiff, Ghoul, Auspex.

### Konkrét, megerősített döntések, amiket emlékezz

- **"Sect" → "Szekta"** (nem "frakció") — két független forrás szerint.
- **"Setting" → "Játékvilág"** (nem "szetting") — a magyar közösség a "világ" szót használja.
- **Werewolf → Vérfarkas, Wraith → Lidérc** (NEM "Szellem"!), **Mage → Mágus**, **Changeling →
  Tündér** (NEM "tünde/tündék" — az a Tolkien "Elf" fordítása, más szó!).

## 4. Forrás-playbook játékvonalanként

Ez azt mutatja, meddig jutottunk minden vonal terminológiai kutatásában — frissítsd, ha tovább
jutsz valamelyikben.

| Játékvonal | Állapot | Mit próbáltunk, mi működött |
|---|---|---|
| **Vampire: The Masquerade** | Jól lefedett | Delta Vision hivatalos kiadás + lfg.hu + radavit.blogspot.com + worldofdarkness.hungarianforum.net + wodhu.blogspot.com — mind megegyeztek a fő fogalmakban. |
| **Werewolf: The Apocalypse** | Csak a kreatúra-név megerősített ("Vérfarkas") | worldofdarkness.hungarianforum.net felhasználói csoport-neve megerősítve. Mélyebb fogalmak (Tribe, Gift, Rage, Umbra) még nincsenek forrásolva — nincs tudott magyar kiadás vagy részletes fan-tartalom. |
| **Mage: The Ascension** | Csak a kreatúra-név megerősített ("Mágus") | Ugyanaz a forrás, csak a csoportnév. A mélyebb Mage-alfórum tartalma bejelentkezés-védett volt, NEM ellenőrizhető — ne bízz a korábbi (törölt) "Tradíciók/Martalócok/Nefandusok/Technokraták" infóban, az hallucináció volt. |
| **Wraith: The Oblivion** | Csak a kreatúra-név megerősített ("Lidérc") | Ugyanaz a forrás. Ez volt az első helyes korrekció — korábban hibásan "Szellem"-et használtunk. |
| **Changeling: The Dreaming** | Csak a kreatúra-név megerősített ("Tündér") | Ugyanaz a forrás. Korábban hibásan "tünde/tündék"-et használtunk (az Tolkien "Elf" fordítása) — javítva. |
| **Hunter: The Reckoning** | Csak a kreatúra-név megerősített ("Vadász"), van bevezető cikk | `docs/hunter-a-leszamolas/index.md` — a mélyebb fogalmak (Imbue, Edges, Creed) még nincsenek forrásolva. |
| **Demon: The Fallen** | Csak a kreatúra-név megerősített ("Bukott"), van bevezető cikk | `docs/demon-a-bukottak/index.md` — a mélyebb fogalmak (Faction, Lore, Torment) még nincsenek forrásolva. |

Ha regisztrálsz a worldofdarkness.hungarianforum.net-re és hozzáférsz a tényleges
fajleírás-tartalmához (nem csak a bejelentkezési képernyőhöz), az nagyon értékes további forrás
lenne — frissítsd ezt a táblázatot, ha sikerül.

## 5. Stílus és hangnem

- **Terjedelem**: egy átlagos cikk 150-350 szó. Nem kell (és nem is kell törekedni) teljes
  fandom.com-cikk-hosszúságú fordításra egyben — inkább egy tömör, önálló definíció + 2-4
  tematikus alcím, mint egy végtelenül hosszú, de féligkész cikk.
- **Hangnem**: enciklopédikus, tömör, jelen idő. Ne légy "lelkesen népszerűsítő" vagy
  "sztorizó" — ez egy wiki, nem egy blogbejegyzés vagy marketingszöveg.
- **Első bekezdés mindig önmagában érthető** legyen, kontextus nélkül is — ez segít a
  keresőmotoroknak és AI-asszisztenseknek is helyesen idézni a cikket (lásd a projekt
  SEO/GEO-elveit).
- **Ne ismételd a forrást szóról szóra** — a CC BY-SA licenc engedi az adaptációt/fordítást,
  de ez egy saját, magyar nyelvű enciklopédia, nem gépi fordítás. Rövidítsd, szerkeszd, és
  magyarítsd a mondatszerkezetet is, ne csak a szavakat.

## 6. Forrás lekérése fordításhoz — token-hatékonyan

Ne olvasd be a nyers wikitext-et a whitewolf.fandom.com-ról közvetlenül — használd a
`scripts/fetch_source.py`-t, ami megtisztítja a sablonoktól, galériáktól, hivatkozásoktól:

```bash
python scripts/fetch_source.py "Cikk Neve (VTM)" --out scratch/cikk.txt
```

Ha a cím átirányítás, a szkript kiírja a célcímet.

## 7. Cikk megírása

Kövesd a `CONTRIBUTING.md` cikk-sablonját:
- Front matter: `title`, `description` (150-160 karakter), `status: stub` csak ha stúb.
- Első bekezdés: önmagában érthető, 40-60 szavas definíció (lásd Stílus szekció).
- Minden hivatkozott, de még nem létező fogalomhoz hozz létre egy minimális stúbot (lásd
  CONTRIBUTING.md stúb-konvenció) — SOHA ne hagyj törött linket vagy ne linkelj az angol
  fandom wikire helyette.
- Lábjegyzet: `!!! info "Forrás és licenc"` admonition a whitewolf.fandom.com forrásra, CC BY-SA
  megjelöléssel.
- Ha a terminológia munkafordítás (nincs forrás): `!!! warning "Terminológia megjegyzés"`
  admonition, hivatkozva a TERMINOLOGY.md-re.

## 8. Mielőtt befejezed — kötelező önellenőrzés

1. **Olvasd újra a saját cikkedet** a megírás után — ellenőrizd, hogy minden fogalom, amit
   használtál, konzisztens a `TERMINOLOGY.md`-vel, és hogy nem csúszott-e be bare angol szó
   magyar megfelelő nélkül (ez a leggyakoribb hiba, amit a szkript is keres, de az emberi/AI
   átolvasás korábban kifoghatja).
2. Futtasd le ezt az egy parancsot, és javítsd, amit jelez, **mielőtt** commitolsz:

```bash
python scripts/precommit.py
```

Ez sorban lefuttatja a `check_terminology.py`, `check_content_map.py`, `update_stats.py` és a
`mkdocs build --strict` ellenőrzéseket, és megáll az első hibánál — nem kell négy parancsot
külön megjegyezni.

A `check_terminology.py` és a `check_content_map.py` heurisztikák — minden találatot nézz át
emberi szemmel, mielőtt javítasz vagy elvet veted. Ha egy találat hamis pozitív (márkanév,
tulajdonnév, duális alak), vedd fel az `IGNORE_ENGLISH_TERMS` listára a `check_terminology.py`-ban
— az "X: The Y" mintájú játékcímeket (pl. egy új, jövőbeli játékvonalat) a szkript automatikusan
felismeri, azokhoz nem kell manuálisan bővíteni a listát.

## 9. Ha új fordítást rögzítesz

Mindig frissítsd a `TERMINOLOGY.md`-t is a cikkel egy commitban — sose maradjon egy cikkben
használt fordítás dokumentálás nélkül. Add hozzá a forrást (link + idézet, ha van), a
megbízhatósági szintet, és ha releváns, a `CONTENT_MAP.md` állapot-táblázatát is. Ha egy
játékvonalhoz új forrást találtál, frissítsd a 4. pont playbook-táblázatát is.

## 10. Git-munkafolyamat

- Minden munka a **`dev`** branch-en (vagy abból ágazó feature branch-en) zajlik.
- **Soha ne pushol `main`-re** — a `main`-re kerülés mindig explicit emberi jóváhagyással
  történik, nem automatikus.
- Egy commit tartalmazza a cikket/cikkeket ÉS a hozzá tartozó `TERMINOLOGY.md`/`CONTENT_MAP.md`
  frissítést is — ne szóródjon szét több apró commitra, amik külön-külön inkonzisztens
  állapotot hagynának a repóban.
