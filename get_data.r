# Setup
suppressPackageStartupMessages(library(dplyr))
suppressPackageStartupMessages(library(tidyselect))
suppressPackageStartupMessages(library(tidyr))
suppressPackageStartupMessages(library(readr))

# CSV aus Github laden
df_roh <- read_csv("https://raw.githubusercontent.com/NiksMer/get_manifesto_data/main/complete_data.csv")

## Wirtschaft Allgemein

### Filtern auf Trainingsdaten.
df_economy_roh <- df_roh %>%
    select(text,economy)


### 80% Trainingsgröße
smp_size <- floor(0.8 * nrow(df_economy_roh))

### Seed definieren für Reproduzierbarkeit
set.seed(123)
train_ind <- sample(seq_len(nrow(df_economy_roh)), size = smp_size)

### Daten schneiden
df_economy_train <- df_economy_roh[train_ind, ]
df_economy_test <- df_economy_roh[-train_ind, ]

### Daten speichern
write_csv(df_economy_train,"00_Economy/trainingsdaten_economy_24022022.csv")
write_csv(df_economy_test, "00_Economy/testdaten_economy_24022022.csv")

###################

## Protektionismus
df_protectionism_roh <- df_roh %>%
    select(text,protectionism)


### 80% Trainingsgröße
smp_size <- floor(0.8 * nrow(df_protectionism_roh))

### Seed definieren für Reproduzierbarkeit
set.seed(123)
train_ind <- sample(seq_len(nrow(df_protectionism_roh)), size = smp_size)

### Daten schneiden
df_protectionism_train <- df_protectionism_roh[train_ind, ]
df_protectionism_test <- df_protectionism_roh[-train_ind, ]

### Daten speichern
write_csv(df_protectionism_train,"01_Protectionism/trainingsdaten_protectionism_24022022.csv")
write_csv(df_protectionism_test, "01_Protectionism/testdaten_protectionism_24022022.csv")
