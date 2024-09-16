# Regex: find & replace

import spacy
import re


Input_File_Name = input("Enter input filepath: ")
Output_File_Name = re.sub(r'\.\w*', r'', Input_File_Name, flags=re.I |
                          re.M) + "-" + input("Enter output filename suffix: ") + ".txt"


Speaker0 = 'Kyle'
Speaker1 = 'Kyle'
Speaker2 = ''
Speaker3 = ''
Speaker4 = ''


with open(Input_File_Name, 'r') as f:
    content = f.read()


content = re.sub(r'(\w+:)[\t ]+\((\d\d:\d\d:\d\d)\)[\t ]+\W?[\t ]+', r'\n\n\2\n\1\n',
                      content, flags=re.M | re.I | re.X)  # Correct Reduct-formatted timestamps if applicable
content = re.sub(r'([A-Za-z])[\t ]*\n(\w)', r'\1 \2', content,
                     flags=re.M | re.I | re.X)  # Correct Reduct-formatted spacing if applicable
content = re.sub(r'\[*(\d\d:\d\d:\d\d)\][ \t]*([A-Za-z]+:)[ \t]*',
                    r'\n\n\1\n\2\n', content, flags=re.M | re.I | re.X)  # Correct Descript-formatted timestamps if applicable
content = re.sub(r'(\d\d:\d\d:\d\d)',
                    r'[\1]', content, flags=re.M | re.I | re.X)  # Add brackets to timestamps
content = re.sub(r'(Speaker\s+0\s+)(\[\d\d:\d\d:\d\d\])\s+',
                   r'\n\n\2\n{}:\n'.format(Speaker0), content, flags=re.M | re.I | re.X)
content = re.sub(r'(Speaker\s+1\s+)(\[\d\d:\d\d:\d\d\])\s+',
                   r'\n\n\2\n{}:\n'.format(Speaker1), content, flags=re.M | re.I | re.X)
content = re.sub(r'(Speaker\s+2\s+)(\[\d\d:\d\d:\d\d\])\s+',
                   r'\n\n\2\n{}:\n'.format(Speaker2), content, flags=re.M | re.I | re.X)
content = re.sub(r'(Speaker\s+[3-9]\s+)(\[\d\d:\d\d:\d\d\])\s+',
                   r'\n\n\2\n{}:\n'.format(Speaker4), content, flags=re.M | re.I | re.X)  # Replace speaker labels with speaker names, place the timecode above the speaker name
content = re.sub(r'(imposter|impostor)(\ssyndrome)', r'imposter\2', content, flags=re.M | re.I | re.X) # Fix spelling errors
content = re.sub(r'(([^A-Za-z])(Uh,*[^-]\s*))|(([^A-Za-z])(Um,*\s*))', r'\2\5',
                   content, flags=re.M | re.I | re.X)
content = re.sub(r'(Uhhuh|Uh huh)', r'Uh-huh', content, flags=re.M |
                   re.I | re.X)  # Remove filler words
content = re.sub(r'\b(([A-Za-z]+(\'?[A-Za-z]+)?)([ \t]+|,))([ \t]*\1|[ \t]*\2)(\1|\2)*\2*(\b)',
                   r'\2', content, flags=re.M | re.I | re.X)
content = re.sub(r'\b(([A-Za-z]+[ \t]?[A-Za-z]*)([ \t]+|,[ \t]+))([ \t]*\1|[ \t]*\2)(\1|\2)*\2*(\b)',
                   r'\2', content, flags=re.M | re.I | re.X)  # Remove duplicate words
content = re.sub(r'(?<!\n)(Mm-hmm\.\s<affirmative>(\.|,)*\s*|Mm-hmm(\.|,)*\s*)', r'\n\n\n\1\n\n\n',
                   content, flags=re.M | re.I | re.X)  # Attribute affirmative context tags to correct speakers
content = re.sub(r'(\d+)([ \t]+|[^\n,.:\d])(\d+)', r'\1\3', content,
                   flags=re.M | re.I | re.X)  # Fix pricing numbers
content = re.sub(r'([A-Za-z])(\s*\n|\s*,\s*\n)', r'\1-\n\n', content,
                    flags=re.M | re.I | re.X)  # Fix dangling punctuation
content = re.sub(r'>(,|\s)', r'>. ', content, flags=re.M |
                    re.I | re.X)  # Cleanup context tags <>
