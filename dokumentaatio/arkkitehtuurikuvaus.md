# Arkkitehtuurikuvaus

## Ohjelman rakenne

Sovelluksen pakkausrakenne on tällä hetkellä seuraava:

![IMG_2067](https://user-images.githubusercontent.com/75749790/116064853-14892b00-a68f-11eb-8d9d-8d5df94e81ff.jpg)

## Käyttöliittymä

Sovelluksen käyttöliittymä on toteutettu hakemiston ui luokkaan Display ja sisältää neljä erilaista näkymää:

- tasovalikko
- pelitila
- voittoruutu
- häviöruutu

## Sovelluslogiikka ja toiminnallisuudet

Sovelluslogiikka muodostuu hakemiston gamelogic luokista Menu sekä Gameloop, joihin on metodeina toteutettu pelin toiminnallisuus.

### Pelin aloittaminen ja menun toiminta

Sovelluksen avaaminen muodostaa seuraavanlaisen tapahtumaketjun. Oletetaan käyttäjän klikkaavan valikosta kohtaa "Vaikea" ja pelaavan tason onnistuneesti läpi.

![IMG_2066](https://user-images.githubusercontent.com/75749790/116063586-cf182e00-a68d-11eb-9b94-49d8b703bdf2.jpg)

Menu lähettää UI:lle määräyksen piirtää valikkonäkymä. Käyttäjän valitessa tason _Vaikea_ menu arpoo WordRepository-luokassa 4-5 merkkiä pitkän sanan, minkä jälkeen luodaan Gameloop-olio ja aloitetaan peli arvotulla sanalla. Käyttäjän onnistuessa pelissä luo UI voittoruudun, hävitessä häviöruudun. Rastista painamalla pelitila palaa takaisin valikkoon.
