﻿import settings

start = {
    'mes': 'start',
    'text': '''Привет!''',
    'markup': [
        ['👁‍🗨 Смотреть', '📲 Подписаться'],
        ['🚀 Продвижение'],
        ['💶 Мой доход', '🏦 Баланс'],
        ['♻️ Статистика', '⚠️ Информация'],
    ]}
# '🏦 Баланс','👥 Рефералы'
admin = {
    'text': 'Приветсвую вас в админке бота',
    'markup': [
        ['Модерация'], ['Сделать рассылку'], ['Изменить баланс', 'Пополнить баланс', 'Заявки на вывод'], ['⛔️ Отмена']
    ]
}

rules = {
    'text': '''❤️ Исполнителям запрещается
1️⃣ ⛔️ Отписываться от
канала раньше чем 7 дней; 
2⃣ ⛔️Спамить бота 
повторными командами; 
3⃣ ⛔️ Создавать более 
одного аккаунта;
4⃣ ⛔️ Накручивать рефералов;
5⃣ ⛔️ Иметь не понятный профиль - без аватарки, username, и нормального имени. 

‼️ За нарушение обнуления баланса ‼️

⭐️ Рекламодателям запрещается
1️⃣ ⛔️ Убирать права 
у бота до завершения заказа; 
2️⃣ ⛔️ Изменять username 
канала до завершения заказа;

_P.S Если рекламодатель допустит ошибку в продвижении канала или по ошибке переведёт деньги не на тот счёт, Администрация бота ответственности НЕ НЕСЁТ!_''',
    'markup': start['markup']
}

rules2 = {
    'text': '''🔥Наши Акции 🔥
➖➖➖➖➖➖➖➖➖➖➖➖
1️⃣
Акция до 15.01.18
За каждого приведенного друга в нашего бота вы получаете 1р.
Можно привести хоть 1000 друзей, получите 1000р.
Начисления денег за друзей в конце акции (15.01.18)
Действуйте, второй такой акции не будет.
➖➖➖➖➖➖➖➖➖➖➖➖
2️⃣
Если вы приводите нам рекламодателя
который закажет подписчиков на канал
то получаете 25% от вложенной им суммы.
➖➖➖➖➖➖➖➖➖➖➖➖
3️⃣
При пополнение баланса от 500 рублей +100% в подарок.
➖➖➖➖➖➖➖➖➖➖➖➖''',
    'markup': start['markup']
}

rules3 = {
    'text': '''Новости бота - @Newseasymoney''',
    'markup': start['markup']
}

rules4 = {
    'text': '''💯Только лучшее!
〰〰〰〰〰〰〰〰〰〰〰
✅ @vzaimnayapodpiska - Чат для взаимных подписок.
〰〰〰〰〰〰〰〰〰〰〰
✔️Добавление в данный каталог - 1500🅿️ / навсегда
✔️По вопросам писать -  @guldq📨Если спам : @guldq_bot''',
    'markup': start['markup']
}

for_advert = {
    'text': """🤚🏻Добро пожаловать!
Наш бот создан для тех, кто ведёт каналы в Телеграме.
Через бот Вы можете заказать "👥 подписчиков" в Ваш канал,
или купить  "👀просмотры" поста из Вашего канала.
И то и другое повышает цену канала и/или рекламы в нём.
Выберите услугу в меню👇🏻""",
    'markup': [['👁‍🗨 Просмотры', '📲 Подписчики'], ['📮Мои заказы'], ['🔙 Начало']],
}
for_advert_admin = {
    'text': '''*Чтобы начать продвижение вашего канала вам нужно:*
```    
1. Добавить этого бота в администраторы вашего канала. 

2. Переслать любой пост из вашего канала в чат с ботом.

3. Проследовать дальнейшим указаниям бота```[ ]({})'''.format(settings.tutorial_url),
    'markup': [['⛔️ Отмена']],
    'success': {
        'text': '''👑 Все сделано правильно!
👥Теперь введите стоимость 1 подписчика на ваш канал в рублях
⛔️Минимальная стоимость: {} рублей.'''.format(settings.min_post_cost),
        'markup': [['⛔️ Отмена']]
    },
    'success_count': {
        'text': '''Теперь введите желаемое количество подписчиков''',
        'markup': [['⛔️ Отмена']]
    },
    'success_apply': {
        'text': '''Стоимость продвижения канала: {} * {} = {}
        Все верно? Подтвердить?''',
        'markup': [['✅ Подтвердить'], ['⛔️ Отмена']]
    },
    'error_not_admin': {
        'text': '''🚫 Ошибка! Бот не обнаружен в администраторах канала. Добавьте бота и нажите кнопку ниже.''',
        'markup': [[{'text': 'Проверить', 'data': 'check_admin'}, {'text': '❌ Отклонить', 'data': 'cancel_check_admin'}]]
    },
    'error_low_cost': {
        'text': '''🚫 Ошибка!
Минимальная стоимость одного подписчика -  {} руб'''.format(settings.min_post_cost),
        'markup': [['⛔️ Отмена']]
    },
    'success_done': {
        'text': '''Канал добавлен!''',
        'markup': start['markup']
    },
    'error_money': {
        'text': '''🚫 Ошибка! Недостаточно средст на счету''',
        'markup': start['markup']
    },
    'already_in': {
        'text': '''🚫 Ошибка! Канал можно будет добавить заново после вступления добавленного количества подписчиков''',
        'markup': [['📮Мои заказы'], ['⛔️ Отмена']]
    }
}

