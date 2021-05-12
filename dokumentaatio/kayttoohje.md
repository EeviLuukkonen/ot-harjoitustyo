# Käyttö-ohje

## Ohjelman lataaminen

Projektin viimeisimmän releasen lähdekoodin voi ladata klikkaamalla Releases-osion alta kohtaa Source code.

## Konfigurointi

Pelinaikainen tallennus tapahtuu data-hakemistoon tietokantaan scores.sqlite. Tiedostonimeä voi konfiguroida .env-tiedostossa:

```
SCORES_FILENAME=scores.sqlite
```

## Ohjelman käynnistäminen

Asenna riippuvuudet komennolla:

```
poetry install
```

Suorita alustus komennolla:

```
poetry run invoke build
```

Peli alkaa suoraan onnistuneen asennuksen jälkeen terminaalin komennolla:

```
poetry run invoke start
```

## Peliohjeet

Peli aukeaa valikkonäkymään, jossa voi klikkaamalla valita vaikeustason. Pelin voi sulkea yläkulman rastista.


![Screenshot from 2021-05-04 17-19-46](https://user-images.githubusercontent.com/75749790/117018449-2dcc5000-acfd-11eb-835f-4d50e273af14.png)


Peliä pelataan arvailemalla sanassa olevia kirjaimia ja klikkailemalla niistä ruudulla. Ruudulla on valmiiksi sanan ensimmäinen kirjain ja tämän mahdolliset muut esiintymät sanassa. Yläkulman rastia painamalla pääsee takaisin valikkonäkymään. Koita olla nopea!


![Screenshot from 2021-05-04 17-20-13](https://user-images.githubusercontent.com/75749790/117018975-acc18880-acfd-11eb-923c-f4874d84d79a.png)


Kuudesta väärästä arvauksesta peli päättyy.


![Screenshot from 2021-05-04 17-20-37](https://user-images.githubusercontent.com/75749790/117019001-b21ed300-acfd-11eb-9188-240ae21b4295.png)


Jos keksit kaikki oikeat kirjaimet, voitat pelin! Tulostauluun ilmestyy tuloksiasi nopeusjärjestykseen.


![Screenshot from 2021-05-12 19-28-51](https://user-images.githubusercontent.com/75749790/118011156-5e913280-b358-11eb-8c39-c5f517762e13.png)

