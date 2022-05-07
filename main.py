
import discord
import os
import requests
import json
import random
from discord.ext import tasks

client = discord.Client()


econ = ["econ", "economic", "microeconomics", "macroeconomics"]
econresources = ["https://quizlet.com/291450155/economics-diagram/","https://quizlet.com/ca/692575286/microeconomics-flash-cards/","https://quizlet.com/284463213/macroeconomics-flash-cards/"]

algebra = ["algebra"]
algebraresources = ["https://quizlet.com/324016014/algebra-flash-cards/","https://quizlet.com/534430571/algebra-equations-flash-cards/","https://quizlet.com/explanations/textbook-solutions/algebra-2-a-common-core-curriculum-1st-edition-9781608408405"]

statistic = ["statistics"]
statisticsresources = ["https://quizlet.com/explanations/textbook-solutions/elementary-statistics-13th-edition-9780134462455", "https://quizlet.com/145686306/statistics-flash-cards/", "https://quizlet.com/147341548/statistics-flash-cards/"]

trigonometry = ["trigonometry"]
trigonometryresources = ["https://quizlet.com/227795513/trigonometry-flash-cards/","https://quizlet.com/299876791/trigonometry-trigonometry-flash-cards/","https://quizlet.com/explanations/textbook-solutions/trigonometry-11th-edition-9780134217437"]

english = ["english", "poetry", "drama"]
englishresources =["https://quizlet.com/explanations/textbook-solutions/springboard-english-language-arts-senior-english-9781457302244", "https://quizlet.com/356545128/composition-and-rhetoric-flash-cards/", "https://quizlet.com/396668765/literature-and-composition-flash-cards/"]

study_words = [ "exam","test", "final", "study"]
study_encouragements = ["I hope you pass", "You are going to do great", "Remember, it's okay to not always get an A.", "You are a star!"]

playlist = ["https://bit.ly/3FqI6Qv","https://bit.ly/3w91Vax","https://bit.ly/3sixFZI","https://bit.ly/3vR8X4Q","https://bit.ly/3ypIrBh"]


#Water and break reminder
@tasks.loop(minutes=35.0)
async def test():
    channel = client.get_channel(972274902151352343)
    await channel.send("Please remember to drink water, Take a break if need be!")



#Bot log in 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    test.start()

#Welcome, encouraging words and playlist
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

  
    if msg.startswith('motivation'):
        quote = get_quote()
        await message.channel.send(quote)

    if any (word in msg for word in study_words):
      await message.channel.send(random.choice(study_encouragements))

    if msg.startswith('hi'):
      await message.channel.send("Hey there! How are you?")

    if msg.startswith('playlist'):
       await message.channel.send(random.choice(playlist))
      
    if any (word in msg for word in econ):
      await message.channel.send("Here's a cool study guide for you: "+ random.choice(econresources))

    if any (word in msg for word in algebra):
      await message.channel.send("Here's a cool study guide for you: "+ random.choice(algebraresources))

    if any (word in msg for word in trigonometry):
     await message.channel.send("Here's a cool study guide for you: "+ random.choice(trigonometryresources))
      
    if any (word in msg for word in english):
      await message.channel.send("Here's a cool study guide for you: "+ random.choice(englishresources))  

      
# Motivational quotes
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


client.run(os.getenv('token'))
