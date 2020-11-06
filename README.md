Instrukcja uruchomienia

### `python3 main.py (-cpu | -gpu | -cpu_test | -gpu_test) [-path PATH | -auto AUTOGENERATE]`

Uruchomienie zliczania samogłosek sekwencyjnie na CPU

### `python3 main.py -cpu`

Uruchomienie wersji zrównoleglonej na GPU

### `python3 main.py -gpu`

Uruchomienie testów wersji na CPU

### `python3 main.py -cpu_test`

Uruchomienie testów wersji na GPU

### `python3 main.py -gpu_test`

Domyślnie wszystkie tryby wykonują się na domyślnym tekscie. Można to zmienić używając flag:

### `-path PATH`

gdzie PATH jest ścieżką do pliku tekstowego, który ma zostać wczytany

### `-auto AUTOGENERATE`

gdzie AUTOGENERATE to wielkość tekstu w MB, który ma zostać wygenerowany automatycznie.


przykłady uruchomienia

### `python3 -cpu -auto 500`

wygeneruje tekst o wielkości 500MB i uruchomi zliczanie głosek w tym tekście w wersji na CPU

### `python3 -gpu -path './text/textfile.txt'

wczyta podany tekst i uruchomi zliczanie głosek w tym tekście w wersji na GPU

