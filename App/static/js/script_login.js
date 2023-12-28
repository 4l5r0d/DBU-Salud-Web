const container = document.getElementById('container');
const codigoBtn = document.getElementById('log2');
const loginBtn = document.getElementById('log1');

codigoBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});