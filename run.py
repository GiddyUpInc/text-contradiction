"""
Description:
    Script for running text contradiction analysis
"""

from text_contradiction import TextContradiction

def main():
    # Set initial statement and a follow up comment to be checked for contradiction
    initial_statement = "I do not like ice cream"
    followup_statement = "I like cars"

    # Call API to load models and perform text analysis
    tc = TextContradiction()
    tc.load_tokenizer()
    prob_contradiction, prob_no_contradiction, prob_neutral = tc.analyse_text(initial_statement, followup_statement)

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