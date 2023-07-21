import openai

openai.api_key = "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"
model_engine = "gpt-3.5-turbo"

response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful  assistant."},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
        {"role": "user", "content": "I'm new in using ChatGPT. I heard that it's very useful."},
        {"role": "assistant", "content": "Yes, ChatGPT is a very useful platform that provides a range of services from automated assistance to personalized and timely support. You can ask questions and get quick answers, have engaging conversations, get homework help, and much more. Whether you want a friendly chat or need help with something specific, ChatGPT is here to assist you. Do you have any questions or would you like me to assist you with anything?"},
        {"role": "user", "content": "What is the first sentence I've sent you? And what is the first sentence you've sent me?"}
    ]
)

message = response.choices[0]['message']
print("{}:{}".format(message['role'], message['content']))
