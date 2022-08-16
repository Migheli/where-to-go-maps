# Куда пойти — Москва глазами Артёма
Проект на Django для будущего сайта о самых интересных местах в Москве. Авторский проект Артёма.

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](https://github.com/devmanorg/where-to-go-frontend/blob/master/.gitbook/assets/site.png?raw=true)

[Демка сайта](https://migheli.pythonanywhere.com).

## Как запустить

Python версии 3.9 должен быть уже установлен.
* Скопируйте данный репозиторий
* Установите все зависимости командой
```bash
$ pip install -r requirements.txt
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
Запомните введенные логин и пароль, они потребуются Вам для доступа в "админку" проекта.

* Загрузите данные
Загрузка данных возможна как "вручную", путем использования учетной записи созданного в предыдущем шаге суперпользователя (через "админку" Django).
Такая функция незаменима, позволяет быстро и точечно вносить правки. Однако, первоначальная загрузка большого количества данных может потребовать существенного времени.
В данной связи в проекте предусмотрена специальная команда для загрузки данных:
```bash
$ python manage.py load_place 'place_dir'
```
Аргументом данной команды (то что в примере выше в скобках`'place_dir'`) является путь до директории, с JSON-файлами, содержащего данные о локации в определенном требованиями проекта формате,
либо URL до JSON-файла, например: https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json
Подробнее см. раздел Источники данных. 
Кратко: пример JSON-файла в нужном формате размещен в настоящем репозитории (файл `moscow_legens.json`)
Скрипт автоматически создаст локацию из загруженных в файл данных.
* Запустите тестовый локальный сервер для проверки работоспособности сайта и тестовых данных:
```bash
$ python manage.py runserver
```
* В случае, если Вы последовательно выполнили все предшествующие шаги, перейдя по адресу http://127.0.0.1:8000/
Вы увидите сайт, аналогичный представленному в демо-версии сайта [Демка сайта](https://migheli.pythonanywhere.com). Перейдя в режим администратора http://127.0.0.1:8000/admin с учетными данными,
ранее указанными Вами при создании `superuser` Вы получите доступ в "админку" проекта, где сможете свободно редактировать локации и (или) прилагающиеся к ним фотографии.
Меню "админки" сайта:
<img src=https://i.ibb.co/PgySync/2022-08-14-10-05-04.png>

После проверки и кастомизации всех настроек можете приступать к размещению Вашего проекта на сервере.
Подробные инструкции зависят от выбранного Вами способа деплоя.
Достаточно просто можно задеплоить такой проект с помощью сервиса pythonanywhere.com. 
Перед деплоем рекомендуем ознакомиться с чек-листом из официальной документации Django:
https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
Инструкция по деплою на pythonanywhere здесь:
https://tutorial.djangogirls.org/ru/deploy/index.html#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B1%D0%BB%D0%BE%D0%B3%D0%B0-%D0%BD%D0%B0-pythonanywhere


## Настройки переменных окружения

Переменные окружения объявляются в файле .env который должен лежать в основном каталоге проекта.
Вот описание значений:
* `SECRET_KEY` - секретный ключ проекта 
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-SECRET_KEY
* `DEBUG` - настройки отладочного режима
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-DEBUG
* `ALLOWED_HOSTS` - настройки разрешенных хостов
https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts
* `DEFAULT_DB_NAME` - имя БД, используемой по-умолчанию
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-DATABASES
* `DEFAULT_DB_ENGINE` - движок БД, используемой по-умолчанию 
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-DATABASES
* `LANGUAGE_CODE` - языковой код проекта
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-LANGUAGE_CODE
* `TIME_ZONE` - часовая зона проекта
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-TIME_ZONE
* `USE_I18N` - настройки использования перевода проекта
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-USE_I18N
* `USE_L10N` - настройки локализации форматирования даты.
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-USE_I18N
* `USE_TZ` - настройки использования часовой зоны
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-USE_TZ
* `MEDIA_URL` URL, который обрабатывает медиа, обслуживаемые из MEDIA_ROOT, используемый для managing stored files.
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-MEDIA_URL
* `MEDIA_ROOT` Наименование директории (в корнеовом каталоге проекта), в которой будет храниться user-uploaded files.
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-MEDIA_ROOT
* `STATIC_URL` URL, который обрабатывает статические файлы 
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-STATIC_URL
* `STATICFILES_DIRS` директории, содержащие статические файлы
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-STATICFILES_DIRS
* `STATIC_ROOT='PATH_TO_STATIC_ROOT'`
Путь к директории, в которой collectstatic будет собирать статические файлы для развертывания. По существу указывает, откуда на продакшене будут "браться" файлы для проекта.
https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-STATIC_ROOT


В размещенном в репозитории файле `where_to_go/settigns.py` настройки выполнены с использованием переменных окружения, 
которые Вы можете кастомизировать "под себя".
Ниже пример заполнения файла `.env`, который должен располагаться, как указывалось, в корневой папке проекта. 
От Вас потребуется самостотяельно заполнить переменную `SECRET_KEY` - это "ключ" Вашего проекта.
Остальные настройки уже подготовлены в данном примере для запуска на локальном компьютере в режиме отладки.
Просто создайте в корневом каталоге файл `.env` и скопируйте в него следующее содержимое:

```Python
SECRET_KEY='YOUR_PROJECT_SECRET_KEY'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, .pythonanywhere.com
DEFAULT_DB_ENGINE='django.db.backends.sqlite3'
DEFAULT_DB_NAME='db.sqlite3'
LANGUAGE_CODE='ru-ru'
TIME_ZONE='UTC'
USE_I18N=True
USE_TZ=True
STATICFILES_DIRS=places
```
Обратите внимание: списки передаются без квадратных скобок `[]`, элементы списка перечисляются через запятую.
В переменной `ALLOWED_HOSTS` в качестве примера передано сразу несколько значений - локальный адрес: 127.0.0.1 и хост: .pythonanywhere.com.
При передаче строк указание кавычек - `''` или `""` для заполнения .env файла обязательным не является.
Обратите внимание, что для некоторых переменных в файле `settings.py` заданы значения по-умолчанию.
В случае, если значения этих переменных не будут Вами явно переопределены в файле `.env` проекта, для них будет применено соответствующее значение по-умолчанию. 

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](https://github.com/devmanorg/where-to-go-frontend/blob/master/.gitbook/assets/debug-option.png?raw=true)

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
* `placeId` — уникальный идентификатор локации, строка или число (параметр id задается у модели автоматически).
* `detailsUrl` — адрес для скачивания доп. сведений о локации в JSON формате

Значение поля `placeId` может быть либо строкой, либо числом. Само значение не играет большой роли, важна лишь чтобы оно было уникальным. Фронтенд использует `placeId` чтобы избавиться от дубликатов — если у двух локаций одинаковый `placeId`, то значит это одно и то же место.

Второй источник данных — это те самые адреса в поле `detailsUrl` с подробными сведениями о локации. Каждый раз, когда пользователь выбирает локацию на карте JS код отправляет запрос на сервер и получает картинки, текст и прочую информацию об объекте. 
Для данных целей в проекте реализовано мини-API. View - функция 'show_place_detail' подготавливает, размещаемый по адресу JSON-response в определенном формате.
Формат ответа сервера такой:

```json
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg"
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

