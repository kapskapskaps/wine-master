# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Запустите сайт командой `python3 main.py -fp example.xlsx`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Изменения и добавление новых товаров
Чтобы добавить новый товар, нужно:
1. Создать новый .xlsx файл по образцу:

| Категория | Название | Сорт | Цена | Картинка | Акция |
| --------- | -------- | ---- | ---- | -------- | ----- |
|Белые вина|Белая леди|Дамский пальчик|399|belaya_ledi.png|Выгодное предложение|
|Напитки|Коньяк классический|   |350|konyak_klassicheskyi.png|   |

1. При запуске сайта вместо "example.xlsx" указать путь к вашему новому файлу
#### Например: 
- если Вы работаете на Windows `python3 main.py -fp  C:\Users\Username\Desktop\НАЗВАНИЕ_ВАШЕГО_ФАЙЛА.xlxs`
- если Вы работаете на Linux `python3 main.py -fp  /home/user_name/папка_с_файлом/НАЗВАНИЕ_ВАШЕГО_ФАЙЛА.xlxs`	


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
