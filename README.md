# Куда пойти — Москва глазами Артёма
Проект на Django для будущего сайта о самых интересных местах в Москве. Авторский проект Артёма.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)

[Демка сайта](https://migheli.pythonanywhere.com).

## Как запустить

Python версии 3.9 должен быть уже установлен.
* Скопируйте данный репозиторий
* Установите все зависимости командой
```bash
$ pip install -r -requirements.txt
```
* Настройте переменные окружения (стандартные для Django-проекта, о них будет подробнее в следующем разделе)
* Сделайте миграцию моделей в Вашу БД: 

```bash
$ python manage.py migrate
```

* Создайте суперпользователя (администратора) командой:
```bash
$ python manage.py createsuperuser
```

* Загрузите данные
Загрузка данных возможна как "вручную", путем использования учетной записи созданного в предыдущем шаге суперпользователя (через "админку" Django).
Такая функция незаменима, позволяет быстро и точечно вносить правки. Однако, первоначальная загрузка большого количества данных может потребовать существенного времени.
В данной связи в проекте предусмотрена специальная команда для загрузки данных:
```bash
$ python manage.py load_place 'place_dir'
```
Аргументом данной команды (то что в примере выше в скобках`'place_dir'`) является путь до директории, с JSON-файлами, содержащего данные о локации в определенном требованиями проекта формате.
Подробнее см. раздел Источники данных.
Кратко: пример JSON-файла в нужном формате размещен в настоящем репозитории (файл `moscow_legens.json`)
Скрипт автоматически создаст локацию из загруженных в файл данных.


* Запустите тестовый локальный сервер для проверки работосособности сайта и тестовых данных:
```bash
$ python manage.py runserver
```
После проверки и кастомизации всех настроек можете приступать к размещению Вашего проекта на сервере.
Подробные инструкции зависят от выбранного Вами способа деплоя.
Достаточно просто можно задеплоить такой проект с помощью сервиса pythonanywhere.com. 
Перед деплоем рекомендуем ознакомиться с чек-листом из официальной документации Django:
https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
Инструкция по деплою на pythonanywhere здесь:
https://tutorial.djangogirls.org/ru/deploy/index.html#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B1%D0%BB%D0%BE%D0%B3%D0%B0-%D0%BD%D0%B0-pythonanywhere

## Настройки перменных окружения

Для корректного запуска проекта необходимо предварительно указать переменные окружения 
Перменные объявляются в файле .env который должен лежать в основном каталоге проекта.
Вот описание значений: 
```Python
#Секретный ключ Вашего Django-проекта
SECRET_KEY='YOUR_PROJECT_SECRET_KEY'

#Булево значение - включение/отключение дебаг-режима. В продакшене должно быть False.
DEBUG='BOOLEAN_TRUE_OR_FALSE'

#имена хостов/доменов, которые может обслуживать данный Django-сайт. Это мера безопасности для предотвращения HTTP Host header attacks, которые возможны даже при многих, казалось бы, безопасных конфигурациях веб-серверов
ALLOWED_HOST='YOUR_ALLOWED_HOSTS_TO_DEPLOY'

#путь до папки с файлами Template (шаблонами) Вашего проекта
TEMPLATE_DIR='PATH_TO_DIRECTORY_WITH_PROJECT_TEMPLATES'

#Имя используемой по-умолчанию проектом базы данных
DEFAULT_DB_NAME='PROJECT_DB_NAME'

#Движок используемой по-умолчанию проектом базы данных
DEFAULT_DB_ENGINE='PROJECT_DB_ENGINE'

#Языковой код
LANGUAGE_CODE='PROJECT_LANGUAGE_CODE'

#Часовой пояс
TIME_ZONE='TIME_ZONE'

#Булево значение, определяющее, должна ли быть включена система перевода Django. Это дает возможность отключить ее для повышения производительности. Если это значение установлено в False, Django сделает некоторые оптимизации, чтобы не загружать механизм перевода.
USE_I18N='BOOLEAN_TRUE_OR_FALSE'

#Строка, представляющая часовой пояс для данного соединения с базой данных или None. Этот внутренний параметр настройки DATABASES принимает те же значения, что и общий параметр TIME_ZONE
USE_TZ='True'


#URL, который обрабатывает медиа, обслуживаемые из MEDIA_ROOT, используемый для managing stored files.
MEDIA_URL='URL_TO_HANDLE_MEDIA'

#Абсолютный путь файловой системы к директории, в которой будет храниться user-uploaded files.
MEDIA_ROOT='PATH_TO_MEDIA_DIR'

STATIC_URL='URL_TO_HANDLE_STATIC'

#Строка, содержащая полные пути к каталогу (каталогам) дополнительных файлов.
STATICFILE_DIR='PATH_TO_ADDITIONAL_STATIC_DIRS'
#В зависимости от способа размещения файлов, избранного Вами, может быть несколько значений , ниже приведены условные ссылки, лишь для примера:
STATICFILES_DIRS = [
    "/home/special.polls.com/polls/static",
    "/home/polls.com/polls/static",
    "/opt/webfiles/common",
]
#Для такого примера Вам потребуется прописать settings.py следующим образом и задать соответствующие переменные окружения `ENV_VARIABLE_STATICFILE_DIR1` `ENV_VARIABLE_STATICFILE_DIR2` `ENV_VARIABLE_STATICFILE_DIR3` и так далее:

STATICFILES_DIRS = [
    os.getenv('ENV_VARIABLE_STATICFILE_DIR1'),
    os.getenv('ENV_VARIABLE_STATICFILE_DIR2'),
    os.getenv('ENV_VARIABLE_STATICFILE_DIR3'),
]

#Абсолютный путь к директории, в которой collectstatic будет собирать статические файлы для развертывания. По существу указывает, откуда на продакшене будут "браться" файлы для проекта.
STATIC_ROOT='PATH_TO_STATIC_ROOT'
```

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

<a href="#" id="data-sources"></a>

## Источники данных

Фронтенд получает данные для отрисовки "локаций" из JSON-файлов с определенного формата. Образец правильно оформленного JSON файла размещен в настоящем репозитории.
Шаблон подготавливается на основе данных моделей из БД с помощью view-функции.
Ниже приведен формат генерируемого функцией кода:

```javascript
<script id="places-geojson" type="application/json">
  {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [37.62, 55.793676]
        },
        "properties": {
          // Специфичные для этого сайта данные
          "title": "Легенды Москвы",
          "placeId": "moscow_legends",
          "detailsUrl": "./places/moscow_legends.json"
        }
      },
      // ...
    ]
  }
</script>
```

При загрузке страницы JS код ищет тег с id `places-geojson`, считывает содержимое и помещает все объекты на карту.

Данные записаны в [формате GeoJSON](https://ru.wikipedia.org/wiki/GeoJSON). Все поля здесь стандартные, кроме `properties`. Внутри `properties` лежат специфичные для проекта данные:

* `title` — название локации
* `placeId` — уникальный идентификатор локации, строка или число. В предложенном варианте данный параметр равен `title`, поскольку названия локаций не дулируются.
* `detailsUrl` — адрес для скачивания доп. сведений о локации в JSON формате

Значение поля `placeId` может быть либо строкой, либо числом. Само значение не играет большой роли, важна лишь чтобы оно было уникальным. Фронтенд использует `placeId` чтобы избавиться от дубликатов — если у двух локаций одинаковый `placeId`, то значит это одно и то же место.

Второй источник данных — это те самые адреса в поле `detailsUrl` c подробными сведениями о локации. Каждый раз, когда пользователь выбирает локацию на карте JS код отправляет запрос на сервер и получает картинки, текст и прочую информацию об объекте. 
Для данных целей в проекте реализовано мини-API. View - функция 'show_place_detail' подготавливает, размещаемый по адресу JSON-response в определенном формате.
Формат ответа сервера такой:

```javascript
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
