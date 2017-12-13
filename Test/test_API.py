# coding=utf-8
import json
import unittest
import requests as req
import app.api.task.tasks as tasks
import app.api.auth.auth as auth
from random import choice
from string import ascii_lowercase

#URL = 'http://127.0.0.1:13451'
URL = 'http://0.0.0.0:13451'


class TestRegistration(unittest.TestCase):

    @unittest.skip
    def test_registration(self):
        data = json.dumps({
            'Login': 'anton',#.join(choice(ascii_lowercase) for i in range(12)),
            'Password': '2',
            'Name': '3',
            'Surname': '4',
            'Email': 'a@a.ru',
            'Sex': '5',
            'City': '6',
            'Educational': '7',
            'Logo_name': '8',
            'Logo': '9'
        })
        data = req.request('POST', '%s/registration' % URL, data={'Data': data})
        print('registration')
        print(data.text)
        print(data)
        print(data.headers)

    @unittest.skip
    def test_auth(self):
        data = json.dumps({
            'Login': 'anton',
            'Password': '2'
        })
        data = req.request('POST', '%s/auth' % URL, data={'Data': data})
        print('auth')
        print(data.text)
        print(data)
        print(data.headers)

    def test_create_task(self):

        data = [{
                'task_category': 'crypto',
                'task_name': 'Test',
                'task_flag': 'CTF{c0c7c76d30bd3dcaefc96f40275bdc0a}',
                'task_description': 'Отдел тестирования передал вам зашифрованное сообщение, исходное сообщение и легкий алоритм шифрования, по которому было зашифровано это сообщение. Найдите ключ. Зашифрованное сообщение K]GBSAAWVFZ[AFWAF Исходное сообщение: youpassedthistest Ответ переведите в md5 Формат CTF{md5}',
                'task_point': 100,
                'task_hint': '',
                'task_link': 'https://cloud.mail.ru/public/2Q6W/qR1MDtFMZ'
            },
                {
                    'task_category': 'crypto',
                    'task_name': 'Mafia',
                    'task_flag': 'CTF{kawasakipinlox}',
                    'task_description': 'Дон мафии Гендон зашифровал сообщение и передал своему подчиненному Никитосьёну, отделу расследований удалось достать алгоритм шифрования. Расшифруйте сообщение: mikusgwanmxbkz Формат CTF{answer}',
                    'task_point': 200,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/A4F4/5xSadZZ14'
                },

                {
                    'task_category': 'crypto',
                    'task_name': 'Salad',
                    'task_flag': 'CTF{Caesarisnotjustasalad}',
                    'task_description': 'Для поступления на должность криптографа вам выдали тестовое задание.. Расшифруйте: Omqemduezafvgefmemxmp',
                    'task_point': 50,
                    'task_hint': '',
                    'task_link': ''
                },
                {
                    'task_category': 'crypto',
                    'task_name': 'Combo_Wombo',
                    'task_flag': 'CTF{cryptographyiseasy}',
                    'task_description': 'Наши доблесные оперативники перехватили собщение злоумышленников, но что это такое им не понять. Поможете? Перехваченное сообщение: MlHuQfTGMIhsLI96pj6B+2gmbyHrnxTqLIk7px6k0jXu0mB3+2gmA2gqbbCC',
                    'task_point': 400,
                    'task_hint': '',
                    'task_link': ''
                },
                {
                    'task_category': 'exploit',
                    'task_name': 'Meloit',
                    'task_flag': 'CTF{amazing_metaslpoit}',
                    'task_description': 'Вам поступил заказ на взлом компьютера некоторого человека. Предложили хорошую награду и высразу же согласились. Вы проникли в ту же сеть, в которой сейчас находится этот компьютер. И вы узнали его ip адресс: 192.168.0.228. Украдите секретные файлы с его рабочего стола.',
                    'task_point': 200,
                    'task_hint': '',
                    'task_link': ''
                },
                {
                    'task_category': 'Forensic',
                    'task_name': 'Just Find It',
                    'task_flag': 'CTF{GhPD94KO}',
                    'task_description': 'Нам дали новое задание - найти и восстановить личность человека, по имени Gensi Hopster. Один из первых разработчиков системы Лёд. Все его личные файлы - зашифрованы, но мы нашли образ, где когда то хранилась база доступа сотрудников - нам нужен пароль оттуда.',
                    'task_point': 300,
                    'task_hint': '',
                    'task_link': 'https://yadi.sk/d/3AoBpEC23PACLk'
                },
                {
                    'task_category': 'ppc',
                    'task_name': 'Игровые автоматы',
                    'task_flag': 'flag{you_win_1_stage_ppc_casino_you_cool}',
                    'task_description': 'Ты же знаешь, что тут случилось? Никто даже не подумал, что он играет не честно. Я не знал, кто он такой иначе охрана выставила бы его за дверь сразу или отдала вам. Когда система оповестила о том, что один кибер-человек смог выиграть в несколько игр и собрать огромную кучу денег я конечно же не поверил. Но увидев потерю в 36 млн свиткоинов я понял, что он нас обманул. Моя охрана отправилась за ним, но никто так и не вернулся. Поймите меня, мне важно, чтобы его поймали. Я предоставлю возможность сыграть в мои игры и попытаться узнать, как у него это всё получилось. Наше казино самое честное и тут вы не найдете ничего плохого. Удачи и найдите его следы.',
                    'task_point': 100,
                    'task_hint': '',
                    'task_link': ''
                },
                {
                    'task_category': 'ppc',
                    'task_name': 'Рулетка',
                    'task_flag': 'flag{love_base64_and_ppc}',
                    'task_description': 'Стол с рулеткой. Очень популярная игра в нашем казино. Ты же знаешь правила? Запускаем шарик, крутим барабан и вуаля. Я конечно понимаю, в современном мире много причуд и то, что на самом деле это никакой не стол, а всего лишь терминал, как и игровой автомат. Но всё же тоже очень азартно, вводишь свою ставку и смотришь на сколько я стал богаче.. точнее ты)',
                    'task_point': 200,
                    'task_hint': '',
                    'task_link': ''
                },
                {
                    'task_category': 'ppc',
                    'task_name': 'Русская рулетка',
                    'task_flag': 'flag{you_life}',
                    'task_description': 'Скоро ты очутишься там, где ты должен был оказаться уже давно. Мы давно наблюдаем за тобой... Весь город в нашей власти и ты кажется добрался до сердца нашего казино... Теперь тебе решать ты с нами или нет... Каждая секунда замешательства будет дорого стоить... После увиденного ты не сможешь думать, что мир не сошел с ума... Надеюсь ты умеешь пользоваться nc ведь без него тебе не выжить... Я ПРИДУ ЗА ТОБОЙ... Я близко и ты нужен нам... Но тебе одному решать, живым или мертвым...',
                    'task_point': 500,
                    'task_hint': '',
                    'task_link': ''
                },
                {
                    'task_category': 'stego',
                    'task_name': 'GABEN',
                    'task_flag': 'CTF{Gaben_let_the_Half_Life_3}',
                    'task_description': 'Прогуливаясь по городу, в куче мусора вы заметли фотоаппарат. Придя домой, подключив к компьютеру фотоаппарат вы нашли там только эту фотографию. Что же в ней такого необычного?',
                    'task_point': 50,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/9omm/NgwFtiPCV'
                },
                {
                    'task_category': 'stego',
                    'task_name': 'Пресс машина',
                    'task_flag': 'ctf{r@rJpeG}',
                    'task_description': 'Получил по почте картинку, в описании говорилось, что в ней что-то есть',
                    'task_point': 50,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/KDj5/YYfLzmXY1'
                },
                {
                    'task_category': 'stego',
                    'task_name': 'Скрытое сообшение',
                    'task_flag': 'ctf{Hex_message}',
                    'task_description': 'Савьер написал в этой картинке флаг, попробуй найти его',
                    'task_point': 50,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/CKxY/FTnHsEzKQ'
                },
                {
                    'task_category': 'stego',
                    'task_name': 'Черно-желто-белое',
                    'task_flag': 'ctf{stegsolVVVe}',
                    'task_description': 'Было бы забавно поменять цвета флага',
                    'task_point': 200,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/71dw/2BNcshzyU'
                },
                {
                    'task_category': 'stego',
                    'task_name': 'strange balls',
                    'task_flag': 'CTF{c0l0rr}',
                    'task_description': 'HE HA /704Ty /70cT09HH0 /7Pux0g9T cTPAHHblE c006w,EHu9, B0T 0gH0 u3 Hux, HE /70HuMAl0 4T0 3gEcb.',
                    'task_point': 300,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/K8Kz/UMZr6Y2a3'
                },
                {
                    'task_category': 'stego',
                    'task_name': 'bad internet',
                    'task_flag': 'CTF{600d_w0rk_h4x0r}',
                    'task_description': 'Ó MEH9 cJluwK0M MEgJlEHHblu* uHTEPHET, 9 HE M0ry /7P0rPy3uTb KAPTuHKy, H0 TAM cJluwK0M BA}|{HA9 uHcp0PMAL|u9! ÂAM /7PugETc9 cgEJlATb -)T0 cAMuM...',
                    'task_point': 400,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/5YCf/vM8G86vEr'
                },
                {
                    'task_category': 'stego',
                    'task_name': 'QR maniac',
                    'task_flag': 'CTF{1_h473_qr_c0d3}',
                    'task_description': 'T0 T0 BE4H0 B0PyET M0u gAHHblE, HAgEl0cb TE/7EPb ux HE cM0ryT yKPAcTb, /70cJlE T0r0 4T0 9 cgEJlAJl.',
                    'task_point': 500,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/KLWP/tCuRH5e4p'
                },
                {
                    'task_category': 'Recon',
                    'task_name': 'Who are you, mr. Smith? (Part 1)',
                    'task_flag': 'CTF{+7961-873-09-73}',
                    'task_description': 'Тусклый свет и спертый запах разбудили что-то в глубинах моей памяти. Когда-то я бывал здесь. Наверное, тогда я был человеком. Иногда даже жалею, что пошел на это задание. Но настало время возвращать долги. Все что было найдено возле того, что осталось от моего тела – обрывок какой-то листовки. Кажется, это сайт некоего подпольного торговца. Нужно найти способ связаться с ним.',
                    'task_point': 100,
                    'task_hint': '',
                    'task_link': 'http://savepic.net/10265760.htm'
                }, {
                'task_category': 'Recon',
                'task_name': 'Who are you, Mr. Smith? (Part 2)',
                'task_flag': 'CTF{Luxembourg}',
                'task_description': 'Пожалуй, есть что то такое в этом облике. Мгновенная интеграция сознания с мировой сетью позволяет решать задачки по поиску информации в кратчайшие сроки. Как бы не привыкнуть к этому… Мне удалось найти номер телефона, но он не доступен. Судя по всему, у него должно быть место, где он хранит всю личную информацию. Возможно тогда я смогу понять - где его искать… Ответом будет являться город на английском языке.',
                'task_point': 200,
                'task_hint': '',
                'task_link': ''
            },
                {
                    'task_category': 'teacher',
                    'task_name': 'teacher_500.1',
                    'task_flag': 'CTF{90BBBB59F998FA52F8DA70B2D2D878319193D973BA92B0B2FB98B873F9F833DA53F83B7238B09AD0}',
                    'task_description': """Неуклюжий алгоритм.
                                В результате работы следящего ПО с Хоста жертвы был снят алгоритм получения ключевой последовательности.
                                При этом графический интерпретатор алгоритма оказался менее успешным, представив неэффективный громоздкий вычислительный процесс.
                                Исходные данные:
                                * 40-байтовый исходный HEX-код.
                                * Алгоритм преобразования кода в ключевую последовательность.
                                Задача:
                                Получить ключевую последовательность.
                                Значение, представленное в HEX-виде будет являться флагом. Для сдачи флага полученное значение соедините в одну строку.""",
                    'task_point': 500,
                    'task_hint': '',
                    'task_link': """https://cloud.mail.ru/public/2Jvb/ghguUVvVS https://cloud.mail.ru/public/GuUP/cE8ZB76oG"""
                }, {
                'task_category': 'teacher',
                'task_name': 'teacher_500.2',
                'task_flag': 'CTF{209C}',
                'task_description': 'Взлом Maxim Integrated В результате мастерски проведённого дампа памяти системы Н была извлечена программа с функцией проверки контрольного числа подтверждения операции. Система H работает на микроконтроллере с архитектурой ядра MaxQ (производства Maxim Integrated). Исходные данные: * Код программы функции. Задача: * Получить в результате запуска алгоритма программы контрольное число подтверждения. Полученное число в HEX-представлении будет являться флагом.',
                'task_point': 500,
                'task_hint': '',
                'task_link': 'https://cloud.mail.ru/public/K4uu/tiauYgTnj'
            },

                {
                    'task_category': 'joy',
                    'task_name': 'Joy_100',
                    'task_flag': 'CTF{bratishkanechelovek}',
                    'task_description': '''Зацепка так себе, но проверить все же необходимо. В трущобах базируется группировка, что отвергает современные технологии и пользуются уже устаревшей техникой. Вы возможно не поверите, но она работает вся на пару!
                        Поступила наводка, что они могли быть замешаны в инциденте.Возглавляет их человек по
                        кличке Пара-Гон.Если они как то к этому причастны - он отдал приказ.Как бы странно это не звучало, но
                    информация кто он и откуда у нас и спецслужб отсутствует.
                        Вам необходимо связаться с нашими информаторами в трущобах, они смогут вывести вас на Пара - Гона.Будьте
                    бдительны, малейшая ошибка и она испарится и найти его будет невозможно.
                        Ваш первый информатор нелюдим, по этому назначил встречу в нелюдном месте.Он сказал, что б вы подошли к
                    манекену в указанном районе трущоб.Приступайте к расследованию.
                        Вы прибываете на место встречи немного раньше назначенного времени, в надежде, что информатор прибудет
                    раньше и вы сможете побыстрее раскрыть это дело.В ожидании вам ничего не остается, как осмотреть
                    достопримечательности трущоб.Множество медных труб сплетены между собой и уходят куда то под землю.Местами
                    трубы потрескались и из них валит пар.Вокруг вас множество заброшенных домов, на которых висят таблички
                    Аварийной состояние. Подлежит сносу.
                        Спустя длительное время, надышавшись затхлым воздухом трущоб и набродившись в округе, вы осознаете, что
                    никто так и не придет.За время, что вы провели здесь, ни одна живая душа не попалась вам на глаза.Только
                    манекен стоял с ухмылкой глядя на вас.Не выдержав такого отношения вы решили выместить свое негодование на
                    юродивый манекен, но после первого удара, из него выпадают два рисунка и список.Видимо это то, что хотел вам
                    передать информатор! Вам необходимо задокументировать эти предметы как улику, как положено в транслитной форме.Приступайте!
                ''',
                    'task_point': 100,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/5JhU/7pSPegRL2'
                },
                {
                    'task_category': 'joy',
                    'task_name': 'Joy_200',
                    'task_flag': 'CTF{StEaMpUnKinOblIvIoN}',
                    'task_description': 'На первый взгляд казалось, что информатор просто сошел с ума и решил поводить нас за нос, заставляя разгадывать сканворды, но это совсем не так. В этих данных был спрятан шифр, в которых сообщалось, где может находится Пара-Гон. К сожалению информатор шифровал эти данные в спешке, т.к. за ним следили. Часть данных зашифрованно обусловленным алгоритмом, но самая ценная информация была зашифрована неизвестным для нас способом. Может у вас получится разобрать, что же он написал?',
                    'task_point': 200,
                    'task_hint': '',
                    'task_link': 'https://cloud.mail.ru/public/H8Tg/xz2yzh9QA'
                }, {
                'task_category': 'joy',
                'task_name': 'Joy_300',
                'task_flag': 'CTF{$Te@m_PuN|<}',
                'task_description': '''Отлично, вы смогли расшифровать сообщение! Вас незамедлительно отправляют вместе с отрядом захвата по указанному адресу.
                        По дороге к месту предпологаемого нахождения Пара - Гона, вам и группе захвата передаются планы здания и
                    фотографии со спутников и дронов, командир отряда продумывает все детали операции и распределяет своих
                    людей.Как и следовало ожидать, от спецгруппы - до места вы добрались довольно быстро.Все члены отряда и вы
                    расходятся на позиции и ожидают приказа.Но приказ так и не поступил. ЗАСАДА! - единственное, что вы успели
                    подумать, перед тем как вам вкололи что то в шею и вы отключились...
                        Вы приходите в себя, перед глазами все плывет и вы не в состоянии сконцентрироваться.Проходит пара
                    минут, прежде чем вы понимаете, что вас взяли в плен.Надо выбираться!''',
                'task_point': 300,
                'task_hint': '',
                'task_link': 'https://cloud.mail.ru/public/CsMA/HkpTpBd1g'
            }, {
                'task_category': 'joy',
                'task_name': 'Joy_500',
                'task_flag': "CTF{I've_To_Do_Lvl_23_Before_Server_Crush_ Down}",
                'task_description': 'Пара-гон скрылся в толпе. Осматревшись вы замечаете, что манекен снова стоит и к руке у него примотан старый касетный плеер. К нему приклеена записка Я не тот, кто нужен тебе. Но на касете есть информация, которая заинтересует ваших безопасников. Там указано название уязвимости. Желаю удачи. Пара-Гон.',
                'task_point': 500,
                'task_hint': '',
                'task_link': 'https://cloud.mail.ru/public/5PUP/54XKXpGzN'
            },
            {
                'task_category': 'web',
                'task_name': 'Разгон',
                'task_flag': 'flag{4af5fefb25c00bde1561227407b9976c}',
                'task_description': 'Привет, я слышал ты любишь веб и даже знаешь как играть в эту игру. Я подготовил для тебя простое задание с которым справится даже самый маленький ребенок. Ты ВЕБЕР И ЭТО ЗВУЧИТ ГОРДО. http://192.168.0.75:2001/',
                'task_point': 100,
                'task_hint': '',
                'task_link': ''
            },
            {
                'task_category': 'web',
                'task_name': 'Мертвая блокировка',
                'task_flag': 'flag{flag{web_love_or_love_web}}',
                'task_description': 'SQL - инъекции это вчерашний день, а что ты знаешь о блокировках?? Администратор этого сайта почему-то случайно вывел на страницу запрос и дал возможность ввести строку... http://192.168.0.75:2002/',
                'task_point': 200,
                'task_hint': '',
                'task_link': ''
            }

        ]

        for task in data:
            print(tasks.create_one_task(task))

    @unittest.skip
    def test_get_task(self):
        data = {
            'id_event': 1,
            'id_user': 1
        }
        data = tasks.get_task_event(data)
        print(data)

    @unittest.skip
    def test_session(self):
        data = json.dumps({
            'Login': 'anton',
            'Password': '2'
        })
        #data = req.request('POST', '%s/auth' % URL, data={'Data': data})
        data = 'c2f57e8d-bb8a-43c7-aeac-339dc311de71'
        print(data)
        print(auth.session_verification(data))

    @unittest.skip
    def test_check_task(self):
        data = {
            'Task_name': 'Task3',
            'Task_flag': 'flag{flag1flag2}'
        }
        print(tasks.check_task(data))

    @unittest.skip
    def test_requests(self):
        from requests import get
        print(get('{}/task?session=12'.format(URL)).text.encode('utf-8'))

    @unittest.skip
    def test_check_task_http(self):
        from requests import get
        text = '/task?session=12&Task_name=Task2&Task_flag=flag{flag1flag1}'
        print(get('{}{}'.format(URL, text)).text.encode('utf-8'))