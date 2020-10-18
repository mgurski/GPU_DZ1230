Instrukcja uruchomienia

### `python3 main.py (-cpu | -gpu | -cpu_test | -gpu_test) [-path PATH | -auto AUTOGENERATE]`
<br/>
Uruchomienie zliczania samogłosek sekwencyjnie na CPU

### `python3 main.py -cpu`
<br/>
Uruchomienie wersji zrównoleglonej na GPU

### `python3 main.py -gpu`
<br/>
Uruchomienie testów wersji na CPU. Zwraca plik csv lub txt(zobaczymy) oraz ewentualnie generuje wykres(zobaczymy).

### `python3 main.py -cpu_test`
<br/>
Uruchomienie testów wersji na GPU. Zwraca plik csv lub txt(zobaczymy) oraz eweneutlanie generuje wykres(zobaczymy).

### `python3 main.py -gpu_test`
<br/>
Domyślnie wszystkie tryby wykonują się na domyślnym tekscie. Można to zmienić używając flag:

<br/>

### `-path PATH`
gdzie PATH jest ścieżką do pliku tekstowego, który ma zostać wczytany

<br/>

### `-auto AUTOGENERATE`
gdzie AUTOGENERATE to wielkość tekstu w MB, który ma zostać wygenerowany automatycznie.

<br/>

przykłady uruchomienia
<br/>

### `python3 -cpu -auto 500`
wygeneruje tekst o wielkości 500MB i uruchomi zliczanie głosek w tym tekście w wersji na CPU

### `python3 -gpu -path './text/textfile.txt'`
wczyta podany tekst i uruchomi zliczanie głosek w tym tekście w wersji na GPU

