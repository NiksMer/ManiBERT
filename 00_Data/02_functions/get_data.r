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
    select(text,economy,corpus_code) %>%
    dplyr:: filter(!corpus_code %in% c("62110_200810","62320_200406","62320_200601","62320_200810","62420_200406","62420_200601","62420_200810","62623_200406","62623_200601","62623_200810")) %>%
    select(-corpus_code) %>%
    rename(label = economy)

df_economy_test <- df_roh %>%
    select(text,economy,corpus_code) %>%
    dplyr:: filter(corpus_code %in% c("62110_200810","62320_200406","62320_200601","62320_200810","62420_200406","62420_200601","62420_200810","62623_200406","62623_200601","62623_200810")) %>%
    select(-corpus_code) %>%
    rename(label = economy)

### 80% Trainingsgröße
smp_size <- floor(0.85 * nrow(df_economy_roh))

### Seed definieren für Reproduzierbarkeit
set.seed(123)
train_ind <- sample(seq_len(nrow(df_economy_roh)), size = smp_size)

### Daten schneiden
df_economy_train <- df_economy_roh[train_ind, ]
df_economy_val <- df_economy_roh[-train_ind, ]

### Daten speichern
write_csv(df_economy_train,"00_Data/00_Economy/trainingsdaten_economy_26022022.csv")
write_csv(df_economy_val, "00_Data/00_Economy/validierungsdaten_economy_26022022.csv")
write_csv(df_economy_test, "00_Data/00_Economy/testdaten_economy_26022022.csv")

###################

## Protektionismus
df_protectionism_roh <- df_roh %>%
    select(text,protectionism,corpus_code) %>%
    dplyr:: filter(!corpus_code %in% c("62110_200810","62320_200406","62320_200601","62320_200810","62420_200406","62420_200601","62420_200810","62623_200406","62623_200601","62623_200810")) %>%
    select(-corpus_code) %>%
    rename(label = protectionism)

df_protectionism_test <- df_roh %>%
    select(text,protectionism,corpus_code) %>%
    dplyr:: filter(corpus_code %in% c("62110_200810","62320_200406","62320_200601","62320_200810","62420_200406","62420_200601","62420_200810","62623_200406","62623_200601","62623_200810")) %>%
    select(-corpus_code) %>%
    rename(label = protectionism)

### 80% Trainingsgröße
smp_size <- floor(0.85 * nrow(df_protectionism_roh))

### Seed definieren für Reproduzierbarkeit
set.seed(123)
train_ind <- sample(seq_len(nrow(df_protectionism_roh)), size = smp_size)

### Daten schneiden
df_protectionism_train <- df_protectionism_roh[train_ind, ]
df_protectionism_val <- df_protectionism_roh[-train_ind, ]

### Daten speichern
write_csv(df_protectionism_train,"00_Data/01_Protectionism/trainingsdaten_protectionism_26022022.csv")
write_csv(df_protectionism_val,"00_Data/01_Protectionism/validierungsdaten_protectionism_26022022.csv")
write_csv(df_protectionism_test, "00_Data/01_Protectionism/testdaten_protectionism_26022022.csv")
