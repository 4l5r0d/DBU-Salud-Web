document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelectorAll('.carousel-slide');
    const wrapper = document.querySelector('.carousel-wrapper');
    let currentSlide = 0;

    function showSlide(index) {
        const offset = -index * 100 + '%';
        wrapper.style.transform = 'translateX(' + offset + ')';
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
    }

    function autoSlide() {
        nextSlide();
    }

    document.getElementById('nextBtn').addEventListener('click', function () {
        clearInterval(intervalId); // Detiene el intervalo al hacer clic manual
        nextSlide();
    });

    document.getElementById('prevBtn').addEventListener('click', function () {
        clearInterval(intervalId); // Detiene el intervalo al hacer clic manual
        prevSlide();
    });

    let intervalId = setInterval(autoSlide, 2000); // Cambia de imagen cada 2 segundos automáticamente
});