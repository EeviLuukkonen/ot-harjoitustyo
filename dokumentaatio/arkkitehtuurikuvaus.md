# Arkkitehtuurikuvaus

## Ohjelman rakenne

Sovelluksen koodin pakkausrakenne on seuraava:

![Screenshot from 2021-05-12 20-44-49](https://user-images.githubusercontent.com/75749790/118020598-ec721b00-b362-11eb-9e80-286646bc1c55.png)

Pakkaus ui sisältää käyttöliittymästä ja gamelogic sovelluslogiikasta vastaavan koodin. Words-pakkauksessa on tekstitiedosto peliin arvottavia sanoja, images-kansiossa puolestaan kuvatiedostot peliä varten.

## Käyttöliittymä

Sovelluksen käyttöliittymä on toteutettu hakemiston ui luokkaan Display ja sisältää neljä erilaista näkymää:

- tasovalikko
- pelitila
- voittoruutu
- häviöruutu

![Screenshot from 2021-05-12 20-51-25](https://user-images.githubusercontent.com/75749790/118021423-e2045100-b363-11eb-8cdb-1640bdf0efe2.png)

Käyttöliittymä on eriytetty sovelluslogiikasta, mutta kaikki näkymät on toteutettu metodeina samaan luokkaan siksi, että näkymissä on paljon samoja ominaisuuksia toisiinsa nähden.

## Tietojen pysyväistallennus

Sovellus tallentaa tietokantaan peliaikoja. Tästä vastaa reposities-hakemiston luokka Highscores. Tietokannat scores.sqlite ja test-scores.sqlite löytyvät hakemistosta data. Sovelluksen juuren .env-tiedosto määrittelee tietokannan nimen.

## Sovelluslogiikka ja toiminnallisuudet

Sovelluslogiikka muodostuu hakemiston gamelogic luokista Menu, Gameloop, EventQueue ja Clock, joihin on metodeina toteutettu pelin toiminnallisuus. Luokkien välisiä suhteita kuvaa oheinen kaavio:

![Screenshot from 2021-05-04 18-04-38](https://user-images.githubusercontent.com/75749790/117025222-65d69180-ad03-11eb-8a38-78f8c6af072c.png)


### Pelin toiminta

Sovelluksen avaaminen muodostaa seuraavanlaisen tapahtumaketjun. Oletetaan käyttäjän klikkaavan valikosta kohtaa "Vaikea" ja pelaavan tason onnistuneesti läpi.

![IMG_2066](https://user-images.githubusercontent.com/75749790/116063586-cf182e00-a68d-11eb-9b94-49d8b703bdf2.jpg)

Menu lähettää UI:lle määräyksen piirtää valikkonäkymä. Käyttäjän valitessa tason _Vaikea_ menu arpoo WordRepository-luokassa 10-14 merkkiä pitkän sanan, minkä jälkeen luodaan Gameloop-olio ja aloitetaan peli arvotulla sanalla. Käyttäjän onnistuessa pelissä luo UI voittoruudun, hävitessä häviöruudun. Rastista painamalla pelitila palaa takaisin valikkoon.

Pelin aikana suoritettavat toiminnot noudattavat samankaltaista periaatetta.


