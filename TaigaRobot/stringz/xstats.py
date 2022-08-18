import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from TaigaRobot import (StartTime, DEV_USERS, L_STATS, pbot)
import TaigaRobot.utils.formatter as formatter
import TaigaRobot.modules.sql.users_sql as sql




# Stats Module

async def bot_sys_stats():
    bot_uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    users = sql.num_users()
    chats = sql.num_chats()
    stats = f"""
 Tomozaki@TaigaGremory
---------------------
• Uptime: {formatter.get_readable_time((bot_uptime))}
• Bot: {round(process.memory_info()[0] / 1024 ** 2)} MB
• Cpu: {cpu}%
• Ram: {mem}%
• Disk: {disk}%
• Chats: {chats}
• Users: {users}
---------------------
Do not use this bot
"""
    return stats

# logs Module

async def xlogs_stats():
    loges = f"""{L_CHAT}
"""
    return loges

