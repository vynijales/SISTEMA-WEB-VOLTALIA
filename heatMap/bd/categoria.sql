select categoria.descricao, sum(produto.valor)
from categoria
inner join produto on produto.categoria_id = categoria.id group by categoria.descricao