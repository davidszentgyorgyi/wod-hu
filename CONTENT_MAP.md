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

## Fő játékvilágok mérete (kategória cikkszám alapján)

### Classic World of Darkness (oWoD)
| Játékvilág | Cikkek (kategória mérete) |
|---|---|
| Werewolf: The Apocalypse | 1376 |
| Vampire: The Masquerade | 1156 |
| Mage: The Ascension | 839 |
| Wraith: The Oblivion | 793 |
| Changeling: The Dreaming | 670 |
| Demon: The Fallen | 314 |
| Hunter: The Reckoning | 250 |

### Chronicles of Darkness / nWoD (2004+)
| Játékvilág | Cikkek (kategória mérete) |
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

## Javasolt prioritási sorrend (játékvilág-független elv)

1. **Glosszárium / alapfogalmak** (pl. Embrace, Masquerade, Humanity, Frenzy, Kindred) — ezek nélkül semmilyen más cikk nem érthető.
2. **Setting-struktúra**: klánok/törzsek/rendek, szekták/frakciók — ez adja a "mi micsoda" áttekintést.
3. **Mechanikai/játékbeli fogalmak**: diszciplínák, ajándékok, varázslattípusok stb.
4. **Mellékvérvonalak, altípusok, almozgalmak** (bloodlines stb.).
5. **Karakterek, események, kiadványok** — legalacsonyabb prioritás, ez a legnagyobb volumenű, de legkevésbé alapvető réteg; közösségi kontributorokra bízható hosszú távon.

## 1. hullám — konkrét fordítási sorrend (Vampire: A Maszkabál)

Ez a legelső, konkrét munkalista. A sorrend az elv alapján (glosszárium → setting-struktúra →
mechanika → mellékágak → karakterek) van kialakítva. Minden tételhez a
[TERMINOLOGY.md](TERMINOLOGY.md)-ben rögzített terminológiát kell használni.