for_subs = {
    'text': '''*Чтобы начать продвижение вашего канала вам нужно: *
```
1. Добавить этого бота в администраторы вашего канала.

2. Переслать любой пост из вашего канала в чат с ботом.

3. Проследовать дальнейшим указаниям бота```[ ]({})'''.format(settings.tutorial_url),
    'markup': [['⛔️ Отмена']],
    'success': {
        'text': '''👑 Все сделано правильно!
👥Теперь введите стоимость 1 подписчика на ваш канал в рублях
⛔️Минимальная стоимость: {} рублей.'''.format(settings.min_post_cost),
        'markup': [['⛔️ Отмена']]
    },
    'success_count': {
        'text': '''Теперь введите желаемое количество подписчиков''',
        'markup': [['⛔️ Отмена']]
    },
    'success_apply': {
        'text': '''Стоимость продвижения канала: {} * {} = {}
        Все верно? Подтвердить?''',
        'markup': [['✅ Подтвердить'], ['⛔️ Отмена']]
    },
    'error_not_admin': {
        'text': '''🚫 Ошибка! Бот не обнаружен в администраторах канала. Добавьте бота и нажите кнопку ниже.''',
        'markup': [[{'text': 'Проверить', 'data': 'check_admin'}, {'text': '❌ Отклонить', 'data': 'cancel_check_admin'}]]
    },
    'error_low_cost': {
        'text': '''🚫 Ошибка!
Минимальная стоимость одного подписчика -  {} руб'''.format(settings.min_post_cost),
        'markup': [['⛔️ Отмена']]
    },
    'success_done': {
        'text': '''Канал добавлен!''',
        'markup': start['markup']
    },
    'error_money': {
        'text': '''🚫 Ошибка! Недостаточно средст на счету''',
        'markup': start['markup']
    },
    'already_in': {
        'text': '''🚫 Ошибка! Канал можно будет добавить заново после вступления добавленного количества подписчиков''',
        'markup': [['📮Мои заказы'], ['⛔️ Отмена']]
    }
}

view_end = {
    'text': '''🎉Спасибо за подписку, вы получили: {} рублей.
💲Ваш баланс: {} рублей''',
    'markup': start['markup']
}

sub_err = {
    'text': 'Пока нет каналов для подписки, попробуйте позднее.',
    'markup': start['markup']
}

channel_enter_cost = {
    'text': 'Введите стоимость одного показа.',
    'markup': [['⛔️ Отмена']],
    'error': {
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    },
    'error_0.10': {
        'text': 'Ошибка! Стоимость 1 просмотра не может быть ниже 0.1 рубля',
        'markup': [['⛔️ Отмена']]
    }
}
channel_enter_count = {
    'text': 'Введите колличество просмотров',
    'markup': [['⛔️ Отмена']],
    'error': {
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    },
    'error_int': {
        'text': 'Ошибка! Введите целое число',
        'markup': [['⛔️ Отмена']]
    }
}

stat = {
    'text': '''📊 *Статистика проекта*:
    👥Пользователей всего: %all_users%
    👤Пользователей сегодня: %users_today%
    📈Каналов на продвижении: %posts_count%
    📂Постов на продвижении:  %views_count%
    💵Заработано всего: %money_for_views%
    💸Выплачено всего: %money_out%''',
    'markup': start['markup']
}

decline = {
    'text': '''Операция отменена''',
    'markup': start['markup']
}

