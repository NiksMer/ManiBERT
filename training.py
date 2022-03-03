# %%
# Setup

## Packages
import pandas as pd
import numpy as np
import torch
from transformers import RobertaForSequenceClassification, TrainingArguments, Trainer, RobertaTokenizer, RobertaConfig
from datasets import load_metric, load_dataset
from sklearn.metrics import precision_recall_fscore_support, accuracy_score, classification_report
from tqdm import tqdm

## Cuda
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
n_gpu = torch.cuda.device_count()


####### Model Config ############

## Modelname
model_to_use = "roberta-base"
trained_model_name = "ManiBERT_v2"

## Max Sequence Length
max_lengh_parameter = 512

## Anzahl Labels
label_count = 56

## Anzahl Epochs
if n_gpu > 1 :
    epoch_count = 5
else:
    epoch_count = 1

## Batch Size
if n_gpu > 1 :
    batch_size = 16
else:
    batch_size = 4

## warmup_steps
warmup_ratio_parameter = 0.05

## weight_decay
weight_decay_parameter = 0.1

## learning_rate
learning_rate_parameter = 5e-05

## Log file
log_name = '01_Report/log_manibert.json'

## Report
validatipon_report_name = '01_Report/validation_report_manibert.txt'
test_report_name = '01_Report/test_report_manibert.txt'

####### Data Config ############

## Train Data
train_data = "00_Data_intern/01_data/trainingsdaten_manibert_27022022.csv"

## Valid Data
valid_data = "00_Data_intern/01_data/validierungsdaten_manibert_27022022.csv"

## Test Data
test_data = "00_Data_intern/01_data/testdaten_manibert_27022022.csv"

## Delimeter
delimeter_char = ","

## Label Names
label_names = [
"Foreign Special Relationships: Positive",
"Foreign Special Relationships: Negative",
"Anti-Imperialism",
"Military: Positive",
"Military: Negative",
"Peace",
"Internationalism: Positive",
"European Community/Union or Latin America Integration: Positive",
"Internationalism: Negative",
"European Community/Union or Latin America Integration: Negative",
"Freedom and Human Rights",
"Democracy",
"Constitutionalism: Positive",
"Constitutionalism: Negative",
"Decentralisation: Positive",
"Centralisation: Positive",
"Governmental and Administrative Efficiency",
"Political Corruption",
"Political Authority",
"Free Market Economy",
"Incentives: Positive",
"Market Regulation",
"Economic Planning",
"Corporatism/ Mixed Economy",
"Protectionism: Positive",
"Protectionism: Negative",
"Economic Goals",
"Keynesian Demand Management",
"Economic Growth: Positive",
"Technology and Infrastructure: Positive",
"Controlled Economy",
"Nationalisation",
"Economic Orthodoxy",
"Marxist Analysis: Positive",
"Anti-Growth Economy and Sustainability",
"Environmental Protection",
"Culture: Positive",
"Equality: Positive",
"Welfare State Expansion",
"Welfare State Limitation",
"Education Expansion",
"Education Limitation",
"National Way of Life: Positive",
"National Way of Life: Negative",
"Traditional Morality: Positive",
"Traditional Morality: Negative",
"Law and Order",
"Civic Mindedness: Positive",
"Multiculturalism: Positive",
"Multiculturalism: Negative",
"Labour Groups: Positive",
"Labour Groups: Negative",
"Agriculture and Farmers",
"Middle Class and Professional Groups",
"Underprivileged Minority Groups",
"Non-economic Demographic Groups"
]

## Config Dicts
id2label_parameter = {
    "0": "Foreign Special Relationships: Positive",
    "1": "Foreign Special Relationships: Negative",
    "2": "Anti-Imperialism",
    "3": "Military: Positive",
    "4": "Military: Negative",
    "5": "Peace",
    "6": "Internationalism: Positive",
    "7": "European Community/Union or Latin America Integration: Positive",
    "8": "Internationalism: Negative",
    "9": "European Community/Union or Latin America Integration: Negative",
    "10": "Freedom and Human Rights",
    "11": "Democracy",
    "12": "Constitutionalism: Positive",
    "13": "Constitutionalism: Negative",
    "14": "Decentralisation: Positive",
    "15": "Centralisation: Positive",
    "16": "Governmental and Administrative Efficiency",
    "17": "Political Corruption",
    "18": "Political Authority",
    "19": "Free Market Economy",
    "20": "Incentives: Positive",
    "21": "Market Regulation",
    "22": "Economic Planning",
    "23": "Corporatism/ Mixed Economy",
    "24": "Protectionism: Positive",
    "25": "Protectionism: Negative",
    "26": "Economic Goals",
    "27": "Keynesian Demand Management",
    "28": "Economic Growth: Positive",
    "29": "Technology and Infrastructure: Positive",
    "30": "Controlled Economy",
    "31": "Nationalisation",
    "32": "Economic Orthodoxy",
    "33": "Marxist Analysis: Positive",
    "34": "Anti-Growth Economy and Sustainability",
    "35": "Environmental Protection",
    "36": "Culture: Positive",
    "37": "Equality: Positive",
    "38": "Welfare State Expansion",
    "39": "Welfare State Limitation",
    "40": "Education Expansion",
    "41": "Education Limitation",
    "42": "National Way of Life: Positive",
    "43": "National Way of Life: Negative",
    "44": "Traditional Morality: Positive",
    "45": "Traditional Morality: Negative",
    "46": "Law and Order",
    "47": "Civic Mindedness: Positive",
    "48": "Multiculturalism: Positive",
    "49": "Multiculturalism: Negative",
    "50": "Labour Groups: Positive",
    "51": "Labour Groups: Negative",
    "52": "Agriculture and Farmers",
    "53": "Middle Class and Professional Groups",
    "54": "Underprivileged Minority Groups",
    "55": "Non-economic Demographic Groups"
    }
