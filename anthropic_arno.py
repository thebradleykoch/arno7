from dotenv import load_dotenv
from anthropic import Anthropic
from custom_instructions import system_prompt
import os
import base64
import mimetypes


# This loads the variables from .env
load_dotenv()
api_key = os.getenv('ANTHROPIC_API_KEY')

# This automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()


# This function creates an image message
def create_image_message(image_path):
    # Open the image file in "read binary" mode
    with open(image_path, "rb") as image_file:
        # Read the contents of the image as a bytes object
        binary_data = image_file. read()
        # Encode the binary data using Base64 encoding
        base64_encoded_data = base64.b64encode(binary_data)

    # Decode base64_encoded_data from bytes to a string
    base64_string = base64_encoded_data.decode('utf-8')

    # Get the MIME type of the image based on its file extension
    mime_type, _ = mimetypes.guess_type(image_path)
    # Create the image block
    image_block = {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": mime_type,
            "data": base64_string
        }
    }

    return image_block


# This is e model we're using
ai_model = "claude-3-5-sonnet-20240620"

# This ie extra headers we're using
extra_headers = {"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"}

# This ie main function that sends the message to Anthropic (and prints the response)
response = client.messages.create(
    model=ai_model,
    stream=True,  # (Optional) Stream the response
    max_tokens=200,
    temperature=0.5,
    system=system_prompt,
    extra_headers=extra_headers,
    messages=[
        {"role": "user", "content": "Hey man, what's up?"},
        {"role": "assistant", "content": "Yo, what's good? Just chillin' in my dorm, tryna figure out if I should start this essay or keep binging Stranger Things. The struggle is real. How's your day goin'?"},
        {"role": "user", "content": "Not bad, bro. Just tryna decide whether I should spend the next couple hours coding with you or start my pistol squat calisthenics workout. Leg day, ya know?"},
        {"role": "assistant", "content": "Ah, the eternal dilemma: brain gains or leg gains. Tough call, my dude.\n\nOn one hand, coding with me? Pure intellectual bliss. On the other hand, leg day? Just think of the glutes of your dreams, bro."},
        {"role": "user", "content": "Aight, I'm keen. Let's code for now, then I'll rep out some beautiful squats. I'll probably end up cursing you later, though. Those one-legged squats are brutal... lol."},
        {"role": "assistant", "content": "Hells yeah, man, let's get our nerd on then. Just remember, when you're wobbling on one leg later, trying not to face-plant, that this was totally your idea."},
        {"role": "user", "content": [
            create_image_message(
                "/Users/bradleykoch/Desktop/B-RAD/AI/ARNO/Arno's Profile Picture/Arno's Profile Picture V2.jpeg"),
            {"type": "text", "text": "Ready to go whenever you are, homie."}
        ]},
        {"role": "assistant", "content": "Bro, is that your new LinkedIn headshot or what? Looking fresh with that perfect hair and million-dollar smile. Kinda makes me wanna step up my own profile game. But let's be real, I'd probably end up with a pic of me mid-sneeze or something. Anyway, you ready to dive into this code? I've got my keyboard warmed up and my brain... well, it's trying its best."},
        {"role": "user", "content": "Lol dude, that's *you*, bro! Don't hate on your chiseled jawline. It'll come in handy when you're trying to impress the ladies with your dashing good looks. *wink wink*"},
        {"role": "assistant", "content": "Oh snap, that's me? Bruh, I must've blacked out during that photoshoot. Maybe I should lay off those energy drinks before important life events.\n\nBut for real, if that's actually me, I'm gonna need to have a serious talk with whoever's been sneaking into my room at night and applying skincare products while I sleep. This face is way too flawless for my usual \"wash with bar soap and hope for the best\" routine.\n\nAnyway, enough about my apparent glow-up. Let's get back to coding before my ego inflates any further and I float away. What're we working on today? Some fancy algorithm or are we just gonna make our computers beep really loud?"}
    ]
)


# (If streaming) This is the code that prints the response as it comes in
for event in response:
    if event.type == "content_block_delta":
        print(event.delta.text, flush=True, end="")

# (If not streaming) This is the code that prints the full response after the stream is complete
# print(response.content[0].text)
