from telegram.ext import Updater, CommandHandler
import picamera
import datetime
import os

# Bot Token
TOKEN = "466130108:AAGXwqE9qEYXdW4WdojNKVTi5Xp7JFFDURU"
# Test Kommandos
KOMMANDOS = ["/SENDPICTURE"]

def start(bot, update):
    update.message.reply_text('Herzlich Willkommen!')



#
# Command Optionen
#
def sendPicture(bot, update):
    tempPicture = make_temp_image()
    update.message.reply_photo(photo=open(tempPicture, 'rb'))
    delete_file(tempPicture)

#
# PiCam Operations
#
def make_temp_image():
    currentTime = datetime.datetime.now()
    with picamera.PiCamera() as camera:
        # camera.start_preview()
        # Camera warm-up time
        # time.sleep(2)
        photoPath = 'data/{}.jpg'.format(str(currentTime))
        camera.capture(photoPath)
        return photoPath

def delete_file(path):
    os.remove(path)

#
# Initialisiere Bot und adde Commandhandler
#

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('sendPicture', sendPicture))


#
# Start
#

updater.start_polling()
updater.idle()


# JSON Zugriff auf Force Reply Nachricht
# update.message.reply_to_message