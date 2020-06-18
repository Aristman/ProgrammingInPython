use test;
set names utf8mb4;

-- 1. Выбрать все товары (все поля)
select * from product;

-- 2. Выбрать названия всех автоматизированных складов
select name from store where is_automated>0;

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select store_id from sale group by store_id;


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select distinct store.store_id from store natural left join sale where sale.total is null;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select avg(s.total/s.quantity) from sale s natural left join product p group by p.name;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select name from sale as s natural join product as p group by p.name having count(distinct s.store_id)=1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
select name from sale as s natural join store as st group by st.name having count(distinct s.product_id)=1;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale order by sale.total desc limit 1;

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select r1.date from (select sum(s.total) total, s.date from sale s group by s.date) as r1 order by r1.total desc, r1.date limit 1;
