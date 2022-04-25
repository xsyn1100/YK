#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    
                ]
            )
    buttons.append(
        [
            
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    
                ]
            )
        if OWNER:
            buttons.append(
                [
                    
                ]
            )
    buttons.append(
        
    )
    return buttons
