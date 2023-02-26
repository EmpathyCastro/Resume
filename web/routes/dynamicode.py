import json

BLOCK_C1 = """import page
hide_blocks = ['C2', 'C3', 'C4', 'C5', 'C6', 'Game Slider', 'Game Answer', 'Game Guesses', 'Color Choice',
               'Color', 'Prompt']
for block in hide_blocks:
    page.get_block(block).hide()
name_block = page.get_block('Name')
name_block.set_text('#### Hello, please enter your name below.')
name = input('What is your name?\\n').strip()
name_block.set_text(name)
name_block.hide()

page.get_block('Prompt').set_text(f'#### Hi {name}! This is a simple demo of DynamiCode. This specific demo'
                                  ' takes the form of a short survey. Hopefully it can convey the capabilities'   
                                  ' of DynamiCode!\\n\\nTo continue to each new section, simply run the code block'
                                  ' at the end of each section.')
page.get_block('Prompt').show()
page.get_block('C2').show()
page.get_block('C1').hide()
"""

BLOCK_C2 = """# RUN ME TO CONTINUE!
import page
page.get_block('Prompt').hide()
color_block = page.get_block('Color Choice')
color_block.set_text('#### Choose your favorite color from the list below.\\n\\nRemember to run the \
code block at the end!')
color_block.show()
page.get_block('C2').hide()
page.get_block('C3').show()
"""

BLOCK_C3 = """# RUN ME TO CONTINUE!
import page
import random
color_block = page.get_block('Color Choice')
color = color_block.get_selected_choice()
color_block.hide()
prompt_block = page.get_block('Prompt')
if color == 'Other':
    prompt_block.set_text('#### So your favorite color wasn\\'t on the list, huh? Alright then, what is it?')
    prompt_block.show()
    color = input('What is your favorite color?\\n').strip()
page.get_block('Color').set_text(color)
prompt_block.set_text(f'#### Your favorite color is {color}? Interesting.')
page.get_block('Game Answer').set_text(str(random.randint(0, 10)))
prompt_block.show()
page.get_block('Game Slider').show()
page.get_block('C3').hide()
page.get_block('C4').show()
"""

BLOCK_C4 = """# RUN ME TO CONTINUE!
import page
true_number = int(page.get_block('Game Answer').get_text())
guess = int(page.get_block('Game Slider').get_value())
page.get_block('Prompt').hide()
if guess == true_number:
    page.get_block('Prompt').set_text(f'#### That\\'s right! The number was {true_number}.\\n\\nNow run the code block'
                                      ' to see your results.')
    page.get_block('Prompt').show()
    page.get_block('Game Slider').hide()
    page.get_block('C4').hide()
    page.get_block('C5').show()
else:
    page.get_block('Game Slider').set_text(f'#### The number is not {guess}. Try again.')
    guesses = int(page.get_block('Game Guesses').get_text()) + 1
    page.get_block('Game Guesses').set_text(str(guesses))
"""

BLOCK_C5 = """# RUN ME TO SEE RESULTS!
import page
name = page.get_block('Name').get_text()
color = page.get_block('Color').get_text()
guesses = page.get_block('Game Guesses').get_text()
page.get_block('Prompt').set_text(f'#### Thank you for taking the survey! From what I remember, your name is {name},'
                                  f' your favorite color is {color}, and it took you {guesses} guesses to guess the'  
                                  ' number.\\n\\nThanks for running this demo! Run the next code block to see all'
                                  ' the code used to create this page.')
page.get_block('Prompt').show()
page.get_block('C5').hide()
page.get_block('C6').show()
"""

BLOCK_C6 = """# RUN ME TO SEE THE CODE!
import page
all_blocks = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'Name', 'Prompt', 'Color Choice', 'Color',
              'Game Slider', 'Game Answer', 'Game Guesses']
for block in all_blocks:
    page.get_block(block).show()
"""


def get_dynamicode_demo_data():
    data = {
        "title": "DynamiCode Demo",
        "author": "Empathy",
        "date_created": "2022-06-25",
        "codepage_type": "post",
        "blocks": [
            {
                "type": "TextBlock",
                "name": "Name",
                "text": "### Hi! Get started by running the code block below."
            },
            {
                "type": "CodeBlock",
                "name": "C1",
                "code": BLOCK_C1
            },
            {
                "type": "TextBlock",
                "name": "Prompt",
                "text": ""
            },
            {
                "type": "ChoiceBlock",
                "name": "Color Choice",
                "text": "What is your favorite color?",
                "choices": ["Red", "Yellow", "Blue", "Other"]
            },
            {
                "type": "SliderBlock",
                "name": "Game Slider",
                "text": "#### Now, let's play a game. I'm thinking of a number between 0 and 10. "
                        "Can you guess what it is?",
                "lower": 0,
                "upper": 10,
                "default": 5
            },
            {
                "type": "CodeBlock",
                "name": "C2",
                "code": BLOCK_C2
            },
            {
                "type": "TextBlock",
                "name": "Color",
                "text": ""
            },
            {
                "type": "TextBlock",
                "name": "Game Answer",
                "text": ""
            },
            {
                "type": "TextBlock",
                "name": "Game Guesses",
                "text": "1"
            },
            {
                "type": "CodeBlock",
                "name": "C3",
                "code": BLOCK_C3
            },
            {
                "type": "CodeBlock",
                "name": "C4",
                "code": BLOCK_C4
            },
            {
                "type": "CodeBlock",
                "name": "C5",
                "code": BLOCK_C5
            },
            {
                "type": "CodeBlock",
                "name": "C6",
                "code": BLOCK_C6
            }
        ]
    }
    return json.dumps(data, indent=4)
