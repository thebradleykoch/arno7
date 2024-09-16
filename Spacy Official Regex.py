# Regex: find & replace

import spacy
import re


Input_File_Name = input("Enter input filepath: ")
Output_File_Name = re.sub(r'\.\w*', r' ', Input_File_Name, flags=re.I |
                          re.M) + input("Enter output filename suffix:-") + ".txt"


Speaker1 = 'Kyle'
Speaker2 = 'Kyle'
Speaker3 = 'Bradley'
Speaker4 = 'Speaker4'
Speaker5 = 'Speaker5'


with open(Input_File_Name, 'r') as f:
    content = f.read()


content_0000 = re.sub(r'(\w+:)[\t ]+\((\d\d:\d\d:\d\d)\)[\t ]+\W?[\t ]+', r'\n\n\2\n\1\n',
                      content, flags=re.M | re.I | re.X)  # Correct Reduct-formatted timestamps if applicable
content_000 = re.sub(r'([A-Za-z])[\t ]*\n(\w)', r'\1 \2', content_0000,
                     flags=re.M | re.I | re.X)  # Correct Reduct-formatted spacing if applicable
content_00 = re.sub(r'\[*(\d\d:\d\d:\d\d)\][ \t]*([A-Za-z]+:)[ \t]*',
                    r'\n\n\1\n\2\n', content_000, flags=re.M | re.I | re.X)  # Correct Descript-formatted timestamps if applicable
content_0 = re.sub(r'(Speaker\s+1\s+)(\d\d:\d\d:\d\d)\s+',
                   r'\n\n\2\n{}:\n'.format(Speaker1), content_00, flags=re.M | re.I | re.X)
content_1 = re.sub(r'(Speaker\s+0\s+)(\d\d:\d\d:\d\d)\s+',
                   r'\n\n\2\n{}:\n'.format(Speaker2), content_0, flags=re.M | re.I | re.X)
content_2 = re.sub(r'(Speaker\s+2\s+)(\d\d:\d\d:\d\d)\s+',
                   r'\n\n\2\n{}:\n'.format(Speaker3), content_1, flags=re.M | re.I | re.X)
content_3 = re.sub(r'(Speaker\s+[3-9]\s+)(\d\d:\d\d:\d\d)\s+',
                   r'\n\n\2\n{}:\n'.format(Speaker5), content_2, flags=re.M | re.I | re.X)  # Replace speaker labels with speaker names, place the timecode above the speaker name
content_4 = re.sub(r'(([^A-Za-z])(Uh,*[^-]\s*))|(([^A-Za-z])(Um,*\s*))', r'\2\5',
                   content_3, flags=re.M | re.I | re.X)
content_5 = re.sub(r'(Uhhuh|Uh huh)', r'Uh-huh', content_4, flags=re.M |
                   re.I | re.X)  # Remove filler words
content_6 = re.sub(r'\b(([A-Za-z]+(\'?[A-Za-z]+)?)([ \t]+|,))([ \t]*\1|[ \t]*\2)(\1|\2)*\2*(\b)',
                   r'\2', content_5, flags=re.M | re.I | re.X)
content_7 = re.sub(r'\b(([A-Za-z]+[ \t]?[A-Za-z]*)([ \t]+|,[ \t]+))([ \t]*\1|[ \t]*\2)(\1|\2)*\2*(\b)',
                   r'\2', content_6, flags=re.M | re.I | re.X)  # Remove duplicate words
content_8 = re.sub(r'(?<!\n)(Mm-hmm\.\s<affirmative>(\.|,)*\s*|Mm-hmm(\.|,)*\s*)', r'\n\n\n\1\n\n\n',
                   content_7, flags=re.M | re.I | re.X)  # Attribute affirmative context tags to correct speakers
content_9 = re.sub(r'(\d+)([ \t]+|[^\n,.:\d])(\d+)', r'\1\3', content_8,
                   flags=re.M | re.I | re.X)  # Fix pricing numbers
content_10 = re.sub(r'([A-Za-z])(\s*\n|\s*,\s*\n)', r'\1-\n\n', content_9,
                    flags=re.M | re.I | re.X)  # Fix dangling punctuation
content_11 = re.sub(r'>(,|\s)', r'>. ', content_10, flags=re.M |
                    re.I | re.X)  # Cleanup context tags <>
