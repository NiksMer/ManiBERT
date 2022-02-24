# Setup
suppressPackageStartupMessages(library(dplyr))
suppressPackageStartupMessages(library(tidyselect))
suppressPackageStartupMessages(library(tidyr))
suppressPackageStartupMessages(library(readr))

# Economy

df_economy_train <- read_csv("00_Economy/trainingsdaten_economy_24022022.csv") %>%
    group_by(economy) %>%
    summarise(n=n())

print(df_economy_train)

df_economy_val <- read_csv("00_Economy/validierungsdaten_economy_24022022.csv") %>%
    group_by(economy) %>%
    summarise(n=n())

print(df_economy_val)

df_economy_test <- read_csv("00_Economy/testdaten_economy_24022022.csv") %>%
    group_by(economy) %>%
    summarise(n=n())

print(df_economy_test)

# Protektionismus

df_protectionism_train <- read_csv("01_Protectionism/trainingsdaten_protectionism_24022022.csv") %>%
    group_by(protectionism) %>%
    summarise(n=n())

print(df_protectionism_train)

df_protectionism_val <- read_csv("01_Protectionism/validierungsdaten_protectionism_24022022.csv") %>%
    group_by(protectionism) %>%
    summarise(n=n())

print(df_protectionism_val)

df_protectionism_test<- read_csv("01_Protectionism/testdaten_protectionism_24022022.csv") %>%
    group_by(protectionism) %>%
    summarise(n=n())

print(df_protectionism_test)
