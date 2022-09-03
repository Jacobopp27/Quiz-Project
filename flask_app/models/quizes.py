from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Quiz:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.category = data['category']
        self.description = data['description']
        self.question_1 = data['question_1']
        self.correct_answer_1 = data['correct_answer_1']
        self.incorrect_answer_1_1 = data['incorrect_answer_1_1']
        self.incorrect_answer_1_2 = data['incorrect_answer_1_2']
        self.incorrect_answer_1_3 = data['incorrect_answer_1_3']
        self.question_2 = data['question_2']
        self.correct_answer_2 = data['correct_answer_2']
        self.incorrect_answer_2_1 = data['incorrect_answer_2_1']
        self.incorrect_answer_2_2 = data['incorrect_answer_2_2']
        self.incorrect_answer_2_3 = data['incorrect_answer_2_3']
        self.question_3 = data['question_3']
        self.correct_answer_3 = data['correct_answer_3']
        self.incorrect_answer_3_1 = data['incorrect_answer_3_1']
        self.incorrect_answer_3_2 = data['incorrect_answer_3_2']
        self.incorrect_answer_3_3 = data['incorrect_answer_3_3']
        self.question_4 = data['question_4']
        self.correct_answer_4 = data['correct_answer_4']
        self.incorrect_answer_4_1 = data['incorrect_answer_4_1']
        self.incorrect_answer_4_2 = data['incorrect_answer_4_2']
        self.incorrect_answer_4_3 = data['incorrect_answer_4_3']
        self.question_5 = data['question_5']
        self.correct_answer_5 = data['correct_answer_5']
        self.incorrect_answer_5_1 = data['incorrect_answer_5_1']
        self.incorrect_answer_5_2 = data['incorrect_answer_5_2']
        self.incorrect_answer_5_3 = data['incorrect_answer_5_3']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.first_name = data['first_name']

        self.likes = 0


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO quizes (name, category, description, question_1, correct_answer_1, incorrect_answer_1_1, incorrect_answer_1_2, incorrect_answer_1_3, question_2, correct_answer_2, incorrect_answer_2_1, incorrect_answer_2_2, incorrect_answer_2_3, question_3, correct_answer_3, incorrect_answer_3_1, incorrect_answer_3_2, incorrect_answer_3_3, question_4, correct_answer_4, incorrect_answer_4_1, incorrect_answer_4_2, incorrect_answer_4_3, question_5, correct_answer_5, incorrect_answer_5_1, incorrect_answer_5_2, incorrect_answer_5_3, user_id) VALUES (%(name)s, %(category)s , %(description)s , %(question_1)s , %(correct_answer_1)s, %(incorrect_answer_1_1)s, %(incorrect_answer_1_2)s, %(incorrect_answer_1_3)s, %(question_2)s , %(correct_answer_2)s, %(incorrect_answer_2_1)s, %(incorrect_answer_2_2)s, %(incorrect_answer_2_3)s, %(question_3)s , %(correct_answer_3)s, %(incorrect_answer_3_1)s, %(incorrect_answer_3_2)s, %(incorrect_answer_3_3)s, %(question_4)s , %(correct_answer_4)s, %(incorrect_answer_4_1)s, %(incorrect_answer_4_2)s, %(incorrect_answer_4_3)s, %(question_5)s , %(correct_answer_5)s, %(incorrect_answer_5_1)s, %(incorrect_answer_5_2)s, %(incorrect_answer_5_3)s, %(user_id)s)"
        result = connectToMySQL('quiz_project').query_db(query , formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT quizes.*, first_name FROM quizes LEFT JOIN users ON users.id = quizes.user_id;" 
        results = connectToMySQL('quiz_project').query_db(query) 
        quizes = []
        
        for row in results:

            quiz = cls(row)

            valores =  {"id": quiz.id}
            query_likes = "SELECT COUNT(quiz_id) as like_quiz FROM likes WHERE quiz_id = %(id)s"
            results2 = connectToMySQL('quiz_project').query_db(query_likes, valores) 

            quiz.likes = results2[0]["like_quiz"]

            quizes.append(quiz) 
        print(quizes[0].likes)
        return quizes

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT quizes.*, first_name FROM quizes LEFT JOIN users ON users.id = quizes.user_id WHERE quizes.id = %(id)s" 
        result = connectToMySQL('quiz_project').query_db(query, formulario) 
        quiz = cls(result[0]) 
        print(result)
        return quiz

    @classmethod
    def update(cls, formulario):
        query = "UPDATE quizes SET name = %(name)s, category= %(category)s , description=%(description)s ,question_1= %(question_1)s ,correct_answer_1= %(correct_answer_1)s, incorrect_answer_1_1 =%(incorrect_answer_1_1)s, incorrect_answer_1_2 = %(incorrect_answer_1_2)s, incorrect_answer_1_3= %(incorrect_answer_1_3)s, question_2 = %(question_2)s ,correct_answer_2 = %(correct_answer_2)s, incorrect_answer_2_1= %(incorrect_answer_2_1)s, incorrect_answer_2_2 = %(incorrect_answer_2_2)s, incorrect_answer_2_3 = %(incorrect_answer_2_3)s, question_3 = %(question_3)s ,correct_answer_3= %(correct_answer_3)s, incorrect_answer_3_1 = %(incorrect_answer_3_1)s, incorrect_answer_3_2 = %(incorrect_answer_3_2)s, incorrect_answer_3_3 = %(incorrect_answer_3_3)s, question_4 = %(question_4)s , correct_answer_4 = %(correct_answer_4)s, incorrect_answer_4_1 = %(incorrect_answer_4_1)s, incorrect_answer_4_2 = %(incorrect_answer_4_2)s, incorrect_answer_4_3 = %(incorrect_answer_4_3)s, question_5 = %(question_5)s , correct_answer_5 = %(correct_answer_5)s, incorrect_answer_5_1 = %(incorrect_answer_5_1)s, incorrect_answer_5_2 = %(incorrect_answer_5_2)s, incorrect_answer_5_3 = %(incorrect_answer_5_3)s WHERE quizes.id = %(quiz_id)s"
        result = connectToMySQL('quiz_project').query_db(query, formulario)
        print(result)
        return result

    @classmethod
    def delete(cls, formulario): 
        query = "DELETE * FROM quizes WHERE id = %(id)s"
        result = connectToMySQL('quiz_project').query_db(query, formulario)
        return result

    @staticmethod
    def valida_quiz(formulario):
        es_valido_quiz = True
        if len(formulario['name']) < 2:
            flash('Insert a Quiz name', 'create')
            es_valido_quiz = False
        if len(formulario['description']) < 2:
            flash('Insert a Quiz description', 'create')
            es_valido_quiz = False
        if len(formulario['question_1']) < 2 or len(formulario['question_2']) < 2 or len(formulario['question_3']) < 2 or len(formulario['question_4']) < 2 or len(formulario['question_5']) < 2:
            flash('Insert all questions', 'create')
            es_valido_quiz = False
        
        if len(formulario['correct_answer_1']) < 2 or len(formulario['correct_answer_2']) < 2 or len(formulario['correct_answer_3']) < 2 or len(formulario['correct_answer_4']) < 2 or len(formulario['correct_answer_5']) < 2 or len(formulario['incorrect_answer_1_1']) < 2 or len(formulario['incorrect_answer_1_2']) < 2 or len(formulario['incorrect_answer_1_3']) < 2 or len(formulario['incorrect_answer_2_1']) < 2 or len(formulario['incorrect_answer_2_2']) < 2 or len(formulario['incorrect_answer_2_3']) < 2 or len(formulario['incorrect_answer_3_1']) < 2 or len(formulario['incorrect_answer_3_2']) < 2 or len(formulario['incorrect_answer_3_3']) < 2 or len(formulario['incorrect_answer_4_1']) < 2 or len(formulario['incorrect_answer_4_2']) < 2 or len(formulario['incorrect_answer_4_3']) < 2 or len(formulario['incorrect_answer_5_1']) < 2 or len(formulario['incorrect_answer_5_2']) < 2 or len(formulario['incorrect_answer_5_3']) < 2:
            flash('No empty spaces', 'create')
            es_valido_quiz = False


        return es_valido_quiz