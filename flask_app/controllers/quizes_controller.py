from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User
from flask_app.models.quizes import Quiz
from flask_app.models.likes import Like


@app.route('/new')
def new():
    if 'user_id' not in session: 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }
    
    user = User.get_by_id(formulario)
    return render_template('create_quiz.html', user=user)

@app.route('/create/quiz', methods=['POST'])
def create_quiz():
    if 'user_id' not in session:  
        return redirect('/')

    if not Quiz.valida_quiz(request.form):
        return redirect('/create/quiz')
    else:
        Quiz.save(request.form)
        return redirect('/dashboard')





@app.route('/play/quiz/<int:id>')  
def play_quiz(id):
    if 'user_id' not in session:  
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) 


    formulario = { "id": id }
    quiz = Quiz.get_by_id(formulario)

    return render_template('play.html', user=user, quiz=quiz)


@app.route('/results/<int:id>')  
def results(id):
    if 'user_id' not in session:  
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) 


    formulario = { "id": id }
    quiz = Quiz.get_by_id(formulario)

    return render_template('results.html', user=user, quiz=quiz)

    
@app.route('/show/quiz/<int:id>')  
def show_quiz(id):
    if 'user_id' not in session:  
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario) 


    formulario = { "id": id }
    quiz = Quiz.get_by_id(formulario)

    return render_template('show.html', user=user, quiz=quiz)


@app.route('/edit/quiz/<int:id>') 
def edit_quiz(id):
    if 'user_id' not in session: 
        return redirect('/')
    
    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario)
    formulario_quiz = { "id": id }

    quiz = Quiz.get_by_id(formulario_quiz)

    return render_template('edit.html', user=user, quiz=quiz)


@app.route('/update/quiz', methods=['POST'])
def update_quiz():
    if 'user_id' not in session:
        return redirect('/')
    
    Quiz.update(request.form)

    return redirect('/dashboard')


@app.route('/delete/like/<int:user_id>/<int:quiz_id>')
def delete_like(user_id, quiz_id):
    if 'user_id' not in session:  
        return redirect('/')
    
    formulario = {"user_id": user_id, "quiz_id":quiz_id}
    Like.delete_like(formulario)

    return redirect('/dashboard')

@app.route('/like/<int:user_id>/<int:quiz_id>', methods=['POST'])
def like(user_id, quiz_id):
    if 'user_id' not in session:  
        return redirect('/')

    formulario = {"user_id": user_id, "quiz_id":quiz_id}
    Like.save(formulario)
    return redirect('/dashboard')