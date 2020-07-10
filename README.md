# BackendDjangoTodoServer

------------

Для работы с бд локально на пк нужно клонировать этот репозиторий [curl](https://github.com/curl/curl "curl"), он позволит организовывать http запросы локально(и глобально)


####  Парочка команд 
------------
##### Добавление юзера
Создает json пару и отправляет по POST запросу на сервер по адресу
`curl -d id=1  http://127.0.0.1:8000/person`
```json
{"id": "1"}
```
------------
#####  Добавление задачи
Создает json пару и отправляет по POST запросу на сервер по адресу
`curl -d text="how does this work?" -d person_id="1"  http://127.0.0.1:8000/todo`
```json
  {
    "text":"how does this work?",
    "person_id":"1"
    }
```
------------
#### Запуск сервера
Запустить run.bat файл

#### Просмотр данных 
Локальный сервер http://127.0.0.1:8000/

Вкладки:
- person/ -`Выводит всех Person`
- todo/ -`Выводит все Todo`
- person/id/ - `Выводит все Todo с id Person`

