"""
Description:
    Script for running text contradiction analysis
"""

from text_contradiction import TextContradiction

def main():
    # Set initial statement and a follow up comment to be checked for contradiction
    initial_statement = "I do not like chocolate"
    followup_statement = "I like ice cream"

    # Call API to load models and perform text analysis
    tc = TextContradiction()
    tc.load_tokenizer()
    prob_contradiction, prob_neutral = tc.analyse_text(initial_statement, followup_statement)

    # Make prediction about contradiction
    if prob_neutral > 0.5:
        print(f"Sentences are unrelated - probability: {prob_neutral}")
    else:
        if prob_contradiction > 0.5:
            print(f"Contradiction Detected with a probability of: {prob_contradiction}")
        else:
            print(f"No Contradiction Detected with a probability of: {1 - prob_contradiction}")
        

if __name__ == "__main__":
    main()