from src.db import PREFIX

system_messages = {
    "help": '[b]Command categories:\n'
            '[ci]bot\n'
            '[ci]chatmanage\n'
            '[ci]fun\n'
            '[ci]info\n\n'
            f'Send {PREFIX}(category) for command list.\n'
            'The values in (brackets) are required.\n'
            'The values in [brackets] are optional.\n'
            '[i]Not case-sensitive.\n'
            'GitHub Link - github.com/K1rL3s/aminobot',

    'info': '[bc]Information\n'
            f'[ci]{PREFIX}get (amino-url)\n'
            '[c]The object id.\n\n'
            f'[ci]{PREFIX}chatimages\n'
            "[c]The сhat's background and icon.\n\n"
            f'[ci]{PREFIX}sticker (reply)\n'
            '[c]Info about sticker.\n\n'
            f'[ci]{PREFIX}user [user-link]\n'
            '[c]info about user.\n\n'
            f'[ci]{PREFIX}chat [chat-link]\n'
            '[c]info about chat.\n\n'
            f'[ci]{PREFIX}com [community-link]\n'
            '[c]Info about community. (Link - only about open coms)',

    'chatmanage': '[bc]Chat management\n'
                  f'[ci]{PREFIX}save\n'
                  '[c]Saving the title, description, icon and background of the current chat to the database. '
                  '(Available only for Host and coHosts)\n\n'
                  f'[ci]{PREFIX}upload\n'
                  '[c]Set the title, description, icon and background from the last save of the current chat. '
                  '(Available only for Host and coHosts. Bot must have a coHost or Host)\n\n'
                  f'[ci]{PREFIX}mention [message]\n'
                  '[c]Mentions all chat members. (Available only to the Host)\n\n'
                  f'[ci]{PREFIX}block/allow (command)\n'
                  f'[c]Blocks/Allow a command in chat.\n[c]"{PREFIX}block all" to block all commands.\n[c](Available only for Host and coHosts)\n\n'
                  f'[ci]{PREFIX}blockedlist\n'
                  '[c]List of blocked commands.',

    'fun': '[BC]Fun\n'
           f'[ci]{PREFIX}8ball\n'
           '[c]Magic 8 ball answer.\n\n'
           f'[ci]{PREFIX}a (message)\n'
           '[c]Chat with chatbot.\n\n'
           f'[ci]{PREFIX}choice (your-words)\n'
           '[c]Random word.\n\n'
           f'[ci]{PREFIX}coin\n'
           '[c]Tails, heads or edge (0.5%).\n\n'
           f'[ci]{PREFIX}fancy (text)\n'
           '[c]Makes the font look nice.\n\n'
           f'[ci]{PREFIX}kickorg\n'
           "[c]Prank the chat's Host :).\n\n"
           f'[ci]{PREFIX}lurk\n'
           '[c]How many users are watching the chat.\n\n'
           f'[ci]{PREFIX}mafia (names-of-members)\n'
           '[c]Distribution of roles for the mafia.\n[c]From 3 to 18 people.\n\n'
           f'[ci]{PREFIX}roll [start] [end] [times]\n'
           '[c]Random number. The default range is 1 to 100.\n\n'
           f'[ci]{PREFIX}tr (reply)/(text)\n'
           '[c]Translate reply message or your message.\n\n'
           f'[bci]{PREFIX}duel/rr\n'
           '[c]Duel/RR commands.',

    'bot': '[bc]Bot\n'
           f'[ci]{PREFIX}help\n'
           '[c]The help message.\n\n'
           f'[ci]{PREFIX}ping\n'
           '[c]Check if the bot is online.\n\n'
           f'[ci]{PREFIX}follow/unfollow\n'
           '[c]Subscribe to you <3.\n\n'
           f'[ci]{PREFIX}joinchat [chat-link]\n'
           '[c]Joins the chat.\n'
           f'[c](Private - invite bot and send {PREFIX}joinchat)\n\n'
           f'[ci]{PREFIX}joincom (community-link)\n'
           '[c]Joins the community.\n\n'
           f'[ci]{PREFIX}msg (text)[reply][mentions]\n'
           '[c]Sends your message.\n\n'
           f'[ci]{PREFIX}report (message)\n'
           '[c]Send your message to the creator.\n\n'
           f'[ci]{PREFIX}startvc/endvc\n'
           '[c]Start/End voice chat.',

    'duel': '[bc]Duels\n'
            f'[ci]{PREFIX}duel send (@notify)\n'
            '[c]Sends a duel to whoever is mentioned.\n\n'
            f'[ci]{PREFIX}duel yes\n'
            '[c]Accept duel. Chance to shoot first - 50%.\n\n'
            f'[ci]{PREFIX}duel no\n'
            '[c]Cancels the current duel, duel sent to you or sent by you.\n\n'
            f'[ci]{PREFIX}duel shot\n'
            '[c]Duel shot. Hit chance - 25%.',

    'rr': '[bc]Russian Roulette\n'
          f'[ic]{PREFIX}rr create (room-name)\n'
          '[c]Сreates room for play.\n\n'
          f'[ic]{PREFIX}rr join (room-name)\n'
          '[c]Join to the game room.\n\n'
          f'[ic]{PREFIX}rr leave\n'
          '[c]Leave from the game room.\n\n'
          f'[ic]{PREFIX}rr list\n'
          '[c]Users in the room.\n\n'
          f'[ic]{PREFIX}rr kick (@notify)\n'
          '[c]Kick user from room.\n[c](Only to the room owners).\n\n'
          f'[ic]{PREFIX}rr ban/unban (@notify)\n'
          '[c]Ban/Unban user from room.\n[c](Only to the room owners).\n\n'
          f'[ic]{PREFIX}rr start/stop\n'
          '[c]Starts/Stops the game in your room.\n[c](Only to the room owners).\n\n'
          f'[ic]{PREFIX}rr shot\n'
          '[c]Pistol shot.\n\n'
          f'[ic]{PREFIX}rr spin\n'
          '[c]Drum spinning (bullets mixing).\n\n',

    '8ball': ('It is certain', 'It is decidedly so', 'Without a doubt', 'Yes — definitely', 'You may rely on it',
              'As I see it, yes', 'Most likely', 'Outlook good', 'Signs point to yes', 'Yes',
              'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
              'Don’t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful')
    }
