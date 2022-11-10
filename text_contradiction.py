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
        print("Finished loading classifier.")

    def analyse_two_statements(self, premise, hypothesis):
        # run through model pre-trained on MNLI
        x = self.tokenizer.encode(premise, hypothesis, return_tensors='pt')
        logits = self.nli_model(x.to('gpu'))[0]

        # "entailment" is the probability of each category
        entail_contradiction_logits = logits[:,:]
        probs = entail_contradiction_logits.softmax(dim=1)
        probabilities = probs.data[0,:]
        probabilities = probabilities.tolist()
        prob_contradiction, prob_neutral, prob_no_contradiction = probabilities[:]
        
        return prob_contradiction, prob_no_contradiction, prob_neutral

    def analyse_text(self, paragraph):
        # run through model pre-trained on MNLI
        x = self.tokenizer.encode(paragraph, return_tensors='pt')
        logits = self.nli_model(x.to('cpu'))[0]

        # "entailment" is the probability of each category
        entail_contradiction_logits = logits[:]
        probs = entail_contradiction_logits.softmax(dim=1)
        probabilities = probs.data[0,:]
        probabilities = probabilities.tolist()
        prob_contradiction, prob_neutral, prob_no_contradiction = probabilities[:]
        
        return prob_contradiction, prob_no_contradiction, prob_neutral