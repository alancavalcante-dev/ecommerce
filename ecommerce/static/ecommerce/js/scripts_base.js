document.getElementById('searchIcon').addEventListener('click', function(event) {
    event.preventDefault(); // Impede o comportamento padrão do link
    document.getElementById('searchForm').submit(); // Envia o formulário
});


function releaseCart() {
    var url = 'http://127.0.0.1:8000/api/v1/cart/numbers-products/'
        fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer '+ '{{ token }}',
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Produto adicionado ao carrinho:', data);
        })
        .catch(error => {
            console.error('Erro ao adicionar ao carrinho:', error);
            window.location.href = '/login/';
        });
}



function numberIconCart(token) {
    var url = 'http://127.0.0.1:8000/api/v1/cart/quantity-products/'

    fetch(url, {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer '+ token
        }
    })
    .then(response => response.json())
    .then(data => {
        // Adicionar dados numbers-products no icone
        var quantity = data.quantity
        if (quantity > 0) {
            var span = document.createElement('span');
            var cartLink = document.getElementById('cart');

            span.textContent = quantity 
            span.setAttribute('id', 'numbers-product');
            cartLink.appendChild(span);
        }

    })
    .catch(error => {
        console.error('Erro ao consultar o número de produtos do carrinho: '+ error);
    });
}



numberIconCart