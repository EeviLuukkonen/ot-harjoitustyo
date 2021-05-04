# Käyttö-ohje

## Ohjelman käynnistäminen

Asenna riippuvuudet komennolla:

```
poetry install
```

Peli alkaa suoraan onnistuneen asennuksen jälkeen hirsipuu_peli-kansiossa terminaalin komennolla

```
poetry run invoke start
```

## Peliohjeet

Peli aukeaa valikkonäkymään, jossa voi klikkaamalla valita vaikeustason:
![Screenshot from 2021-05-04 17-19-46](https://user-images.githubusercontent.com/75749790/117018449-2dcc5000-acfd-11eb-835f-4d50e273af14.png)

Peliä pelataan arvailemalla sanassa olevia kirjaimia ja klikkailemalla niistä ruudulla. Ruudulla on valmiiksi sanan ensimmäinen kirjain ja tämän mahdolliset muut esiintymät sanassa.

![Screenshot from 2021-05-04 17-20-13](https://user-images.githubusercontent.com/75749790/117018975-acc18880-acfd-11eb-923c-f4874d84d79a.png)

Kuudesta väärästä arvauksesta peli päättyy.

![Screenshot from 2021-05-04 17-20-37](https://user-images.githubusercontent.com/75749790/117019001-b21ed300-acfd-11eb-9188-240ae21b4295.png)

Jos keksit kaikki oikeat kirjaimet, voitat pelin! Koita päihittää itsesi nopeudessa.
![Screenshot from 2021-05-04 17-21-06](https://user-images.githubusercontent.com/75749790/117018523-3c1a6c00-acfd-11eb-8dd5-4b548c429163.png)
