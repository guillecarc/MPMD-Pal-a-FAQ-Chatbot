library(jsonlite)
library(tidyverse)


data <- read_json(path = "OneDrive/Added_Business_Value_of_implementing_Chatbots/Proof_of_concept/MPMD_Pal_V2/training_dataset_1560747506.json")

data_t <- transpose(data$rasa_nlu_data$common_examples)

intents <- unlist(data_t$intent)
text <- unlist(data_t$text)

mapping_file <- cbind(intents, text) %>% as.data.frame(stringsAsFactors = FALSE)

mapping_file %>% 
  group_by(intents) %>% 
  summarise(count = n())