out_pay = {
    'text': '''К выводу доступно %max_money%. Минимальная сумма - {}. Напиши нужную сумму.'''.format(settings.min_out_pay),
    'markup': [['⛔️ Отмена']],
    'ya': {
        'text': '''К выводу доступно %max_money%. Минимальная сумма - {}. Напиши нужную сумму.'''.format(
            settings.min_out_pay),
        'markup': [['⛔️ Отмена']],
    },
    'error_min_pay': {
        'text': 'Ошибка! Нельзя вывести меньше минимальной суммы',
        'markup': [['⛔️ Отмена']]
    },
    'error_max_pay': {
        'text': 'Ошибка! У вас недостаточно средств на счету',
        'markup': [['⛔️ Отмена']]
    },
    'enter_ya': {
        'text': 'Хорошо! Теперь введите номер вашего кошелька',
        'markup': [['⛔️ Отмена']]
    },
    'enter_qiwi': {
        'text': 'Хорошо! Теперь введите номер телефона, который привязан к QIWI',
        'markup': [['Отправить номер вашего телефона'], ['⛔️ Отмена']]
    },
    'success': {
        'text': 'Вывод будет произведен в течение 24ч.',
        'markup': start['markup']
    }
}

balance = {
    'code': {
        'text': '''🔥Для автоматического пополнения баланса переведите нужную сумму на этот QIWI кошелек `{}` со следующим кодом в комментарии к переводу.
⛔️Очень важно оставить код в комментарии, иначе платеж не будет засчитан!

⚡️После перевода сумма зачислится в течение 1 минуты'''.format(settings.number),
        'markup': start['markup']
    },
    'success': {
        'text': 'Ваш счет пополнен на {}',
        'markup': start['markup']
    },
    'ya': {
        'text': '''🔥 Для автоматического пополнения баланса переведите нужную сумму по [ссылке](https://money.yandex.ru/to/{}) со следующим кодом в комментарии к переводу.
⛔️Очень важно оставить код в комментарии, иначе платеж не будет засчитан!

⚡️После перевода сумма зачислится в течение 1 минуты'''.format(
            settings.ya_number),
        'markup': start['markup']
    }
}

edit_balance = {
    'text': 'Введи имя пользователя с @username или его id',
    'markup': [['⛔️ Отмена']],
    'err_user': {
        'text': 'Ошибка, пользователь не найден',
        'markup': [['⛔️ Отмена']]
    },
    'enter_balance': {
        'text': 'Введите новый баланс пользователя, сейчас он %balance%',
        'markup': [['⛔️ Отмена']]
    },
    'success': {
        'text': 'Новый баланс установлен!',
        'markup': admin['markup']
    },
    'err_number': {
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    }
}

pay_balance = {
    'text': 'Введи имя пользователя с @username или его id',
    'markup': [['⛔️ Отмена']],
    'err_user': {
        'text': 'Ошибка, пользователь не найден',
        'markup': [['⛔️ Отмена']]
    },
    'enter_balance': {
        'text': 'Введите на сколько пополнить, сейчас баланс %balance%',
        'markup': [['⛔️ Отмена']]
    },
    'success': {
        'text': 'Баланс пополнен!',
        'markup': admin['markup']
    },
    'err_number': {
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    }
}

mailer = {
    'text': 'Отправь нужное сообщение для рассылки',
    'markup': [['⛔️ Отмена']],
    'confirm': {
        'text': 'Принято! Разослать?',
        'markup': [['⛔️ Отмена'], ['✅ Подтвердить']],
    },
    'success': {
        'text': 'Ок!',
        'markup': admin['markup']
    }
}

post_enter_cost = {
    'text': 'Введите стоимость каждого просмотра. Стоимость 1 просмотра не может быть ниже 0.05 рубля. Так же чем выше стоимость 1 просмотра - тем выше пост в очереди просмотров.',
    'markup': [['⛔️ Отмена']],
    'error': {
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    },
    'error_0.10': {
        'text': 'Ошибка! Стоимость 1 просмотра не может быть ниже 0.1 рубля',
        'markup': [['⛔️ Отмена']]
    }
}

post_enter_count = {
    'text': 'Введите колличество просмотров, минимальное количество показов 10.',
    'markup': [['⛔️ Отмена']],
    'error': {
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    },
    'error_int': {
        'text': 'Ошибка! Введите целое число',
        'markup': [['⛔️ Отмена']]
    },
    'error_count': {
        'text': 'Ошибка! Минимальное количество показов 10.',
        'markup': [['⛔️ Отмена']]
    }

}

post_success = {
    'text': 'Успешно добавлено.',
    'markup': start['markup']
}

post_received = {
    'text': '''👑 Все сделано правильно!
👁Теперь введите стоимость 1 просмотра на ваш пост в рублях
⛔️Минимальная стоимость: {} рублей.'''.format(settings.min_view_cost),
    'markup': [['⛔️ Отмена']]
}

admin_new = {
    'moderation': {
        'text': 'Что модерировать?',
        'markup': [['Каналы'], ['Посты'], ['⛔️ Отмена']]
    }
}
