from config import TOKEN
from discord.ext import commands
from tinydb import TinyDB, Query
from random import randint

bot = commands.Bot(command_prefix='ql')
db = TinyDB('../db/quotes.json')

@bot.event
async def on_ready():
    print('Logged as {0}'.format(bot.user))

@bot.command()
async def quote(ctx, user = None, msg = None):
    nb_quote = db.count(Query().id.exists())
    if user == None or msg == None:
        quote_id = randint(0, nb_quote-1)
        print('qid{0}'.format(quote_id))
        quote = db.get(Query().id == quote_id)
        await ctx.send('{0} a déjà dit : {1}'.format(quote['user'], quote['msg']))
        return

    db.insert({'id': nb_quote, 'user': user, 'msg': msg})
    print('{0}: {1}'.format(user, msg))
    await ctx.send('La citation a été ajouté au lexique.')

bot.run(TOKEN)