| # | Cikk | Státusz | Megjegyzés |
|---|---|---|---|
| 1 | Glosszárium alapfogalmak (Ölelés, Emberség, Őrjöngés, Éhség, Vértestvér, Klán, Diszciplína, Generáció) | ✅ Elkészült | `docs/glosszarium/index.md` |
| 2 | Kamarilla (szekta áttekintő) | ✅ Kész | `docs/vampire-a-maszkabal/kamarilla.md` — whitewolf.fandom.com alapján |
| 3 | Szabbat (szekta áttekintő) | ✅ Kész | `docs/vampire-a-maszkabal/szabbat.md` — whitewolf.fandom.com alapján |
| 4 | Anarch mozgalom | ✅ Kész | `docs/vampire-a-maszkabal/anarch.md` |
| 5 | A 13 fő klán áttekintő listája | ✅ Kész | `docs/vampire-a-maszkabal/klanok.md` |
| 6 | Brujah (klán) | ✅ Kész | |
| 7 | Ventrue (klán) | ✅ Kész | |
| 8 | Toreador (klán) | ✅ Kész | |
| 9 | Nosferatu (klán) | ✅ Kész | |
| 10 | Malkavian (klán) | ✅ Kész | Figyelem: a klán TAGJÁT "Malkavita"-nak hívjuk, lásd TERMINOLOGY.md |
| 11 | Gangrel (klán) | ✅ Kész | |
| 12 | Tremere (klán) | ✅ Kész | |
| 13 | Lasombra (klán) | ✅ Kész | |
| 13b | Banu Haqim (klán) | ✅ Kész | Nem volt az eredeti listán, de a 13 fő klán része |
| 13c | Hecata (klán) | ✅ Kész | `docs/vampire-a-maszkabal/hecata.md` — hiányzott a 13-ból, a felhasználó észrevétele alapján pótolva |
| 13d | Ministry (klán) | ✅ Kész | `docs/vampire-a-maszkabal/ministry.md` — hiányzott a 13-ból, a felhasználó észrevétele alapján pótolva |
| 24 | Káin | ✅ Kész | `docs/vampire-a-maszkabal/kain.md` — az első vámpír, korábban csak mellékesen volt említve, sosem volt önálló cikke |
| 25 | Gehenna | ✅ Kész | `docs/vampire-a-maszkabal/gehenna.md` — a vámpírok világvége, ugyanaz a hiányosság |
| 14 | Ravnos, Salubri, Tzimisce (klánok) | ✅ Kész | Külön cikkenként, nem egy összevont cikkben |
| 15 | Diszciplínák áttekintő listája | ✅ Kész | `docs/vampire-a-maszkabal/diszciplinak.md` |
| 15b | Diszciplínák részletes cikkei (11 db, V5 szintenkénti erők) | ✅ Kész | `docs/vampire-a-maszkabal/diszciplina-allatiassag.md` és további 10 testvércikk — mind a 11 Diszciplína saját cikket kapott, linkelve a 13 klán leírásából |
| 15c | Ragadozó-típus (Predator Type) karakteralkotási mechanika | ✅ Kész | `docs/vampire-a-maszkabal/predator-tipus.md` — a "milyen tartalom kell a játszhatósághoz" bővítés része |
| 15d | Előnyök és Hátrányok (Merits & Flaws) áttekintő | ✅ Kész | `docs/vampire-a-maszkabal/elonyok-es-hatranyok.md` |
| 15e | Kapaszkodók és Hitvallások (Touchstones & Convictions) | ✅ Kész | `docs/vampire-a-maszkabal/kapaszkodok-es-hitvallasok.md` |
| 21 | Kiasyd bloodline | ✅ Kész | `docs/vampire-a-maszkabal/kiasyd.md` — Vampire-mélyítés, "csináld" bővítés része |
| 22 | Nagaraja bloodline | ✅ Kész | `docs/vampire-a-maszkabal/nagaraja.md` |
| 23 | Lamiák bloodline | ✅ Kész | `docs/vampire-a-maszkabal/lamiak.md` |
| 24b | Vérfivérek (Blood Brothers) bloodline | ✅ Kész | `docs/vampire-a-maszkabal/verfiverek.md` |
| 25b | Loresheet-ek mechanika | ✅ Kész | `docs/vampire-a-maszkabal/loresheet-ek.md` |
| 25c | Amalgamok (Combination Disciplines) mechanika | ✅ Kész | `docs/vampire-a-maszkabal/amalgamok.md` |
| 25d | Vérmágia Rituálék (Blood Sorcery Rituals) | ✅ Kész | `docs/vampire-a-maszkabal/vermagia-ritualek.md` |
| 25e | Hígvérű Alkímia (Thin-Blood Alchemy) | ✅ Kész | `docs/vampire-a-maszkabal/higveru-alkimia.md` |
| 26 | Anarch Forradalom (Anarch Revolt), történelmi esemény | ✅ Kész | `docs/vampire-a-maszkabal/anarch-forradalom.md` |
| 27 | Thorns-i Egyezmény (Convention of Thorns), történelmi esemény | ✅ Kész | `docs/vampire-a-maszkabal/thorni-egyezmeny.md` |
| 28 | A Hat Hagyomány (Kamarilla Traditions) részletes cikk | ✅ Kész | `docs/vampire-a-maszkabal/hagyomanyok.md` |
| 29 | A Megvilágosodás Útjai (Paths of Enlightenment) | ✅ Kész | `docs/vampire-a-maszkabal/megvilagosodas-utjai.md` |
| 30 | Milánói Kódex (Code of Milan), a Szabbat szabályzata | ✅ Kész | `docs/vampire-a-maszkabal/milanoi-kodex.md` |
| 31 | Hardestadt, Kamarilla-alapító NPC | ✅ Kész | `docs/vampire-a-maszkabal/hardestadt.md` |
| 32 | Tyler, Anarch Forradalmat elindító NPC | ✅ Kész | `docs/vampire-a-maszkabal/tyler.md` |
| 33 | Helena, Toreador methuselah NPC | ✅ Kész | `docs/vampire-a-maszkabal/helena.md` |
| 34 | Succubus Club, chicagói Elysium | ✅ Kész | `docs/vampire-a-maszkabal/succubus-club.md` |
| 35 | Példakarakter (teljesen eredeti, kész V5 karakter) | ✅ Kész | `docs/vampire-a-maszkabal/pelda-karakter.md` |
| 36 | Kezdő Kaland (teljesen eredeti egy-estés kalandvázlat) | ✅ Kész | `docs/vampire-a-maszkabal/kezdo-kaland.md` |
| 37 | Karl Schrekt, Tremere Justicar NPC | ✅ Kész | `docs/vampire-a-maszkabal/karl-schrekt.md` |
| 38 | Theo Bell, Brujah Archon NPC | ✅ Kész | `docs/vampire-a-maszkabal/theo-bell.md` |
| 39 | Carna, Tremere-ellenes NPC | ✅ Kész | `docs/vampire-a-maszkabal/carna.md` |
| 40 | A Voerman Nővérek, Malkavian NPC-pár | ✅ Kész | `docs/vampire-a-maszkabal/voerman-nover.md` |
| 41 | A Tömegrohajárások Hete (Week of Nightmares), történelmi esemény | ✅ Kész | `docs/vampire-a-maszkabal/tomegrohajarasok-hete.md` |
| 42 | Rudi, Gangrel Anarch NPC | ✅ Kész | `docs/vampire-a-maszkabal/rudi.md` |
| 43 | Ambrus Maropis, Nosferatu NPC | ✅ Kész | `docs/vampire-a-maszkabal/ambrus-maropis.md` |
| 16 | Maszkabál (a szabály részletes kifejtése) | ✅ Kész | `docs/vampire-a-maszkabal/maszkabal.md` |
| 17 | Hígvérű (Thin-Blooded) | ✅ Kész | `docs/vampire-a-maszkabal/higveru.md` |
| 18 | Caitiff | ✅ Kész | `docs/vampire-a-maszkabal/caitiff.md` |
| 19 | Második Inkvizíció | ✅ Kész | `docs/vampire-a-maszkabal/masodik-inkvizicio.md` |
| 20 | Bloodline-ok (mellékvérvonalak) listája | ✅ Kész | `docs/vampire-a-maszkabal/bloodline-ok.md` |
| 21 | Prestation | ✅ Kész | `docs/vampire-a-maszkabal/prestation.md` — fordítatlan, nincs forrás |
| 22 | Vaulderie | ✅ Kész | `docs/vampire-a-maszkabal/vaulderie.md` — fordítatlan, nincs forrás |
| 23 | Jyhad | ✅ Kész | `docs/vampire-a-maszkabal/jyhad.md` — fordítatlan, nincs forrás |

