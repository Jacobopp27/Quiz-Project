

var ul = document.querySelector('ul');
for (var i = ul.children.length; i >= 0; i--) {
    ul.appendChild(ul.children[Math.random() * i | 0]);
}

var ul = document.querySelector('.ul-2');
for (var i = ul.children.length; i >= 0; i--) {
    ul.appendChild(ul.children[Math.random() * i | 0]);
}

var ul = document.querySelector('.ul-3');
for (var i = ul.children.length; i >= 0; i--) {
    ul.appendChild(ul.children[Math.random() * i | 0]);
}

var ul = document.querySelector('.ul-4');
for (var i = ul.children.length; i >= 0; i--) {
    ul.appendChild(ul.children[Math.random() * i | 0]);
}

var ul = document.querySelector('.ul-5');
for (var i = ul.children.length; i >= 0; i--) {
    ul.appendChild(ul.children[Math.random() * i | 0]);
}




score = []

function save_q1(){
    valorActivo = document.querySelector('input[name="question1"]:checked').value;
    var element = document.getElementById("save-q-1");
    var elementsaved = document.getElementById("saved-q-1");

    elementsaved.classList.remove('hide')
    element.classList.add('hide')

    if (valorActivo == "correct_answer_1" ){
        var valor= 1
        score.push(valor)
        console.log(valor)
        console.log(score)
        return valor

    }
    else{
        var valor0= 0
        console.log(valor0)
        console.log(score)
        return valor0
    }
    
}

function save_q2(){
    valorActivo = document.querySelector('input[name="question2"]:checked').value;

    var element = document.getElementById("save-q-2");
    var elementsaved = document.getElementById("saved-q-2");

    elementsaved.classList.remove('hide')
    element.classList.add('hide')

    if (valorActivo == "correct_answer_2" ){
        var valor= 1
        score.push(valor)
        console.log(valor)
        console.log(score)
        return valor

    }
    else{
        var valor0= 0
        console.log(valor0)
        console.log(score)
        return valor0
    }

}

function save_q3(){
    valorActivo = document.querySelector('input[name="question3"]:checked').value;

    var element = document.getElementById("save-q-3");
    var elementsaved = document.getElementById("saved-q-3");

    elementsaved.classList.remove('hide')
    element.classList.add('hide')

    if (valorActivo == "correct_answer_3" ){
        var valor= 1
        score.push(valor)
        console.log(valor)
        console.log(score)
        return valor

    }
    else{
        var valor0= 0
        console.log(valor0)
        console.log(score)
        return valor0
    }

}

function save_q4(){
    valorActivo = document.querySelector('input[name="question4"]:checked').value;

    var element = document.getElementById("save-q-4");
    var elementsaved = document.getElementById("saved-q-4");

    elementsaved.classList.remove('hide')
    element.classList.add('hide')

    if (valorActivo == "correct_answer_4" ){
        var valor= 1
        score.push(valor)
        console.log(valor)
        console.log(score)
        return valor

    }
    else{
        var valor0= 0
        console.log(valor0)
        console.log(score)
        return valor0
    }

}

function save_q5(){
    valorActivo = document.querySelector('input[name="question5"]:checked').value;

    var element = document.getElementById("save-q-5");
    var elementsaved = document.getElementById("saved-q-5");

    elementsaved.classList.remove('hide')
    element.classList.add('hide')

    if (valorActivo == "correct_answer_5" ){
        var valor= 1
        score.push(valor)
        console.log(valor)
        console.log(score)
        return valor

    }
    else{
        var valor0= 0
        console.log(valor0)
        console.log(score)
        return valor0
    }

}

function results(){
    var final_score = score.length
    console.log(final_score)
    document.getElementById('finalscore').innerHTML = "Your final score is: " + final_score +"/5"

    var element = document.getElementById("playagain");
    element.classList.remove('hide');
    var results = document.getElementById("see-results");
    results.classList.remove('hide');
}

var element = document.getElementById("like");
function like(x){
    var elementliked = document.getElementById("unlike");
    x.classList.add('hide');
    elementliked.classList.remove('hide');
    
}

function unlike(){
    elementliked.classList.add('hide');
    element.classList.remove('hide');
    
}
