# Markdown Regex Formatter
## Format website Markdown files for use in copywriting projects
### Use Case: You want to model the structure or style of a mentor's sales page copywriting in your own sales page


import re

# /// Fix Markdown Syntax Errors ///

# Remove extra spaces after bullet points and numbered lists 
# Find: ((-)|(\d\.))\s\s(\s)?
# Replace: $1 

# Fix bold stars that jump to next line
# Find: (\*+.+:).+\n(\*+)
# Replace: $1$2  \n

# Fix extra star at end of bold text
# Find: ([^\*]\*\*[^\*].+)(\*\*\*).+(\n)
# Replace: $1**  $3