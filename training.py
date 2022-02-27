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
trained_model_name = "ManiBERT"

## Max Sequence Length
max_lengh_parameter = 514

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
warmup_steps_parameter = 0

## weight_decay
weight_decay_parameter = 0.1

## learning_rate
learning_rate_parameter = 1e-05

## Log file
log_name = 'log_manibert.json'

## Report
validatipon_report_name = 'validation_report_manibert.txt'
test_report_name = 'test_report_manibert.txt'

####### Data Config ############

## Train Data
train_data = "00_Data/01_data/trainingsdaten_manibert_27022022.csv"

## Valid Data
valid_data = "00_Data/01_data/validierungsdaten_manibert_27022022.csv"

## Test Data
test_data = "00_Data/01_data/testdaten_manibert_27022022.csv"

## Delimeter
delimeter_char = ","

## Label Names
label_names = ["external relations","freedom and democracy","political system","economy","welfare and quality of life","fabric of society","social groups"]

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
# config
config = RobertaConfig(model_to_use)
config.id2label = {
    "0": "external relations",
    "1": "freedom and democracy",
    "2": "political system",
    "3": "economy",
    "4": "welfare and quality of life",
    "5": "fabric of society",
    "6": "social groups"}
config.label2id = {
    "external relations": 0,
    "freedom and democracy": 1,
    "political system": 2,
    "economy": 3,
    "welfare and quality of life": 4,
    "fabric of society": 5,
    "social groups": 6    
}

# Tokenizer
tokenizer = RobertaTokenizer.from_pretrained(model_to_use,config=config,model_max_length=max_lengh_parameter)
tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)

# %%
# Trainer Argumente
training_args = TrainingArguments(
    output_dir=trained_model_name,
    warmup_steps=warmup_steps_parameter,
    weight_decay=weight_decay_parameter, 
    learning_rate=learning_rate_parameter,
    fp16 = True,
    evaluation_strategy="epoch",
    num_train_epochs=epoch_count,
    per_device_train_batch_size=batch_size,
    overwrite_output_dir=True,
    per_device_eval_batch_size=batch_size,
    save_strategy="epoch",
    logging_dir='logs',   
    logging_strategy= 'steps',     
    logging_steps=10)

# %%
# Modell laden
model = RobertaForSequenceClassification.from_pretrained(model_to_use, num_labels=label_count)

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
trainer.save_model (trained_model_name)

# %%
