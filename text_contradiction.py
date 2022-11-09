"""
Description:
    Class to provide interface with other tools.
"""

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

        # "entailment" (2) is the probability of the label being true 
        entail_contradiction_logits = logits[:,[0,2]]
        probs = entail_contradiction_logits.softmax(dim=1)
        prob_no_contradiction = probs[:,1]
        prob_no_contradiction = prob_no_contradiction.tolist()[0]

        prob_contradiction = 1 - prob_no_contradiction

        # "neutral" (dim 1) is the probability the premise and hypothesis are not related
        entail_neutral_logits = logits[:,[0,1]]
        probs = entail_neutral_logits.softmax(dim=1)
        prob_neutral = probs[:,1]
        prob_neutral = prob_neutral.tolist()[0]

        return prob_contradiction, prob_neutral