content_12 = re.sub(r"(?<!be)(cuz|cause)", r"'cause", content_11,
                    flags=re.M | re.I | re.X)  # Replace cuz with 'cause
content_13 = re.sub(r'(:\s*\n[a-z])|(\n+[a-z])',
                    lambda x:  x.group(0).upper()
                    if x.group(0).islower()
                    else x.group(0).lower(),
                    content_12)  # Capitalize the first letter of the first word after a new line
content_14 = re.sub(r'(\.|\?)\s+\'?[a-z]',
                    lambda y: y.group(0).upper()
                    if y.group(0).islower()
                    else y.group(0).lower(),
                    content_13, flags=re.M | re.X)  # Capitalize the first letter of the first word after a period or question mark
content_15 = re.sub(
    r'([A-Za-z])\s{2,}(.)', r'\1 \2', content_14, flags=re.M | re.I | re.X)  # Remove duplicate spaces between words
content_16 = re.sub(
    r'-(\s*\n+.+\n.+\s*\n)(([A-Za-z]+.)\B\s*)', r' \3\1', content_15, flags=re.M | re.I | re.X)
content_17 = re.sub(r'([A-Z]+[a-z]*\'?[ \t]?[A-Za-z]*,?[ \t]?[A-Za-z]+[ \t]?[A-Z]*[a-z]*\'?[ \t]?)(\n|[^\n:-])\n+(\d\d:\d\d:\d\d\s*\n.+\n)([A-Za-z]+\'?[ \t]?([a-z]+.[ \t]?)?)',
                    r'\n\n\n\3\1\4', content_16, flags=re.M | re.X)  # Attach dangling statements to next speaker
content_17 = re.sub(r'Christina', r'Kristina', content_16,
                    flags=re.M | re.I | re.X)  # Correct name spelling
content_18 = re.sub(r'([A-Za-z])(,|\.)([A-Za-z])',
                    r'\1\2 \3', content_17, flags=re.M | re.I | re.X)  # Fix commas and periods with no space afterwards
content_19 = re.sub(r'&lt;(affirmative|laugh|inaudible)&gt;', r'<\1>', content_18,
                    flags=re.M | re.I | re.X)  # Fix <> tags if gibberish is in their place
content_20 = re.sub(r',?[ \t]you[ \t]know,',
                    r'', content_19, flags=re.M | re.I | re.X)  # Delete "you know" filler phrase
content_21 = re.sub(r'(([^\.A-Za-z])|([A-Za-z]))([ \t]<laugh>)', r'\3.\4',
                    content_20, flags=re.M | re.I | re.X)  # Correct <laugh> tag punctation
content_22 = re.sub(r'(.)\n{1,2}(\d\d:)', r'\1\n\n\n\2',
                    content_21, flags=re.M | re.I | re.X)  # Fix newline spacing
content_23 = re.sub(r'(:\d\d\n[A-Za-z]+:)([A-Za-z])',
                    r'\1\n\2', content_22, flags=re.M | re.I | re.X)  # Add newline after Speaker Label if dialogue is stuck on same line
content_24 = re.sub(r'([A-Z]+[a-z]*)(?!(Mark|West|Share|CI))(([A-Z]{2,})|([A-Z][a-z]))', r'\1. \2',
                    content_23, flags=re.M | re.X)  # Fix merged words
content_25 = re.sub(r'.(\d\d:\d\d:\d\d)', r'\n\n\n\1', content_24,
                    flags=re.M | re.I | re.X)  # Fix out-of-place timestamps
content_26 = re.sub(
    r'\d\d:\d\d:\d\d\n[A-Za-z]+:\n\s+', r'', content_25, flags=re.M | re.X)  # Eliminate speaker labels with no dialogue
content_27 = re.sub(r'(Mm-hmm\.\s?)(\s*\n+)(\d\d:\d\d:\d\d\n.+)\n(\s?<affirmative>\.\s?)',
                    r'\1\4\n\n\n\3\n', content_26, flags=re.M | re.I | re.X)  # Reattach <affirmative> tags to Mm-hmm text


with open(Output_File_Name, 'w') as f:
    f.write(content_27)
    print(content_27)

    nlp = spacy.load('en_core_web_sm')
    spacy_parser = nlp(content_27)
    for entity in spacy_parser.ents:
        if entity.label_ == 'PERSON':
            print(
                f'Found: {entity.text}, name of a {entity.label_}.')