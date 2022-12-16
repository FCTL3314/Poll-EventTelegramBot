import aiogram
import utils


async def start_command(message: aiogram.types.Message):
    await message.answer(text='ℹ️<b>Как пользоваться ботом ?</b>\n'
                              '● Первым делом, вам нужно добавить бота в любые ваши группы/каналы, после чего, '
                              'бот отправит вам сообщение о том, что он успешно добавлен.\n'
                              '● После добавления бота, вы можете создавать мероприятия с помощью команды '
                              '/create_event.\n'
                              '● Для просмотра статистики по мероприятиям, используется команда /statistics.\n'
                              '● Что бы удалить все мероприятия используйте команду /clear.\n'
                              '● Если вы передумали создавать мероприятие воспользуйтесь командой /cancel для отмены.',
                         parse_mode='HTML')
    await message.answer(text='❕ <b>Обратите внимание, что у телеграмма есть лимит на кол-во символов в сообщениях с '
                              'изображениями. Лимит равен 1024-м символам. Это ограничение касается не только бота, '
                              'но и всех пользователей телеграмма.\n При превышении лимита, бот проинформирует вас о '
                              'вашем превышении, и остановит создание события для '
                              'предотвращения появления ошибок.</b>', parse_mode='HTML')


def register_start_command_handler(dp: aiogram.Dispatcher):
    dp.register_message_handler(callback=start_command, commands=['start'])
