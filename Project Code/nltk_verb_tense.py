from nltk import word_tokenize, pos_tag

def get_verb_tenses(sentence):
    tokenized_txt = word_tokenize(sentence)
    pos_tagged = pos_tag(tokenized_txt)
    tense = {"sequence": [], "tenses": {}, "words": []}
    for i, word in enumerate(pos_tagged):
        current_tense = ""
        if word[1] == "MD":
            current_tense = "future"
        elif word[1] in ["VBP", "VBZ", "VBG"]:
            current_tense = "present"
        elif word[1] in ["VBD", "VBN"]:
            current_tense = "past"
            
        if current_tense != "":
            tense["sequence"].append(current_tense)
            if current_tense in tense["tenses"]:
                tense["tenses"][current_tense] += 1
            else:
                tense["tenses"][current_tense] = 1
            tense["words"].append((i, word[0], current_tense))
    return tense, pos_tagged

def test():
    text1 = "He will have been doing his homework."
    x = get_verb_tenses(text1)
    text2 = "She has been trying to learn French for one month."
    y = get_verb_tenses(text2)
    #text3 = "I did not wish to talk to you about that matter."
    text3 = "It will rain tomorrow."
    z = get_verb_tenses(text3)
    print("Tense sequence: ", "\n\n", x, "\n\n", y, "\n\n", z)
    #print("Total tenses: ", "\n", len_x, "\n", len_y, "\n", len_z)

if __name__ == "__main__":
    test()
# ***EXTRA****
# MD  Modal verb (can, could, may, must)
# VB  Base verb (take)
# VBC Future tense, conditional
# VBD Past tense (took)
# VBF Future tense
# VBG Gerund, present participle (taking)
# VBN Past participle (taken)
# VBP Present tense (take)
# VBZ Present 3rd person singular (takes)

# Future_Perfect_Continuous: {<MD><VB><VBN><VBG>}
# Future_Continuous:         {<MD><VB><VBG>}
# Future_Perfect:            {<MD><VB><VBN>}
# Past_Perfect_Continuous:   {<VBD><VBN><VBG>}
# Present_Perfect_Continuous:{<VBP|VBZ><VBN><VBG>}
# Future_Indefinite:         {<MD><VB>}
# Past_Continuous:           {<VBD><VBG>}
# Past_Perfect:              {<VBD><VBN>}
# Present_Continuous:        {<VBZ|VBP><VBG>}
# Present_Perfect:           {<VBZ|VBP><VBN>}
# Past_Indefinite:           {<VBD>}
# Present_Indefinite:        {<VBZ>|<VBP>}