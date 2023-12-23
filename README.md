# 🐈 Отчёт в Google Sheets для QRKot

## 📝 Описание

Проект расширяет возможности приложения QRKot и формирует отчёт в гугл-таблице

В таблице отображаются закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму

## ⚙️ Создайте в корневой директории файл .env со следующим наполнением:
```
APP_TITLE=Приложение QRKot.
APP_DESC=Спасем котиков вместе!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=secretcat
FIRST_SUPERUSER_EMAIL=user@example.com
FIRST_SUPERUSER_PASSWORD=admin
TYPE=service_account
PROJECT_ID=logical-dream-408521
PRIVATE_KEY_ID=ac23e2c7b52b0222cb114ac0774abe780a46cc5d
PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC6Ok4SbsAWnt4w\nV5KVbtrefjKJ7S9GlckgFblOK5skwqkhCjWjBtjQNCYrSN9Qgx9eEAZjRFHTrblY\nFI1EYvErhMjIir4tUOW3DQe8yQLk7+GPPpafK6yo6oRt9rsIk3vdq5EXSZZDaTRQ\nUZrnGGYCeAh4SoVPDPY9KGz4GF8+w91U8xIwC7TTAGE3ADzyE/jxI6VZRjLq2siR\nqQ8ls/3FM8OrszREZfMjypqjtp6C6yOuiltsDPSdYWbPV03PU7S54VLQcw6Du2tP\n7SCJyddcgPWBbGjYoCAz1mwRICk86qPbGVjD8BGrTBuofGlF/KJcOJFX8EPZ0wqv\nhCQjbq3bAgMBAAECggEATyP2B7lPIo3TKMIehii9FK6Wtay5WYrQFTWGMWUwolej\nXmojTyvauehfjCeE14dRrjyrKkZfa9C5ImhhfH17th3Q4gCsPz/Qz5DXB/B4rWgP\n+DsF8ZCy6Hn5W23uH//lNNfzae0Y0X8E/1ketjTVLRlrqAsrSePdRTJH1MsuttH2\nSXUWp9O+lC1cCe9/rDQxSF6G7phniyIqBClD95SE/7tbKm3WehJclkbAlKC1rRiu\nPsNIzOm9XmsLHw1bdNt+FRruQr+54MjWEoHk4OlF3POLtZLuZmGZzDy2neNerox7\nbJ2V3tqlBlQjrPtMk63sO6PDHDUp0QhKwR1lPcGhOQKBgQDbCztRkVmzZfFBfOfj\njv3m5EXCLw/Fttv1Eo0dx4ui6UGmwj/M7j5lJcR6AMPl4vl6iGBHR0gC7lkne84p\n6InAW5Zimffn6NLkg9D3PZ3LzEKCKLnKDRzcXi8i8tt0Q87EFB2+0CXfGIVy+Sh6\nLwfYcvwDmwRqGybkKm+7SwYNdwKBgQDZpbSgTWsDiBoRwLL1Vl206gENZAjxxWS+\nPf33oPoynYMRbvFeWQrOUdJ68THrx1088tw4Hk/NMzvRQ19Gt80P2vz4ajGvNWDu\nTXwHJuOK5R3zm3qwSLa/FqmC6RpydlFTE/RhoVpx82qx+gU6l1CPZnl17CCxnvW5\nLhQHh9prvQKBgEZ45ZvHlMF4EdeM9RosXhnT5XGlLIDi5P+C+W3UTmOaginBoz8u\ng1qNfRn3dw9WKAe5KqikEVIIFxzx4xFupCsEDG0qtiyhpoAovKle5I6158vyiFuu\nPlPT5XxsABj22+YPxsYmN5kATacA7Hnq+a40yEnsrM3qcGfGE26Bo6/fAoGATmzO\nREEBQZmGQ0VbdtnzFCCJ1ohoTK4jGgX+gH9KCHkHZH3EjYmqQiProw9MPLhu2Wpt\nfe82NCu07zfGmhXa107CfsTNOGQUlGnpOi6CKWdbvo8Uy3a4Gu0QkbJrLDmEHlp/\nYbqhe5QJqy37OlyR08pKE/rM4RP1WQ/IedozE0UCgYBB7cqTLbrwxq6/pXPzGubt\nt2rBKBbRc62H5rCq8fVhiwTIHFizs1zOtdSuVPfqflcUr8YDeX20GOY78jod1wBF\nDSeZ2P9Qu2HUWF3EfXxoDhD0TD5+cNLd442pXXawkB4KlQBmHpCto0n8dRMweCwO\nXlYqQBdHapZ9KqesV5FkZA==\n-----END PRIVATE KEY-----\n
CLIENT_EMAIL=practicum-training@logical-dream-408521.iam.gserviceaccount.com
CLIENT_ID=104104068248010729851
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/practicum-training%40logical-dream-408521.iam.gserviceaccount.com
EMAIL=your_gmail@gmail.com
```

## ⚙️ Инструкция по развёртыванию проекта

* клонировать проект на компьютер `git clone https://github.com/tapp41k/cat_charity_fund.git`
* создание виртуального окружения `python3 -m venv venv`
* запуск виртуального окружения `source venv/bin/activate`
* установить зависимости из файла requirements.txt `pip install -r requirements.txt`
* запуск сервера `uvicorn main:app`
* запуск сервера с автоматическим рестартом `uvicorn main:app --reload`
* инициализируем Alembic в проекте `alembic init --template async alembic`
* создание файла миграции `alembic revision --autogenerate -m "migration name"`
* применение миграций `alembic upgrade head`
* отмена миграций `alembic downgrade`
* запуск тестов `pytest`

<h2> Автор проекта </a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32" width="32"/></h2>

[Илья Осадчий](https://github.com/tapp41k)
