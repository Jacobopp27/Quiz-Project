from flask_app.config.mysqlconnection import connectToMySQL


class Like:
    def __init__(self, data):
        self.id = data['id']
        self.like = data['like']
        self.user_id = data['user_id']
        self.quiz_id = data['quiz_id']
    

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO likes (user_id, quiz_id) VALUES ( %(user_id)s , %(quiz_id)s )"
        result = connectToMySQL('quiz_project').query_db(query , formulario)
        return result

    @classmethod
    def get_all(cls, formulario):
        query = "SELECT likes.*, first_name, name FROM likes LEFT JOIN users ON users.id = likes.user_id LEFT JOIN quizes ON quizes.id = likes.quiz_id" 
        results = connectToMySQL('quiz_project').query_db(query, formulario) 
        likes = []
        
        for row in results:
            likes.append(cls(row)) 
        print(results)
        return likes
        

    @classmethod
    def delete_like(cls, formulario): 
        query = "DELETE FROM quiz_project.likes WHERE user_id = %(user_id)s AND quiz_id = %(quiz_id)s"
        result = connectToMySQL('quiz_project').query_db(query, formulario)
        return result