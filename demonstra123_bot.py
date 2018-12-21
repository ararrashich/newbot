import telepot, time, subprocess

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        command = msg['text']
        print ('Got command: %s' % command)

        if  '/Cable_diag' in command:#В кавычках команда которую мы будем писать в телеграмм. 
                            #Можно и слова и по русски но начинать нужно именно с косой палочки
            p = subprocess.Popen(cmd0, shell=True)#А тут собственно выполняется команда которую
                            #мы задали для переменной "cmd0"
            bot.sendMessage(chat_id, "Комп не уйдёт в спящий режим")#А это ответ бота в чат.



bot = telepot.Bot('727077862:AAFgOLfmrN5bKr58VHYdyBVx_lGqnsBCgkk')#Вместо иксов пишем ваш токен
cmd0 = 'Powercfg -setactive 6a935962-1964-4f2a-a937-95cd9b8ca616'
cmd1 = 'Powercfg -setactive 021d63d0-34a0-4824-8f5a-b83156cba872'
shut = 'shutdown -s'
soundpc = 'C:\SSD_v3.exe\SSD.exe 7777hidden'
soundtv = 'C:\SSD_v3.exe\SSD.exe 7771hidden'

bot.message_loop(handle)

while 1:
    time.sleep(20)
