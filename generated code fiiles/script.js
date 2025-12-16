
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('nav ul li a');
    const header = document.querySelector('header');
    const stickyOffset = header.offsetHeight;

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - stickyOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });

                // Close mobile menu if it were implemented
                // document.querySelector('.mobile-menu').classList.remove('active');
            }
        });
    });

    // Simple animation on scroll for elements
    const animatedElements = document.querySelectorAll('.about-text, .skills-grid, .projects-grid, .contact-links');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Observe only once
            }
        });
    }, { threshold: 0.1 });

    animatedElements.forEach(el => {
        observer.observe(el);
    });

    // Add class for fade-in effect on skills tags and project cards when visible
    const skillTags = document.querySelectorAll('.skill-tag');
    const projectCards = document.querySelectorAll('.project-card');

    const appearObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 50); // Stagger the animation
                appearObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    skillTags.forEach(tag => appearObserver.observe(tag));
    projectCards.forEach(card => appearObserver.observe(card));

});

// Add CSS for animations
const styleSheet = document.styleSheets[0]; // Assuming this is the main stylesheet

styleSheet.insertRule(`
    .about-text.is-visible,
    .skills-grid.is-visible,
    .projects-grid.is-visible,
    .contact-links.is-visible {
        opacity: 1;
        transform: translateY(0);
    }
`, styleSheet.cssRules.length);

styleSheet.insertRule(`
    .about-text, .skills-grid, .projects-grid, .contact-links {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease-out, transform 0.6s ease-out;
    }
`, styleSheet.cssRules.length);

styleSheet.insertRule(`
    .skill-tag.visible, .project-card.visible {
        opacity: 1;
        transform: translateY(0) scale(1.02);
    }
`, styleSheet.cssRules.length);

styleSheet.insertRule(`
    .skill-tag, .project-card {
        opacity: 0;
        transform: translateY(30px) scale(0.98);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }
`, styleSheet.cssRules.length);
