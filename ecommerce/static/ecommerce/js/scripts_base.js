document.getElementById('searchIcon').addEventListener('click', function(event) {
    event.preventDefault(); // Impede o comportamento padrão do link
    document.getElementById('searchForm').submit(); // Envia o formulário
});