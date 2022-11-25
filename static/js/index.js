const questions = document.querySelectorAll('.faq li .question');

questions.forEach(question => {
    question.addEventListener("click", function(){
        question.querySelector('.plus-minus-toggle').classList.toggle('collapsed');
        question.closest('li').classList.toggle('active');
    })
})
