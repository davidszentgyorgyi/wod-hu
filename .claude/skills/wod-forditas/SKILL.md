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

Használd azt a fordítást, pontosan úgy, ahogy rögzítve van (beleértve a "fordítatlan,
tulajdonnévként kezelve" döntéseket is — pl. Caitiff, Ghoul, Auspex nem fordítjuk).

## 2. Ha egy fogalom MÉG NEM szerepel a TERMINOLOGY.md-ben — kutatási protokoll

Ne találj ki fordítást megerősítés nélkül. Kövesd ezt a sorrendet:

1. **Hivatalos magyar kiadás ellenőrzése.** A World of Darkness-nek van hivatalos magyar
   kiadása (Delta Vision, "Vámpír: A Maszkabál", 2010/2023) — csak a Vampire-vonalhoz. Ha a
   fogalom ebből a vonalból van, keress rá a Delta Vision oldalán
   (deltavision.hu) és termékleírásokban.
2. **Valódi magyar fan-közösségi forrás keresése.** Eddig megbízhatónak bizonyult források:
   - [lfg.hu](https://lfg.hu) — magyar szerepjátékos közösségi oldal, van V5 ismertető cikke
   - [radavit.blogspot.com](https://radavit.blogspot.com) — V5 ismertető
   - [wodhu.blogspot.com](https://wodhu.blogspot.com) — magyar WoD fan blog
   - [worldofdarkness.hungarianforum.net](https://worldofdarkness.hungarianforum.net) — aktív
     magyar WoD szerepjátékos fórum
   - Ha ezek nem elegendők, végezz új keresést hasonló magyar RPG-fórumokra, blogokra.
3. **KRITIKUS SZABÁLY — sose bízz AI-összegzésben bejelentkezés-védett vagy üres oldalról.**
   Ha egy forrás (pl. fórum-alkategória) tartalmát WebFetch-csel kéred le, és az eredmény
   gyanúsan részletes vagy "túl jó", **ellenőrizd nyers HTTP-kéréssel** (`curl` vagy a Bash
   eszköz), hogy a tartalom valóban létezik, nem pedig az összegző modell találta ki. Ez már
   egyszer megtörtént ezen a projekten (lásd TERMINOLOGY.md figyelmeztetését) — egy
   bejelentkezés-képernyőt mutató oldalról a modell részletes alkategória-listát "olvasott ki",
   amit nem is látott.
4. **Legalább 2 egymástól független forrás egyezése esetén** jelöld a fordítást
   **"Megerősített"**-ként a `TERMINOLOGY.md`-ben, idézettel és linkkel.
5. **Ha nincs forrás, vagy csak egy van:** jelöld **"Döntés, nincs közvetlen forrás"**-ként —
   ez azt jelenti, hogy saját munkafordítást használsz, de ezt a cikkben is jelezni kell egy
   `!!! warning "Terminológia megjegyzés"` admonitionnal.
6. **Ha semmit nem találsz:** ne találj ki semmit — vedd fel a "Még nyitott / tisztázandó
   terminusok" listára a `TERMINOLOGY.md`-ben, és hagyd a fogalmat angolul a cikkben, jelezve a
   bizonytalanságot.

### Konkrét, megerősített döntések, amiket emlékezz

- **"Sect" → "Szekta"** (nem "frakció") — két független forrás szerint.
- **"Setting" → "Játékvilág"** (nem "szetting") — a magyar közösség a "világ" szót használja.
- **Werewolf → Vérfarkas, Wraith → Lidérc** (NEM "Szellem"!), **Mage → Mágus**, **Changeling →
  Tündér** (NEM "tünde/tündék" — az a Tolkien "Elf" fordítása, más szó!).
- Klánnevek (Brujah, Toreador, stb.) **tulajdonnevek, nem fordítjuk**.
- Szervezeti címek (Prince, Primogen, Justicar, stb.) fordítatlanok, kivéve ahol van egyértelmű
  rövid magyar glossza (Prince → "Herceg", Archbishop → "Érsek").
- "World of Darkness", "Vampire: The Masquerade", "Masquerade" (mint cím) **márkanévként
  fordítatlanul maradhatnak** futó szövegben — ne cseréld ki mindenhol "Sötétség Világára".

## 3. Forrás lekérése fordításhoz — token-hatékonyan

Ne olvasd be a nyers wikitext-et a whitewolf.fandom.com-ról közvetlenül — használd a
`scripts/fetch_source.py`-t, ami megtisztítja a sablonoktól, galériáktól, hivatkozásoktól:

```bash
python scripts/fetch_source.py "Cikk Neve (VTM)" --out scratch/cikk.txt
```

Ha a cím átirányítás, a szkript kiírja a célcímet.

## 4. Cikk megírása

Kövesd a `CONTRIBUTING.md` cikk-sablonját:
- Front matter: `title`, `description` (150-160 karakter), `status: stub` csak ha stúb.
- Első bekezdés: önmagában érthető, 40-60 szavas definíció.
- Minden hivatkozott, de még nem létező fogalomhoz hozz létre egy minimális stúbot (lásd
  CONTRIBUTING.md stúb-konvenció) — SOHA ne hagyj törött linket vagy ne linkelj az angol
  fandom wikire helyette.
- Lábjegyzet: `!!! info "Forrás és licenc"` admonition a whitewolf.fandom.com forrásra, CC BY-SA
  megjelöléssel.
- Ha a terminológia munkafordítás (nincs forrás): `!!! warning "Terminológia megjegyzés"`
  admonition, hivatkozva a TERMINOLOGY.md-re.

## 5. Mielőtt befejezed — kötelező ellenőrzés

Mindig futtasd le ezt a kettőt, és javítsd, amit jeleznek, **mielőtt** commitolsz:

```bash
python scripts/check_terminology.py   # terminológiai konzisztencia (angol szó magyar nélkül)
python scripts/update_stats.py        # kész/stúb/hiányzó-link statisztika frissítése
mkdocs build --strict                 # build-hiba és hiányzó nav-bejegyzés ellenőrzése
```

A `check_terminology.py` heurisztika — minden találatot nézz át emberi szemmel, mielőtt
javítasz vagy elvet veted. Ha egy találat hamis pozitív (márkanév, tulajdonnév, duális alak),
vedd fel az `IGNORE_ENGLISH_TERMS` listára a szkriptben, ne hagyd figyelmen kívül némán.

## 6. Ha új fordítást rögzítesz

Mindig frissítsd a `TERMINOLOGY.md`-t is a cikkel egy commitban — sose maradjon egy cikkben
használt fordítás dokumentálás nélkül. Add hozzá a forrást (link + idézet, ha van), a
megbízhatósági szintet, és ha releváns, a `CONTENT_MAP.md` állapot-táblázatát is.
