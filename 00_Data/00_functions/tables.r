# Setup
suppressPackageStartupMessages(library(dplyr))
suppressPackageStartupMessages(library(tidyselect))
suppressPackageStartupMessages(library(tidyr))
suppressPackageStartupMessages(library(readr))

# Economy

df_train <- read_csv("00_Data/01_data/trainingsdaten_manibert_27022022.csv") %>%
    group_by(label) %>%
    summarise(n=n())

print(df_train,n=100)

df_val <- read_csv("00_Data/01_data/validierungsdaten_manibert_27022022.csv") %>%
    group_by(label) %>%
    summarise(n=n())

print(df_val,n=100)

df_test <- read_csv("00_Data/01_data/testdaten_manibert_27022022.csv") %>%
    group_by(label) %>%
    summarise(n=n())

print(df_test,n=100)
