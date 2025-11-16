// src/js/app.js

// Carrinho de compras (array de produtos)
let carrinho = [];

// Função para adicionar produto ao carrinho
function adicionarAoCarrinho(nome, preco) {
    const produto = { nome, preco };
    carrinho.push(produto);
    atualizarCarrinho();
    alert(`${nome} foi adicionado ao carrinho!`);
}

// Função para atualizar a seção do carrinho na página
function atualizarCarrinho() {
    const carrinhoSection = document.getElementById("carrinho");
    carrinhoSection.innerHTML = "<h2>🛒 Seu Carrinho</h2>";

    if (carrinho.length === 0) {
        carrinhoSection.innerHTML += "<p>Nenhum item adicionado ainda.</p>";
        return;
    }

    let lista = "<ul>";
    let total = 0;

    carrinho.forEach((item, index) => {
        lista += `<li>${item.nome} - R$ ${item.preco.toFixed(2)} 
                  <button onclick="removerDoCarrinho(${index})">Remover</button></li>`;
        total += item.preco;
    });

    lista += "</ul>";
    carrinhoSection.innerHTML += lista;
    carrinhoSection.innerHTML += `<p><strong>Total: R$ ${total.toFixed(2)}</strong></p>`;
    carrinhoSection.innerHTML += `<button onclick="finalizarCompra()">Finalizar Compra</button>`;
}

// Função para remover produto do carrinho
function removerDoCarrinho(index) {
    carrinho.splice(index, 1);
    atualizarCarrinho();
}

// Função para finalizar compra
function finalizarCompra() {
    if (carrinho.length === 0) {
        alert("Seu carrinho está vazio!");
        return;
    }
    alert("Compra finalizada com sucesso! 🎉");
    carrinho = [];
    atualizarCarrinho();
}

// Adiciona eventos aos botões da vitrine
document.addEventListener("DOMContentLoaded", () => {
    const botoes = document.querySelectorAll("#vitrine .produto button");
    botoes.forEach((botao) => {
        botao.addEventListener("click", () => {
            const produtoDiv = botao.parentElement;
            const nome = produtoDiv.querySelector("h3").innerText;
            const preco = parseFloat(produtoDiv.querySelector("p").innerText.replace("R$ ", "").replace(",", "."));
            adicionarAoCarrinho(nome, preco);
        });
    });
});
