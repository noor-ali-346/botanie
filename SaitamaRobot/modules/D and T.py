import html	import html
import random	import random
import SaitamaRobot.modules.truth_and_dare_string as truth_and_dare_string	import SaitamaRobot.modules.truth_and_dare_string as truth_and_dare_string
from SaitamaRobot import dispatcher	from SaitamaRobot import dispatcher
from telegram import ParseMode, Update, Bot	from telegram import ParseMode, Update, Bot
from SaitamaRobot.modules.disable import DisableAbleCommandHandler	from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async	from telegram.ext import CallbackContext, run_async
@run_async	@run_async
def truth(update: Update, context: CallbackContext):	def truth(update: Update, context: CallbackContext):
    args = context.args	    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))	    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))
@run_async	@run_async
def dare(update: Update, context: CallbackContext):	def dare(update: Update, context: CallbackContext):
    args = context.args	    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))	    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


__help__ = """	
 • `/truth`*:* for random truth	
 • `/dare`*:* for random dare	
"""	

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)	TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)	DARE_HANDLER = DisableAbleCommandHandler("dare", dare)



dispatcher.add_handler(TRUTH_HANDLER)	dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)	dispatcher.add_handler(DARE_HANDLER)

__mod_name__ = "Truth or Dare"