label2id_parameter = {
    "Foreign Special Relationships: Positive": 0,
    "Foreign Special Relationships: Negative": 1,
    "Anti-Imperialism": 2,
    "Military: Positive": 3,
    "Military: Negative": 4,
    "Peace": 5,
    "Internationalism: Positive": 6,
    "European Community/Union or Latin America Integration: Positive": 7,
    "Internationalism: Negative": 8,
    "European Community/Union or Latin America Integration: Negative": 9,
    "Freedom and Human Rights": 10,
    "Democracy": 11,
    "Constitutionalism: Positive": 12,
    "Constitutionalism: Negative": 13,
    "Decentralisation: Positive": 14,
    "Centralisation: Positive": 15,
    "Governmental and Administrative Efficiency": 16,
    "Political Corruption": 17,
    "Political Authority": 18,
    "Free Market Economy": 19,
    "Incentives: Positive": 20,
    "Market Regulation": 21,
    "Economic Planning": 22,
    "Corporatism/ Mixed Economy": 23,
    "Protectionism: Positive": 24,
    "Protectionism: Negative": 25,
    "Economic Goals": 26,
    "Keynesian Demand Management": 27,
    "Economic Growth: Positive": 28,
    "Technology and Infrastructure: Positive": 29,
    "Controlled Economy": 30,
    "Nationalisation": 31,
    "Economic Orthodoxy": 32,
    "Marxist Analysis: Positive": 33,
    "Anti-Growth Economy and Sustainability": 34,
    "Environmental Protection": 35,
    "Culture: Positive": 36,
    "Equality: Positive": 37,
    "Welfare State Expansion": 38,
    "Welfare State Limitation": 39,
    "Education Expansion": 40,
    "Education Limitation": 41,
    "National Way of Life: Positive": 42,
    "National Way of Life: Negative": 43,
    "Traditional Morality: Positive": 44,
    "Traditional Morality: Negative": 45,
    "Law and Order": 46,
    "Civic Mindedness: Positive": 47,
    "Multiculturalism: Positive": 48,
    "Multiculturalism: Negative": 49,
    "Labour Groups: Positive": 50,
    "Labour Groups: Negative": 51,
    "Agriculture and Farmers": 52,
    "Middle Class and Professional Groups": 53,
    "Underprivileged Minority Groups": 54,
    "Non-economic Demographic Groups": 55
}

####### Functions ############

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

## Neue Metrics function: https://huggingface.co/transformers/v3.0.2/training.html#trainer
def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1_micro, _ = precision_recall_fscore_support(labels, preds, average='micro')
    precision2, recall3, f1_macro, _ = precision_recall_fscore_support(labels, preds, average='macro')
    precision3, recall4, f1_weighted, _ = precision_recall_fscore_support(labels, preds, average='weighted')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'f1-micro': f1_micro,
        'f1-macro': f1_macro,
        'f1-weighted': f1_weighted,
        'precision': precision,
        'recall': recall
    }

# %%
# Daten laden
raw_datasets  = load_dataset('csv',data_files={'train':[train_data],'validation':[valid_data],'test': [test_data]},delimiter=delimeter_char)

# %%
# Tokenizer
RobertaTokenizer.from_pretrained(
    model_to_use,
    model_max_length=max_lengh_parameter
    ).save_pretrained(trained_model_name)
tokenizer = RobertaTokenizer.from_pretrained(
    model_to_use,
    model_max_length=max_lengh_parameter
    )
tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)

# %%
# Trainer Argumente
training_args = TrainingArguments(
    output_dir=trained_model_name,
    warmup_ratio=warmup_ratio_parameter,
    weight_decay=weight_decay_parameter, 
    learning_rate=learning_rate_parameter,
    fp16 = True,
    evaluation_strategy="epoch",
    num_train_epochs=epoch_count,
    per_device_train_batch_size=batch_size,
    overwrite_output_dir=True,
    per_device_eval_batch_size=batch_size,
    save_strategy="no",
    logging_dir='logs',   
    logging_strategy= 'steps',     
    logging_steps=10,
    push_to_hub=True,
    hub_strategy="end")

# %%
# Modell laden
model = RobertaForSequenceClassification.from_pretrained(
    model_to_use, 
    num_labels=label_count,
    id2label=id2label_parameter,
    label2id=label2id_parameter
    )

# %%
# Trainer definieren
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    compute_metrics=compute_metrics,
)

# %%
# Trainieren
trainer.train()

# %%
# Evaluate for Classification Report
## Validation
predictions, labels, _ = trainer.predict(tokenized_datasets["validation"])
predictions = np.argmax(predictions, axis=1)
with open(validatipon_report_name,'w',encoding='utf-8') as f:
    f.truncate(0) # Vorher File leeren
    f.write(classification_report(y_pred=predictions,y_true=labels,target_names=label_names))

# %%
# Evaluate for Classification Report
## Test
predictions, labels, _ = trainer.predict(tokenized_datasets["test"])
predictions = np.argmax(predictions, axis=1)
with open(test_report_name,'w',encoding='utf-8') as f:
    f.truncate(0) # Vorher File leeren
    f.write(classification_report(y_pred=predictions,y_true=labels,target_names=label_names))
# %% 
# Abspeichern

## Log speichern
with open(log_name, 'w',encoding='utf-8') as f:
    f.truncate(0) # Vorher File leeren
    for obj in trainer.state.log_history:
        f.write(str(obj)+'\n')

## Modell speichern
trainer.save_model(trained_model_name)
tokenizer.save_pretrained(trained_model_name, push_to_hub=True)
# %%

