# Testausdokumentti

Sovellusta testataan unittestilla yksikkö- ja integraatiotasolla seuraavasti:

## Sovelluslogiikka

Sovelluslogiikasta vastaavia luokkia testataan TestGameloop- ja TestMenu -nimisillä luokilla. TestMenu-luokkaa varten alustetaan valeluokat StubDisplay ja StubEventQueue. TestGameloop-luokkaa varten alustetaan näiden lisäksi luokat StubEvents ja StubImages.

## Repositoriot

Repositorio-luokkaa Highscore testataan TestHighscore-luokalla.

## Testauskattavuus

Sovelluksen testauskattavuudesta on jätetty pois kaikki käyttöliittymään liittyvä UI-hakemiston koodi. Testauskattavuus on 90% ja testejä on 8.

![Screenshot from 2021-05-12 20-14-34](https://user-images.githubusercontent.com/75749790/118016970-b6cb3300-b35e-11eb-811d-ce55ccf4c319.png)

Gameloop-luokassa testaamatta jäi win-metodi ja config.py-tiedostossa FileNotFound-poikkeus. Myös komentoriviltä suorittaminen initialize_database-tiedostossa jäi testauksen ulkopuolelle. Muuten testausraportti on kattava.

## Järjestelmätestaus

Järjestelmätestausta on suoritettu manuaalisesti testaamalla kaikki määrittelydokumentin asettamat toiminnallisuudet. Testattu Linuxin lisäksi myös macOS-käyttöjärjestelmällä.

## Sovellukseen jääneet ongelmat

Pitkissä sanoissa on pieni mahdollisuus, että sana ylettyy peliruudun yli pois näkyvistä. Kyseiseen tilanteeseen ei ole kuitenkaan testatessa kertaakaan päädytty.