## Új játékvonalak (eredeti tervben nem szerepeltek)

| # | Cikk | Státusz | Megjegyzés |
|---|---|---|---|
| H1 | Hunter: A Leszámolás (bevezető) | ✅ Kész | `docs/hunter-a-leszamolas/index.md` — csak a "Vadász" kreatúra-név megerősített |
| D1 | Demon: A Bukottak (bevezető) | ✅ Kész | `docs/demon-a-bukottak/index.md` — csak a "Bukott" kreatúra-név megerősített |

## Alapmotor — játékvilág-független mechanikai cikkek

Ezek a cikkek a Storyteller/Storytelling rendszer alapmechanikáját írják le, ami minden WoD
játékvilágban (Vampire, Werewolf, Mage, stb.) ugyanúgy (vagy nagyon hasonlóan) működik — ezért
külön, szetting-független kategóriaként kezeljük, a `docs/glosszarium/` alatt.

| # | Cikk | Státusz | Megjegyzés |
|---|---|---|---|
| E1 | Dobásrendszer (dicepool, siker, Éhség-kockák, kritikus siker) | ✅ Kész | `docs/glosszarium/dobasrendszer.md` |
| E2 | Attribútumok (9 alaptulajdonság) | ✅ Kész | `docs/glosszarium/attributumok.md` |
| E3 | Képességek (Skills, kb. 27 db) | ✅ Kész | `docs/glosszarium/kepessegek.md` |
| E4 | Akaraterő (Willpower) | ✅ Kész | `docs/glosszarium/akaratero.md` |
| E5 | Életerő és Sebzés (Health track, sebzéstípusok) | ✅ Kész | `docs/glosszarium/eletero-es-sebzes.md` |
| E6 | Harc alapjai (kezdeményezés, támadás/védelem) | ✅ Kész | `docs/glosszarium/harc-alapjai.md` |
| E7 | Tapasztalat (Experience Points, karakterfejlődés) | ✅ Kész | `docs/glosszarium/tapasztalat.md` |

