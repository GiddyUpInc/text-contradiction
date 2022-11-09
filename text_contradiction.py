"""
Description:
    Class to provide interface with other tools.
"""

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class TextContradiction:
    def __init__(self):
        pass

    def load_tokenizer(self):
        """Load text classifier"""
        print("Loading classifier...")
        self.nli_model = AutoModelForSequenceClassification.from_pretrained('facebook/bart-large-mnli')
        self.tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-mnli')

    def analyse_text(self, premise, hypothesis):
        # run through model pre-trained on MNLI
        x = self.tokenizer.encode(premise, hypothesis, return_tensors='pt')
        logits = self.nli_model(x)[0]

        # we throw away "neutral" (dim 1) and take the probability of
        # "entailment" (2) as the probability of the label being true 
        entail_contradiction_logits = logits[:,[0,1,2]]
        probs = entail_contradiction_logits.softmax(dim=1)
        prob_no_contradiction = probs[:,1]
        prob_no_contradiction = torch.tensor_split(prob_no_contradiction, 2)[0]

        prob_contradiction = 1 - prob_no_contradiction

        return prob_contradiction
