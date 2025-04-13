document.querySelectorAll('.question').forEach((question) => {
    question.addEventListener('mouseenter', () => {
        question.style.backgroundColor = '#d0e4ff';
        question.style.transition = 'background-color 0.3s ease';
    });

    question.addEventListener('mouseleave', () => {
        question.style.backgroundColor = 'transparent';
    });
});