content = re.sub(r"(?<!be)(cuz|cause)", r"'cause", content,
                    flags=re.M | re.I | re.X)  # Replace cuz with 'cause
content = re.sub(r'(:\s*\n[a-z])|(\n+[a-z])',
                    lambda x:  x.group(0).upper()
                    if x.group(0).islower()
                    else x.group(0).lower(),
                    content)  # Capitalize the first letter of the first word after a new line
content = re.sub(r'(\.|\?)\s+\'?[a-z]',
                    lambda y: y.group(0).upper()
                    if y.group(0).islower()
                    else y.group(0).lower(),
                    content, flags=re.M | re.X)  # Capitalize the first letter of the first word after a period or question mark
content = re.sub(
    r'([A-Za-z])\s{2,}(.)', r'\1 \2', content, flags=re.M | re.I | re.X)  # Remove duplicate spaces between words
content = re.sub(
    r'-(\s*\n+.+\n.+\s*\n)(([A-Za-z]+.)\B\s*)', r' \3\1', content, flags=re.M | re.I | re.X)
content = re.sub(r'([A-Z]+[a-z]*\'?[ \t]?[A-Za-z]*,?[ \t]?[A-Za-z]+[ \t]?[A-Z]*[a-z]*\'?[ \t]?)(\n|[^\n:-])\n+(\[\d\d:\d\d:\d\d\]\s*\n.+\n)([A-Za-z]+\'?[ \t]?([a-z]+.[ \t]?)?)',
                    r'\n\n\n\3\1\4', content, flags=re.M | re.X)  # Attach dangling statements to next speaker
content = re.sub(r'([A-Za-z])(,|\.)([A-Za-z])',
                    r'\1\2 \3', content, flags=re.M | re.I | re.X)  # Fix commas and periods with no space afterwards
content = re.sub(r'&lt;(affirmative|laugh|inaudible)&gt;', r'<\1>', content,
                    flags=re.M | re.I | re.X)  # Fix <> tags if gibberish is in their place
content = re.sub(r',?[ \t]you[ \t]know,',
                    r'', content, flags=re.M | re.I | re.X)  # Delete "you know" filler phrase
content = re.sub(r'(([^\.A-Za-z])|([A-Za-z]))([ \t]<laugh>)', r'\3.\4',
                    content, flags=re.M | re.I | re.X)  # Correct <laugh> tag punctation
content = re.sub(r'(.)\n{1,2}(\[\d\d:)', r'\1\n\n\n\2',
                    content, flags=re.M | re.I | re.X)  # Fix newline spacing
content = re.sub(r'(:\d\d\]\n[A-Za-z]+:)([A-Za-z])',
                    r'\1\n\2', content, flags=re.M | re.I | re.X)  # Add newline after Speaker Label if dialogue is stuck on same line
# content = re.sub(r'([A-Z]+[a-z]*)(?!(Mark|West|Share|CI))(([A-Z]{2,})|([A-Z][a-z]))', r'\1. \2',
#                     content, flags=re.M | re.X)  # Fix merged words
content = re.sub(r'.(\[\d\d:\d\d:\d\d\])', r'\n\n\n\1', content,
                    flags=re.M | re.I | re.X)  # Fix out-of-place timestamps
content = re.sub(
    r'\[\d\d:\d\d:\d\d\]\n[A-Za-z]+:\n\s+', r'', content, flags=re.M | re.X)  # Eliminate speaker labels with no dialogue
content = re.sub(r'(Mm-hmm\.\s?)(\s*\n+)(\[\d\d:\d\d:\d\d\]\n.+)\n(\s?<affirmative>\.\s?)',
                    r'\1\4\n\n\n\3\n', content, flags=re.M | re.I | re.X)  # Reattach <affirmative> tags to Mm-hmm text
content = re.sub(r'Java\.\s+ript', r'JavaScript', content,
                    flags=re.M | re.I | re.X)  # Correct language name spelling
content = re.sub(r'(C\.\s)', r'CSS', content,
                    flags=re.M | re.X)  # Correct language name spelling
content = re.sub(r'(HT\.\s)', r'HTML', content,
                    flags=re.M | re.X)  # Correct language name spelling


with open(Output_File_Name, 'w') as f:
    f.write(content)
    print(content)

    # nlp = spacy.load('en_core_web_sm')
    # spacy_parser = nlp(content)
    # for entity in spacy_parser.ents:
    #     if entity.label_ == 'PERSON':
    #         print(
    #             f'Found: {entity.text}, name of a {entity.label_}.')