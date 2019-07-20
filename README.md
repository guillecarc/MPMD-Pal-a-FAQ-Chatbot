# MPMD Pal: a FAQ Chatbot

The desing of the chatbot is better represented in the two tables below:

## Product Sheet

|Element|Details |
|---|---|
|**Name:**|MPMD pal|
|**Type:**|Frequently Asked Questions (FAQ)|
|**Purpose:**|Solve questions based on [MPMD HTW Website]("https://mpmd.htw-berlin.de/")|
|**Role:**|Support MPMD staff by answering basic queries to any in-terested person and referring them to contact a given mail if the bot cannot answer the questions.|
|**Audience:**|Any interested person in the program, commonly people between ~25-35 years.|
|**Features:**|Text-only interphase.|
|**Preferred devices:**|Any device capable of using Facebook, commonly desktops, laptops, mobiles, and tablets.|
|**Development framework:**|Rasa 1.1.4|
|**Programming language:**|Python 3.6|

## Technical Sheet

|Element|Details|
|---|---:|
|**Conversational AI**|
|**Type:**|Retrieval-based|
|**Intents:**|20|
|**Utterances per intent:**|~100|
|**Stories:**|1|
|**Rasa NLU**|
|**Pipeline:**|Supervised Embeddings|
|**Tokenizer:**|Whitespace|
|**Intent Classifier Model:**|Neural Embedding|
|**Rasa Core**|
|**Dialogue predictor model:**|Mapping Policy|
|**Iniciative:**|Managed by the user|
|**Restart dialogue:**|Mapping Policy|
|**Grounding:**|Fallback policy|

## Further considerations and development

+ The Chatbot's architecture is designed to exclude all mapped intents from the dialogue predictions.
+ After each action, an "action_listen" is forced.
