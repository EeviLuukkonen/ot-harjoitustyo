# Hirsipuu

Sovellus on hirsipuu-peli, jossa pelaaja arvailee suomenkielistä sanaa pelialueella näkyvistä kirjaimista klikkailemalla. Tavoite on keksiä oikea sana, ennen kuin ukko joutuu hirteen.

## Python-versio

Sovellus on testattu versiolla 3.8.5. Toimivaan sovellukseen vaaditaan vähintään versio 3.6.0.

## Dokumentaatio

* [uusin release](https://github.com/EeviLuukkonen/ot-harjoitustyo/releases)
* [arkkitehtuurikuvaus](https://github.com/EeviLuukkonen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuurikuvaus.md)
* [käyttöohje](https://github.com/EeviLuukkonen/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
* [vaatimusmäärittely](https://github.com/EeviLuukkonen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimuusmaarittely.md)
* [työaikakirjanpito](https://github.com/EeviLuukkonen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

## Sovelluksen asentaminen ja avaaminen

1. Asenna riippuvuudet terminaalin komennolla

```bash
poetry install
```

2. Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

## Testaus

1. Suorita testit komennolla

```bash
poetry run invoke test
```

2. Luo testikattavuusraportti komennolla

```bash
poetry run invoke coverage-report
```
3. Koodin laaturaportin saa komennolla

```bash
poetry run invoke lint
```
