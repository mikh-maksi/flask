function answers(){
    query = ' http://127.0.0.1:5000/save';
    console.log(query);
    fetch(query).then(response => response.json())
    .then(function (quiz) {
    //   question.innerHTML=quiz.question_arr[0];
    //   title.innerHTML = quiz.title_arr[0];
    //   a1.innerHTML = quiz.a1_arr[0];
    //   a2.innerHTML = quiz.a2_arr[0];
    //   a3.innerHTML = quiz.a3_arr[0];
    //   a4.innerHTML = quiz.a4_arr[0];
    //   answer.innerHTML = quiz.answer_arr[0];
      
    //   n_right_answer = quiz.n_right_answer_arr[0];
    //   n_question.value = quiz.total_n;
      console.log(quiz);
        
    });
  }

btn.addEventListener("click",answers);