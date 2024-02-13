Данный проект используется в практической работе по изучению Nginx, а именно работе с обратным проксированием и с балансировкой нагрузки.

Порядок использования:  

1. Клонируем репозиторий:  
```bash
$ git clone https://github.com/RuslanUsmanov/fastapi-nginx.git
```  
2. Создаем виртуальное окружение:  
```bash
$ cd fastapi-nginx
$ python3 -m venv venv
```  
3. Активируем окружение и устанавливаем зависимости:  
```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```
4. Запускаем `FastAPI` c помощью `uvicorn`:
```bash
$ uvicorn src.main:app --port 8000
```
6. Открываем в браузере http://localhost:8000/api/docs и проверяем работу  FastAPI.  
7. Редактируем конфигурацию Nginx:
```conf
upstream backend {
        server localhost:8000;
    }

server {
    listen 80;
    server_name my.server.com;
    ...
    location /api {
        proxy_pass http://backend;
    }
    ...
}
```
8. Перезапускаем Nginx.
9. Открываем в браузере http://my.server.com/api/ и убеждаемся что обратное проксирование работает.

10. Для балансировки нагрузки запускаем еще 1-2 экземпляра FastAPI на других портах, и дописываем сервера в секции `upstream`, например:  
```conf
upstream backend {
        server localhost:8000 weight=3;
        server localhost:8001;
        server localhost:8002;
    }
```
    При данной конфигурации каждые 5 запросов будут обрабатываться следующим образом: три запроса будут направлены на сервер на порту 8000, на сервера с портами 8001 и 8002 будет отправлено по одному запросу. 
11. Проверку балансировки можно осуществить путем обращения по адресу http://my.server.com/api/getpid. Данный API будет возвращать PID экземпляра FastAPI, обработавшего запрос.
