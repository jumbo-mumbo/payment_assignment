## Тестовое задание: [Условия.](https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit)

# Запускаем через Docker
1) Клонируем репозиторий:
```
git clone https://github.com/RussianProgram/payment_assignment
```

2) Билдим образы и поднимаем контейнеры через docker-compose
```
cd /payment_assignment
docker-compose up
```
3) Миграции и тестовые данные уже применены в **entrypoint.sh**
5) Вход в админ панель
```
username: jumbo
password: ego
```

## Готово! 
**Фронт-клиент:**
```
http://localhost:8080/
```
1) Страница с продуктом
```
http://localhost:8080/shop/item/id 

[id = id продукта (пр-р: 1,2,3..)]

http://localhost:8080/shop/item/2
```
2) Страница с заказом
```
http://localhost:8080/shop/order/order_id

[order_id = id заказа (пр-р: uuid4)]

http://localhost:8080/shop/order/8ae1919c-981b-4e7d-b484-e08a9998f62f
```


**Бэк:**
```
 http://127.0.0.1:8000/api/ 
```
1) Админка:
```
 http://127.0.0.1:8000/admin
```