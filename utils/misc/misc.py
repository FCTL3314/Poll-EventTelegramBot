import utils

from typing import List


async def create_channels_text(channels: List[tuple], groups: List[tuple]):
    result = ''
    if channels:
        for i, channel in enumerate(channels, 1):
            result += f'{i}. {channel[1]}\n'
    if groups:
        for i, group in enumerate(groups, len(channels) + 1):
            result += f'{i}. {group[1]}\n'
    return result


async def get_channels_indexes(channels: List[tuple], groups: List[tuple]):
    channels_indexes = dict()
    if channels:
        for i, channel in enumerate(channels, 1):
            channels_indexes[str(i)] = channel[0]
    if groups:
        for i, group in enumerate(groups, len(channels) + 1):
            channels_indexes[str(i)] = group[0]
    return channels_indexes


async def create_users_vote_text(users, emoji):
    result = f'<b>Пользователи которые нажали</b> {emoji}:\n'
    for i, data in enumerate(users, 1):
        result += f'{i}. <a href="tg://user?id={data[0]}">{data[1]} {data[2]}</a>\n'
    return result


async def insert_event_into_db(chat_id, message_id, event_name, vote_limit, link_button_url, link_button_name):
    if link_button_name:
        with utils.database.database as db:
            db.execute(f"INSERT INTO event_data VALUES ({chat_id}, {message_id}, "
                       f"'{event_name}', 0, 0, {vote_limit}, '{link_button_url}', '{link_button_name}',"
                       f"current_date)")
    else:
        with utils.database.database as db:
            db.execute(f"INSERT INTO event_data VALUES ({chat_id}, {message_id}, "
                       f"'{event_name}', 0, 0, {vote_limit}, null, null, current_date)")
