import os
import re


# Calculate the length of the text string
def str_len(string):
    text_string = re.sub(r'\n', ' ', string)
    print(len(text_string))


# Paste your string into the function, then run the script
str_len("""AI Money-Making Ideas

Max’s Introduction
- AI is creating essays, coding, solving math problems, even writing apology letters 
- People will pay for convenience, even if the task can be done for free 
- AI businesses must provide value and convenience 

The Opportunity Paradox
- AI will take our jobs, but also open up doors for new businesses 
- People will pay to solve problems, even if they can solve them themselves 
- Value through convenience is key to making money with AI 

Improving AI Businesses
- User experience is the key to distinguishing AI businesses 
- Brainstorming ideas is the best way to get started 
- Improve AI businesses by offering increased convenience and a great platform 

AI Business Ideas
- Prompt Based.com: Sell AI prompts to others 
- Business Name Generator: Provide a convenient service to generate business names 
- Fitness Coach: Use AI to create a fitness coach service 
- Web Design Concepts: Create a convenient service to design web concepts 

Most Convincing Opinions
Max believes that value through convenience is the key to making money with AI. He suggests brainstorming ideas and improving AI businesses by offering increased convenience and a great platform. He also believes that user experience is the key to distinguishing AI businesses.""")
