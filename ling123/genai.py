from ast import literal_eval
from openai import OpenAI
from IPython import get_ipython

# Sends `prompt` to GPT, and returns the response as a python object, type `t`,
# (if it is one) or a string (otherwise)
def ask_gpt(prompt, t=None, apikey=None):
    if not apikey:
        apikey = get_ipython().user_ns['openai_api_key']

    client = OpenAI(api_key=apikey)
    if t is not None:
        # Add extra instructions on how to return the answer as a particular
        # Python type
        prompt += f"""
    Return your answer in the form of a python {t.__name__} literal.
    Do not wrap your answer in Markdown at all.
    Just return the python {t.__name__} literal only.
    Remember to properly escape characters as needed, like using `\\n`
    for newlines, rather than the newline character inside of strings.\
    """

    model = 'gpt-4o-mini' # Cheapest, but still good model
    message = {
        'role':'user',    # `user` role is like typing in a Q to ChatGPT
        'content':prompt  # `content` is what you would type in to ChatGPT
        }

    # This actually sends the prompt to OpenAI and gets info back
    completion = client.chat.completions.create(
        model = model,
        messages = [message],
    )

    # Store just the answer string itself
    response = completion.choices[0].message.content

    try:
        # Try to convert it to a python literal
        return literal_eval(response)
    except:
        # If anything goes wrong, just return the answer string.
        return response