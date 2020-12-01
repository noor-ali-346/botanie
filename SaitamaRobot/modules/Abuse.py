import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async



@run_async   
def abuse(update, context):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.ABUSE_STRINGS))


help = """
 A little piece of fun wording! Give a loud shout out in the chatroom.
 
 • /abuse bad people
    

ABUSE_HANDLER = DisableAbleCommandHandler(["abuse", "gaali"], abuse, admin_ok=True)

dispatcher.add_handler(ABUSE_HANDLER)

mod_name = "abuse"
command_list = ["abuse"]
handlers = [ABAUSE_HANDLER]