## 2. hullám — Vampire mélyebb fogalmak, és a többi játékvilág első cikkei

A Vampire-vonal maradék Wave 1 elemei (Diszciplínák, Maszkabál, Hígvérű, Caitiff, Második
Inkvizíció, Bloodline-ok) és 3 további mélyebb fogalom (Generáció, Vérkötelék, Diabléria) mind
elkészültek, `docs/vampire-a-maszkabal/` alatt.

A többi négy játékvilághoz is elkészült egy első kör alapfogalom-cikk, **munkafordítással**
(nincs még hivatalos/közösségi forrás-megerősítés, lásd TERMINOLOGY.md):

| Játékvilág | Cikkek |
|---|---|
| Werewolf: Az Apokalipszis | Garou, Törzsek, Gaia, A Wyrm, Ajándékok, Rage, Umbra |
| Mage: A Felemelkedés | Mágusrendek, Szférák, Paradox, Arete, Technokrácia, Avatar |
| Wraith: A Feledés | Árnyék, Labirintus, Legiók, Kötelékek és Szenvedélyek |
| Changeling: Az Álmok | Kith, Banalitás, Glamour, Seelie/Unseelie Udvarok |

**Következő lépés ezekhez a játékvilágokhoz**: közösségi/hivatalos magyar forrás keresése a
terminológia megerősítéséhez (hasonlóan ahhoz, ahogy a Vampire-vonalnál a Delta Vision kiadást és
a magyar fan-fórumokat használtuk) — lásd TERMINOLOGY.md nyitott kérdéseit.

**Jelmagyarázat:** ✅ kész · 🟡 stúb (van oldal, bővítésre vár) · 🔲 nincs elkezdve, nincs még oldal
sem. A friss számokat a kezdőlap [státusz-blokkja](docs/index.md) mutatja automatikusan.

**Hogyan haladjunk?** Nem kötelező sorrendben dolgozni — ha valakinek a Tremere klán a kedvence,
nyugodtan azzal kezdhet. A sorszám csak ajánlás, nem szigorú szabály. Fontosabb, hogy a
[TERMINOLOGY.md](TERMINOLOGY.md)-t és a [stúb-konvenciót](CONTRIBUTING.md#kereszthivatkozások-stúb-konvenció)
kövessük.

## 3. hullám — mélyebb tartalom mind az 5 játékvilágban

A 2. hullám után mind a négy nem-Vampire játékvilág kapott egy második kör alapfogalom-cikket is
(7+7+6+6 cikk), és a Vampire-vonal 4 Bloodline-ja (True Brujah, Baali, Gargoyle-ok, Salubri
antitribu) is önálló cikket kapott.

| Játékvilág | Új cikkek |
|---|---|
| Werewolf: Az Apokalipszis | Auspice-ok, Totem, Kinfolk, Litánia, Delirium, Wyld, Black Spiral Dancers |
| Mage: A Felemelkedés | Ébredés, Konszenzus, Quintessence, Node, Marginálisok, Nephandik, Rote |
| Wraith: A Feledés | Arcanoi, Pathos/Corpus/Angst, Céhek, Risen, Spectre, Renegátok |
| Changeling: Az Álmok | Chimera, Dreaming, Autumn People, Nemesi Házak, Redcap, Nunnehi |
| Vampire: A Maszkabál | True Brujah, Baali, Gargoyle-ok, Salubri antitribu |

**Összesen 90 cikk kész.** A `scripts/check_terminology.py` minden batch után lefuttatva —
lásd a README terminológia-konzisztencia szekcióját.

## Következő lépések a feltérképezésben

1. **Terminológiai megerősítés**: a Werewolf/Mage/Wraith/Changeling cikkek munkafordítások, nincs
   hivatalos vagy közösségi forrásuk — ez a legfontosabb következő lépés, mielőtt ezekből sokkal
   többet fordítanánk.
2. Pontos alkategória-struktúra feltérképezése a whitewolf.fandom.com API-n keresztül, játékvilágonként.
3. Cikklista export `list=categorymembers` segítségével, játékvilágonként — a még hiányzó, mélyebb
   tartalom (pl. egyes klánok/törzsek/rendek teljes története) azonosításához.
