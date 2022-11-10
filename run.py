"""
Description:
    Script for running text contradiction analysis
"""

from text_contradiction import TextContradiction

def main():
    # Set initial statement and a follow up comment to be checked for contradiction
    paragraph = "I do not like ice cream. I like cars. I hate ice cream."
    initial_statement = "I love chocolate"
    followup_statement = "I hate chocolate ice cream"
    categories = ["food", "drink", "sports"]

    # Call API to load models and perform text analysis
    tc = TextContradiction()
    tc.load_tokenizer()
    prob_contradiction, prob_no_contradiction, prob_neutral = tc.analyse_text(paragraph)

    # Classify text
    category_probabilities = tc.classify_text(initial_statement, categories)
    print(category_probabilities)

    # Make prediction about contradiction
    if prob_neutral > prob_contradiction and prob_neutral > prob_no_contradiction:
        print(f"Sentences are unrelated with a probability: {prob_neutral}")
    else:
        if prob_contradiction > prob_no_contradiction:
            print(f"Contradiction Detected with a probability of: {prob_contradiction}")
        else:
            print(f"No Contradiction Detected with a probability of: {prob_no_contradiction}")
        

if __name__ == "__main__":
    main()