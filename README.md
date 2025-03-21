# GESTOR DE TASQUES

Aquesta aplicació és un gestor de tasques feta amb Python i MySQL.

Per això s'ha creat una base de dades amb una sola taula que conté totes les tasques que hi anem introduint.

L'aplicació té el següent menú amb 5 opcions diferents que accedeixen a la base de dades i una darrera per sortir de l'aplicació.

Quina opció vols dur a terme?
1. Mostrar tasques
2. Afegir tasques
3. Eliminar tasques
4. Modificar tasques
5. Canviar estat d'una tasca
6. Sortir

Per poder executar l'aplicació cal tenir instal·lada la llibreria mysql-connector-python que podem instal·lar a partir de la següent comanda de pip:

```
pip install mysql-connector-python
```

Un cop instal·lada la llibreria haurem de crear la base de dades corresponent, modificar l'arxiu _constants.py_ amb la informació de la base de dades i, al codi alomillor s'haurpa de modificar el nom de la taula i dels atributs a les consultes si no la heu anomenada com jo _tasklist_.

Per executar l'aplicació és tan senzill com posicionar-mos a la carpeta on tenim ubicats els arxius .py des de consola (cmd a windows o terminal a mac/linux) i executar la següent commanda:

```
python gestorTasques.py
```

Pot haver-hi variacions depenent de la teva instal·lació de python. Si no et reconeix la comanda _python_ pots provar alguna de les següents:

```
python3 gestorTasques.py
```
o
```
py gestorTasques.py
```

