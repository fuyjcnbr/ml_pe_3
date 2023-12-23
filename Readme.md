
##Запуск
```shell
uvicorn main:app
```


##Веб интерфейс
http://127.0.0.1:8000


##Пример curl
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "I hate machine learning engineering!"
}'
```



 postman

https://identity.getpostman.com/login?continue=https%3A%2F%2Fweb.postman.co%2F

##Пример curl windows
```shell
curl -X POST http://127.0.0.1:8000/predict/ -H "Content-Type: application/json" -d "{\"text\": \"good news for machine learning!\"}"
```

##Зависимости
```shell
pip install -r requirements.txt
```


