document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section');
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5, 
    };
    const handleIntersection = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    };
    const observer = new IntersectionObserver(handleIntersection, observerOptions);
    sections.forEach(section => {
        observer.observe(section);
    });
});
