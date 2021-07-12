import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
import random


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        #* To create a test database using the trivia.psql file in my local machine, i configured the following line to match the user name & password.
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = "postgresql://postgres:postgres@{}/{}".format('localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    '''
    ✅GET routes unittest

    '''   
    #* test successful operation for GET /categories/<category_id>/questions
    def test_get_questions_based_on_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertTrue(data['questions'])
        self.assertTrue(data['currentCategory'])
        self.assertTrue(data['totalQuestions'])

        # test status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    #! test successful operation for expected errors on GET /categories/<category_id>/questions
    def test_404_if_category_is_dosent_exists(self):
        res = self.client().get('/categories/50/questions')
        data = json.loads(res.data)
        
        # test status code and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')
    
    #* test successful operation for GET /questions
    def test_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        # test if the pagination is correct and if it dose not exceed 10 
        self.assertTrue(len(data['questions']) <= 10)

        # test if the following fields are provided
        self.assertTrue(data['totalQuestions'], data['categories'])

        # test status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    #! test successful operation for expected errors on GET /questions
    def test_404_questions_beyond_boundary(self):
        res = self.client().get('/questions?page=50')
        data = json.loads(res.data)

        # test status code and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')
    
    '''
    ✅POST routes unittest

    '''   
    #* test successful operation for creating a question using POST /questions
    def test_create_question(self):
        
        all_questions_before = len(Question.query.all())
        question_2b_created = {'question':'some question', 'answer':'some answer', 'category':1, 'difficulty':1}

        res = self.client().post('/questions', json=question_2b_created)
        data = json.loads(res.data)

        all_questions_after = len(Question.query.all())

        self.assertTrue(all_questions_after - all_questions_before == 1)
        
        # test status code and message
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
    
    #! test successful operation for expected errors on creating a question using POST /questions
    def test_422_create_question(self):
        all_questions_before = len(Question.query.all())

        question_2b_created = {'question':'some question', 'answer':'some answer', 'category':1}

        res = self.client().post('/questions', json=question_2b_created)
        data = json.loads(res.data)

        all_questions_after = len(Question.query.all())

        self.assertTrue(all_questions_before - all_questions_after == 0)

        # test status code and message
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')

    #* test successful operation for searching a question using POST /questions
    def test_search_question(self):
        res = self.client().post('/questions', json={'searchTerm': 'what'})
        data = json.loads(res.data)

        self.assertTrue(data['totalQuestions'] >= 1)
        self.assertTrue(len(data['questions']) >= 1)

        # test status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    #! test successful operation for expected errors on searching a question using POST /questions
    def test_404_search_question(self):
        res = self.client().post('/questions', json={'searchTerm': 'some_phrase_not_found'})
        data = json.loads(res.data)

        # test status code and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')


    #* test successful operation for playing the quiz using POST /quizzes
    def test_random_question(self):
        res = self.client().post('/quizzes', json={'previous_questions': [19, 17], 'quiz_category': {"type":"Art", "id":"2"}})
        data = json.loads(res.data)

        self.assertEqual(data['question']['category'], 2)
        self.assertNotEqual(data['question']['id'], 19)
        self.assertNotEqual(data['question']['id'], 17)

        # test status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #! test successful operation for expected errors on playing the quiz using POST /quizzes
    def test_400_search_question(self):
        res = self.client().post('/quizzes', json={'previous_questions': [19, 17]})
        data = json.loads(res.data)

        # test status code and message
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
    '''
    ✅DELETE routes unittest

    '''  
    #* test successful operation for DELETE /questions
    def test_delete_question(self):

        question_2b_deleted = Question(question='some question', answer='some answer', category=1 , difficulty=1)
        question_2b_deleted.insert()

        all_questions_before = len(Question.query.all())

        # delete the question and store response
        res = self.client().delete('/questions/'+str(question_2b_deleted.id))
        data = json.loads(res.data)

        # test if this removal will persist in the database and when you refresh the page
        all_questions_after = len(Question.query.all())
        self.assertTrue(all_questions_before - all_questions_after == 1)
        self.assertEqual(Question.query.filter(Question.id == question_2b_deleted.id).one_or_none(), None)

        self.assertTrue(data['id'])

        # test status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #! test successful operation for expected errors on DELETE /questions
    def test_404_delete_no_question(self):
        res = self.client().delete('/questions/100')
        data = json.loads(res.data)
        
        # test status code and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')
    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()