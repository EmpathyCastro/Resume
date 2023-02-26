
BLOCK_C1 = """import page
hide_blocks = ["C2", "B", "C3", "Prompt"]
for block in hide_blocks:
    page.get_block(block).hide()
name_block = page.get_block("Name")
name_block.set_text("#### Hello, please enter your name below.")
name = input("What is your name?\\n")
name_block.set_text(name.strip())
name_block.hide()"""


def get_dynamicode_demo_data():
    return {
        "title": "DynamiCode Demo",
        "author": "Empathy",
        "author_uuid": "",
        "date_created": "2023-02-25",
        "date_edited": "2023-02-25",
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
                "name": "C2",
                "text": "What is your favorite color?",
                "choices": ["Red", "Blue", "Green"]
            },
            {
                "type": "SliderBlock",
                "name": "B",
                "text": "What is your favorite number?",
                "lower": 0,
                "upper": 10,
                "default": 5
            },
            {
                "type": "CodeBlock",
                "name": "C3",
                "code": "print('Hello World!')"
            }
        ]
    }
