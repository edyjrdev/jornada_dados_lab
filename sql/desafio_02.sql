-- 1. Cria um relatório para todos os pedidos de 1996 e seus clientes (152 linhas)
select *
from orders o
inner join customers c on o.customer_id = c.customer_id
where date_part('YEAR', order_date) = '1996' 
-- 2. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários (5 linhas)
select e.city, count(distinct c.customer_id) as qtd_cliente
from employees e
left join customers c on e.city = c.city
group by e.city

-- 3. Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes (69 linhas)
select c.city, 
	count(distinct c.customer_id) as qtd_cliente,
	count(distinct e.employee_id) as qtd_funcionario
from employees e
right join customers c on e.city = c.city
group by c.city
	
-- 4.Cria um relatório que mostra o número de funcionários e clientes de cada cidade (71 linhas)
select c.city, 
	count(distinct c.customer_id) as qtd_cliente,
	e.city,
	count(distinct e.employee_id) as qtd_funcionario
from employees e
full join customers c on e.city = c.city
group by c.city,e.city


-- 5. Cria um relatório que mostra a quantidade total de produtos encomendados.
-- Mostra apenas registros para produtos para os quais a quantidade encomendada é menor que 200 (5 linhas)
select distinct p.product_name, sum(od.quantity) as total
from orders o 
inner join order_details od on o.order_id = od.order_id
inner join products p on od.product_id = p.product_id
group by p.product_name
having sum(od.quantity) < 200
order by total, p.product_name

-- 6. Cria um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996.
-- O relatório deve retornar apenas linhas para as quais o total de pedidos é maior que 15 (5 linhas)
select distinct c.contact_name, count(o.order_id) as pedidos
from orders o
inner join customers c on o.customer_id = c.customer_id
where o.order_date > '1996-12-31'
group by c.contact_name
having count(o.order_id) > 15
order by c.contact_name, pedidos