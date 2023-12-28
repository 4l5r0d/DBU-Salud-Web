window.onload = function() {
    const formContainer = document.querySelector('.form-container.sign-up');
    const enviarBtn = formContainer.querySelector('button');

    enviarBtn.addEventListener('click', () => {
        formContainer.classList.add("active");
    });

    enviarBtn.addEventListener('click', () => {
        formContainer.classList.remove("active");
    });
}
