"""
Description:
    Script for running text contradiction analysis
"""

from text_contradiction import TextContradiction

def main():
    # Create text/sequence to be analysed and categories for classification
    statement = "I don't like vanilla"
    comment = "I like chocolate"

    # Call API to load models and perform text analysis
    tc = TextContradiction()
    tc.load_tokenizer()
    prob_contradiction = tc.analyse_text(statement, comment)

    # Make prediction about contradiction
    if prob_contradiction > 0.5:
        print("Contradiction Detected.")
    else:
        print("No Contradiction Detected.")
        

if __name__ == "__main__":
    main()