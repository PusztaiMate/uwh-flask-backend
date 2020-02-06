# Mindenféle

__Disclaimer__: nincs hosszú *__i__* a billentyűzetemen, szóval rövid *__i__* lesz mindenhol.

## Projektről

Az Egyszuszos edzésre járási statisztikákat hivatott egyelőre kezelni, de a jövőben remélem, hogy lesz idő/energia bőviteni:

* Bemutató felület, ahova újonnan érkezők is odatévedhetnek (leirással a hokiról, felszerelésről, edzésekről, stb.)
* Tudásbázis a felállásokkal, edzéstervekkel, stb.
* Fórum esetleg, pl. videóelemzések archiválásához, versenyek lebeszéléséhez
* Tagdij állapota (automatikus köremail, akár személyesen is mindenkinek)
* Versenynaptár
* Hirfal, a facebook feedünkhöz hasonlóan az eredményekkel, stb.

## Mi kell ahhoz, hogy te is hozzá tudj rakni a projekthez?

### Nem kód

* ötlet (mit csináljon, hogyan nézzen ki, stb.)
* bármi grafika

### Kód

__Ami kelleni fog biztosan__
* git (https://git-scm.com/)
* python (3.8 mondjuk, de bármi 3.6+ jó kell, hogy legyen)
* docker (https://docs.docker.com/docker-for-windows/)
* docker-compose (https://docs.docker.com/compose/install/)

__Nem kötelező, de hasznos__
* VSCode (https://code.visualstudio.com/)

__Első lépések Windoshoz__
1. Telepits fel mindent, ami fel van sorolva!
2. Nyomd le a windows gombot (vagy nyisd meg a start menüt) és gépeld be, hogy "git bash"! A felugró programot inditsd el!
3. Add ki a következő parancsokat behelyettesitve a neved a kacsacsőrök közé (< >), entert nyomva utánuk!
    ```bash
    git config --global user.name <neved>
    git config --global user.email <email cimed>
    ```
4. Nyisd meg a fájlkezelődet (Mappa?) és menj be abba a mappába, ahol a projektet szeretnéd tartani (pl. Dokumentumok/Vizihoki/Weboldal, de bármi jó)! Ide lesznek "letöltve" a fájlok és itt lehet majd szerkeszteni őket.
5. shift+jobb klikket megnyomva válaszd ki az "Open git bash here" vagy "Git bash megnyitásat itt" menüpontot.
6. A felugró terminálban ird be a következő parancsot:
```bash
git clone https://gitlab.com/PusztaiMate/uwh-backend.git
git remote add origin https://gitlab.com/PusztaiMate/uwh-backend.git
```
7. Telepitsd a szükséges python csomagokat a következő parancsokkal:
```bash
pip install pipenv
pipenv install
```
8. Nyisd meg a Visual Studio Code programot!
9. Menj rá az "Extensions" (CTRL+SHIFT+X) fülre és telepitsd a következő extensionöket (ird be őket a keresőbe):
    1. python
    2. Docker
    3. Jinja2 Snippet Kit
    4. Visual Studio IntelliCode
10. A VSCode programban nyisd meg a projekt mappáját (CTRL+K, CTRL+O a billentyűparancs)!
11. Folyt. köv., valószinűleg eddig se nagyon lehet ez alapján eljutni idáig...
