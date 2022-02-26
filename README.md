# ManiBERT

ManiBERT ist der Test des LCPN-Ansatzes im Kontext des Manifesto Projects.

Es besteht daher zunächst aus [PolicyBERTa](https://github.com/NiksMer/PolicyBERTa), einem Modell zur Vorhersage der sieben Policy-Domänen.
Sofern nun die wirtschaftliche Policy-Domäne vorhergesagt wurde, werden die Daten durch ManiBERT in die wirtschaftlichen Kategorien eingeteilt. Sollte es um Protektionismus gehen, erfolgt noch eine Aufschlüsselung in eine Pro- oder Kontra-Position.

ManiBERT umfasst dabei das Modell zur Einstufung in die 15 wirtschaftlichen Themengebiete und das Modell zur Klassifizierung der Position zum Protektionismus.

## Wirtschaftliche Themen

### Trainingsdatensatz

| economy | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 87.511 |
| 1       | Freie Unternehmen                         | 1.769  |
| 2       | Anreize: Positiv                          | 3.119  |
| 3       | Marktregulation                           | 3.522  |
| 4       | Wirtschaftliche Planung                   | 533    |
| 5       | Korporatismus/Gemischte Wirtschaft        | 197    |
| 6       | Protektionismus                           | 1.346  |
| 7       | Wirtschaftliche Ziele                     | 817    |
| 8       | Keynesianisches Nachfragemanagement       | 152    |
| 9       | Wirtschaftliches Wachstum: Positiv        | 3.196  |
| 10      | Technologie und Infrastruktur: Positiv    | 8.645  |
| 11      | Kontrollierte Wirtschaft                  | 569    |
| 12      | Verstaatlichungen                         | 845    |
| 13      | Wirtschaftliche Orthodoxie                | 1.723  |
| 14      | Marxistische Analysen: Positiv            | 146    |
| 15      | Anti-Wachstumsökonomie und Nachhaltigkeit | 2.626  |

### Validierungsdatensatz

| economy | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 15.444 |
| 1       | Freie Unternehmen                         | 308  |
| 2       | Anreize: Positiv                          | 525  |
| 3       | Marktregulation                           | 656  |
| 4       | Wirtschaftliche Planung                   | 93    |
| 5       | Korporatismus/Gemischte Wirtschaft        | 28    |
| 6       | Protektionismus                           | 231  |
| 7       | Wirtschaftliche Ziele                     | 139    |
| 8       | Keynesianisches Nachfragemanagement       | 33    |
| 9       | Wirtschaftliches Wachstum: Positiv        | 553  |
| 10      | Technologie und Infrastruktur: Positiv    | 1.527  |
| 11      | Kontrollierte Wirtschaft                  | 94    |
| 12      | Verstaatlichungen                         | 144    |
| 13      | Wirtschaftliche Orthodoxie                | 285  |
| 14      | Marxistische Analysen: Positiv            | 35   |
| 15      | Anti-Wachstumsökonomie und Nachhaltigkeit | 502  |
### Testdatensatz

| economy | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 6.155 |
| 1       | Freie Unternehmen                         | 53  |
| 2       | Anreize: Positiv                          | 81  |
| 3       | Marktregulation                           | 210  |
| 4       | Wirtschaftliche Planung                   | 67    |
| 5       | Korporatismus/Gemischte Wirtschaft        | 23    |
| 6       | Protektionismus                           | 329  |
| 7       | Wirtschaftliche Ziele                     | 148    |
| 8       | Keynesianisches Nachfragemanagement       | 9    |
| 9       | Wirtschaftliches Wachstum: Positiv        | 374  |
| 10      | Technologie und Infrastruktur: Positiv    | 339  |
| 11      | Kontrollierte Wirtschaft                  | 94    |
| 12      | Verstaatlichungen                         | 27    |
| 13      | Wirtschaftliche Orthodoxie                | 184  |
| 14      | Marxistische Analysen: Positiv            | 0  |
| 15      | Anti-Wachstumsökonomie und Nachhaltigkeit | 250  |

## Protektionismus


### Trainingsdaten

| protectionism | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 115.370 |
| 1       | Protektionismus: Positiv                  | 641  |
| 2       | Protektionismus: Negativ                  | 705  |

### Validierungsdaten

| protectionism | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 20.366 |
| 1       | Protektionismus: Positiv                  | 95  |
| 2       | Protektionismus: Negativ                  | 136  |

### Testdaten

| protectionism | Beschreibung                              | Anzahl |
|---------|-------------------------------------------|--------|
| 0       | Keine Kategorie                           | 8.014 |
| 1       | Protektionismus: Positiv                  | 180  |
| 2       | Protektionismus: Negativ                  | 149  |