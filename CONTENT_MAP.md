# Tartalom feltérképezés — forrás wiki

Utolsó frissítés: 2026-10-06

## Forrás megerősítve

**https://whitewolf.fandom.com** ("White Wolf Wiki") — ez a hivatkozási alap, NEM a `worldofdarkness.fandom.com`.

Főlap: https://whitewolf.fandom.com/wiki/Main_Page

### Miért ez és nem a worldofdarkness.fandom.com?

API-n (`/api.php?action=query&meta=siteinfo&siprop=statistics`) keresztül lekért statisztikák:

| Wiki | Cikkek | Aktív szerkesztő | Admin |
|---|---|---|---|
| worldofdarkness.fandom.com | 353 | 1 | 2 |
| vtm.fandom.com | 1429 | 0 | 3 |
| **whitewolf.fandom.com** | **30 971** | **55** | **10** |

A whitewolf.fandom.com összehasonlíthatatlanul nagyobb és aktívabb — ez a valódi, teljes körű WoD-enciklopédia (oWoD + nWoD/Chronicles of Darkness egyaránt).

## API hozzáférés

A fandom wikik MediaWiki motort futnak, standard, nyilvános API-val:
- Base: `https://whitewolf.fandom.com/api.php`
- Hasznos endpointok:
  - `action=query&list=allcategories&acprop=size` — kategórialista méretekkel
  - `action=query&titles=Category:X&prop=categoryinfo` — egy adott kategória cikkszáma
  - `action=query&list=categorymembers&cmtitle=Category:X` — kategória tagjainak listája
  - `action=query&meta=siteinfo&siprop=statistics` — globális statisztika

Ez lehetővé teszi, hogy a teljes cikklistát és kategóriastruktúrát programozottan, scrape-elés nélkül kinyerjük.

## Fő szettingek mérete (kategória cikkszám alapján)

### Classic World of Darkness (oWoD)
| Szetting | Cikkek (kategória mérete) |
|---|---|
| Werewolf: The Apocalypse | 1376 |
| Vampire: The Masquerade | 1156 |
| Mage: The Ascension | 839 |
| Wraith: The Oblivion | 793 |
| Changeling: The Dreaming | 670 |
| Demon: The Fallen | 314 |
| Hunter: The Reckoning | 250 |

### Chronicles of Darkness / nWoD (2004+)
| Szetting | Cikkek (kategória mérete) |
|---|---|
| Werewolf: The Forsaken | 827 |
| Vampire: The Requiem | 357 |
| Mage: The Awakening | 122 |
| Changeling: The Lost | 25 (alulreprezentált — valószínűleg más kategórianév alatt is van tartalom, utánajárás kell) |

Megjegyzés: a kategóriák között átfedés lehet (pl. egy cikk több kategóriában is szerepelhet, "Clans", "Disciplines" stb. aliasok 0-t adtak vissza — pontos alkategória-neveket még fel kell térképezni).

## Vampire: The Masquerade — részletes alkategória-struktúra (mintaként feltérképezve)

A `Category:Vampire:_The_Masquerade` alatt 35 alkategória van. A tartalmi (nem média/merch/stub jellegű) alkategóriák mérete:

| Alkategória | Cikkek | Jellege |
|---|---|---|
| Vampire: The Masquerade character | 4161 | NPC-k, karakterek — rengeteg, de fordítási szempontból **alacsony prioritás** (enciklopédikus névsor, nem alapfogalom) |
| Vampire: The Masquerade glossary | 1095 | **Alapfogalmak, szakszavak** — ez a fordítás gerince, legmagasabb prioritás |
| Vampire: The Masquerade organizations | 439 | Szekták, frakciók, céhek — közepes-magas prioritás |
| Bloodlines (VTM) | 99 | Mellékvérvonalak — közepes prioritás, a fő klánok után |
| Clans (VTM) | 43 | **A 13 fő klán és leírásuk** — magas prioritás, alapvető setting-elem |
| Sects | 23 | Camarilla, Sabbat, Anarch stb. — magas prioritás |
| Independent Clans | 8 | Önálló klánok listája — magas prioritás |

**Tanulság a priorizáláshoz**: a nyers kategóriaméret (pl. "character" 4161 cikk) megtévesztő — nem a legnagyobb kategóriával kell kezdeni, hanem a legtöbb más cikk által hivatkozott alapfogalmakkal (glossary, clans, sects), mert ezekre támaszkodik minden egyéb cikk.

## Javasolt prioritási sorrend (szetting-független elv)

1. **Glosszárium / alapfogalmak** (pl. Embrace, Masquerade, Humanity, Frenzy, Kindred) — ezek nélkül semmilyen más cikk nem érthető.
2. **Setting-struktúra**: klánok/törzsek/rendek, szekták/frakciók — ez adja a "mi micsoda" áttekintést.
3. **Mechanikai/játékbeli fogalmak**: diszciplínák, ajándékok, varázslattípusok stb.
4. **Mellékvérvonalak, altípusok, almozgalmak** (bloodlines stb.).
5. **Karakterek, események, kiadványok** — legalacsonyabb prioritás, ez a legnagyobb volumenű, de legkevésbé alapvető réteg; közösségi kontributorokra bízható hosszú távon.

## Következő lépések a feltérképezésben

1. Pontos alkategória-struktúra feltérképezése szettingenként (pl. Vampire: The Masquerade → Klánok, Diszciplínák, Szekták, Frakciók alkategóriák helyes nevekkel).
2. Cikklista export `list=categorymembers` segítségével, szettingenként.
3. Alapfogalom-cikkek azonosítása (pl. "Embrace", "Humanity", "Masquerade") — ezek a legmagasabb prioritásúak, mert minden más cikk hivatkozik rájuk.
4. Szócikk-hossz/komplexitás becslése a fordítási munka méretezéséhez.
5. Ebből álljon össze a végleges fordítási priorizálási lista.
