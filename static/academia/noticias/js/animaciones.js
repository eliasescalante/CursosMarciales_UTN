document.addEventListener("DOMContentLoaded", function() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    // Función para animar si esta dentro del viewport
    function animateOnScroll() {
        elements.forEach(element => {
            if (isInViewport(element)) {
                gsap.to(element, { opacity: 1, y: 0, duration: 1 });
            } else {
                gsap.to(element, { opacity: 0, y: 100, duration: 0.5 });
            }
        });
    }

    // verifico si esta en el viewport
    function isInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // aca llamo la funcion en cada scroll
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll();
});
