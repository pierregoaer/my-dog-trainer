const questions = document.querySelectorAll('.faq li .question');

questions.forEach(question => {
    question.addEventListener("click", function(){
        console.log(question.querySelector('.plus-minus-toggle'));
        console.log(question.closest('li'));
        question.querySelector('.plus-minus-toggle').classList.toggle('collapsed');
        question.closest('li').classList.toggle('active');
    })
})

//toggleFAQ(){
//}

//document.querySelector('.faq li .question').click(function () {
//  $(this).find('.plus-minus-toggle').toggleClass('collapsed');
//  $(this).parent().toggleClass('active');
//});