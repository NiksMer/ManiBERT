# ManiBERT

ManiBERT ist der Test des LCPN-Ansatzes im Kontext des Manifesto Projects.

Es besteht daher zunächst aus [PolicyBERTa](https://github.com/NiksMer/PolicyBERTa), einem Modell zur Vorhersage der sieben Policy-Domänen.
Sofern nun die wirtschaftliche Policy-Domäne vorhergesagt wurde, werden die Daten durch ManiBERT in die wirtschaftlichen Kategorien eingeteilt. Sollte es um Protektionismus gehen, erfolgt noch eine Aufschlüsselung in eine Pro- oder Kontra-Position.

ManiBERT umfasst dabei das Modell zur Einstufung in die 15 wirtschaftlichen Themengebiete und das Modell zur Klassifizierung der Position zum Protektionismus.

## Wirtschaftliche Themen

### Trainingsdatensatz

| economy | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 79.831 |
| 1       | Freie Unternehmen                         | 1.665  |
| 2       | Anreize: Positiv                          | 2.882  |
| 3       | Marktregulation                           | 3.230  |
| 4       | Wirtschaftliche Planung                   | 510    |
| 5       | Korporatismus/Gemischte Wirtschaft        | 180    |
| 6       | Protektionismus                           | 1.192  |
| 7       | Wirtschaftliche Ziele                     | 755    |
| 8       | Keynesianisches Nachfragemanagement       | 148    |
| 9       | Wirtschaftliches Wachstum: Positiv        | 2.878  |
| 10      | Technologie und Infrastruktur: Positiv    | 7.928  |
| 11      | Kontrollierte Wirtschaft                  | 524    |
| 12      | Verstaatlichungen                         | 743    |
| 13      | Wirtschaftliche Orthodoxie                | 1.570  |
| 14      | Marxistische Analysen: Positiv            | 147    |
| 15      | Anti-Wachstumsökonomie und Nachhaltigkeit | 2.456  |

### Validierungsdatensatz

| economy | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 19.936 |
| 1       | Freie Unternehmen                         | 407  |
| 2       | Anreize: Positiv                          | 679  |
| 3       | Marktregulation                           | 844  |
| 4       | Wirtschaftliche Planung                   | 116    |
| 5       | Korporatismus/Gemischte Wirtschaft        | 45    |
| 6       | Protektionismus                           | 308  |
| 7       | Wirtschaftliche Ziele                     | 181    |
| 8       | Keynesianisches Nachfragemanagement       | 35    |
| 9       | Wirtschaftliches Wachstum: Positiv        | 726  |
| 10      | Technologie und Infrastruktur: Positiv    | 1.982  |
| 11      | Kontrollierte Wirtschaft                  | 129    |
| 12      | Verstaatlichungen                         | 219    |
| 13      | Wirtschaftliche Orthodoxie                | 372  |
| 14      | Marxistische Analysen: Positiv            | 34   |
| 15      | Anti-Wachstumsökonomie und Nachhaltigkeit | 647  |
### Testdatensatz

| economy | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 9.343 |
| 1       | Freie Unternehmen                         | 58  |
| 2       | Anreize: Positiv                          | 164  |
| 3       | Marktregulation                           | 314  |
| 4       | Wirtschaftliche Planung                   | 67    |
| 5       | Korporatismus/Gemischte Wirtschaft        | 23    |
| 6       | Protektionismus                           | 406  |
| 7       | Wirtschaftliche Ziele                     | 168    |
| 8       | Keynesianisches Nachfragemanagement       | 11    |
| 9       | Wirtschaftliches Wachstum: Positiv        | 519  |
| 10      | Technologie und Infrastruktur: Positiv    | 601  |
| 11      | Kontrollierte Wirtschaft                  | 104    |
| 12      | Verstaatlichungen                         | 54    |
| 13      | Wirtschaftliche Orthodoxie                | 250  |
| 14      | Marxistische Analysen: Positiv            | 0  |
| 15      | Anti-Wachstumsökonomie und Nachhaltigkeit | 275  |

## Protektionismus


### Trainingsdaten

| protectionism | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 105.447 |
| 1       | Protektionismus: Positiv                  | 580  |
| 2       | Protektionismus: Negativ                  | 612  |

### Validierungsdaten

| protectionism | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 26.352 |
| 1       | Protektionismus: Positiv                  | 141  |
| 2       | Protektionismus: Negativ                  | 167  |

### Testdaten

| protectionism | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 11.951 |
| 1       | Protektionismus: Positiv                  | 195  |
| 2       | Protektionismus: Negativ                  | 211  |