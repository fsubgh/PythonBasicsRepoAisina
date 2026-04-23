
const questions = [
    {
        questions: 'Мой любимый день недели?',
        answer: ["Четверг", "Суббота", "Воскресенье"],
        correct: 0
    },
    {
        questions: 'Что я больше всего люблю в своем лице',
        answer: ["Нос", "Губы", "Глаза"],
        correct: 2
    },
    {
        questions: 'На что мне больше всего жалко тратить деньги',
        answer: ["Еда", "Косметика", "Транспорт"],
        correct: 1
    },
    {
        questions: 'Чтобы я выбрала?',
        answer: ["Йогурт", "Воздушный рис", "Топтыжка"],
        correct: 1
    },
    {
        questions: 'Какой отдых я бы предпочла?',
        answer: ["В горах", "Выезд на природу", "На море"],
        correct: 2
    }
]
let currentQuestens = 0;
let score = 0;

const qeistiens1 = document.getElementById("qeistiens");
const answer1 = document.getElementById("answer");
const progress1 = document.getElementById("progress");
const result1 = document.getElementById("result");

function showQuestions(){
    const q = questions[currentQuestens];
    qeistiens1.textContent = q.questions;
    answer1.innerHTML = "";

    progress1.textContent = `Вопрос ${currentQuestens + 1} из ${questions.length}`;

    q.answer.forEach((answer, index)=> {
        const button = document.createElement('button');
        button.textContent = answer;

        button.onclick = ()=>{
            if(index === q.correct){
                score++;
        }
        currentQuestens++;
        if(currentQuestens < questions.length){
            showQuestions();
        }else{
            showResult();
        }
    };
    answer1.appendChild(button);
    })}


function showResult(){
    document.getElementById('qiuz').classList.add("hidden");
    result1.classList.remove('hidden');

    let message = '';
    if (score < 2){
        message = "Ты меня совсем не знаешь?"
    }
    else if(score < 3){
        message = "Ну так средне"
    }
    else{
        message = "Ты меня хорошо знаешь!"
    }
    result1.innerHTML = `
    <h2>Твой результат: ${score}/${questions.length}</h2>
    <p>${message}</p>
  `;
}
showQuestions();
