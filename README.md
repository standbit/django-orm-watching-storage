# django-orm-watching-storage
Репозиторий с сайтом для урока «Пишем пульт охранника банка» курса dvmn.org

Программа позволяет отслеживать, кто находится в хранилище банка в данный момент времени. Выводит всех владельцев активных пропусков. Показывает, кто, когда и как долго находился в хранилище. Также позволяет узнать, кто из посетителей подозрителен - провел в хранилище больше часа. 

## Установка программы
1. Склонируйте репозиторий к себе на компьютер
2. Дальше работайте в консоли. Cоздайте папку виртуального окружения
```python
$ virtualenv venv
```
3. Активируйте виртуальное окружение
```python
$ source venv/bin/activate
```
4. Установите зависимости
```python
$ python3 -m pip install -r requirements.txt
```

## Запуск скрипта
1. Запустите скрипт, выполнив команду
```python
$ python manage.py runserver 0.0.0.0:8000
```
2. Перейдите на [localhost](http://localhost:8000/)
3. В открывшемся окне браузера можете работать
4. Остановить выполнение программы в консоли: `Ctrl+C`