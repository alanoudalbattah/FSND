from flask import (
  Flask, abort,
  request, jsonify)
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  ✅@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app, resources={r"/api/*": {"origins": "*"}})
  '''
  ✅@TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  #? Access-Control-Allow-Origin: What client domains can access its resources. For any domain use *
  #? Access-Control-Allow-Credentials: Only if using cookies for authentication - in which case its value must be true
  #? Access-Control-Allow-Methods: List of HTTP request types allowed
  #? Access-Control-Allow-Headers: List of http request header values the server will allow, particularly useful if you use any custom headers
  @app.after_request
  def after_request(res):
      res.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return res

  '''
  ✅@TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def categories():
    
    return jsonify({
      'success': True,
      'categories': {category.id: category.type for category in  Category.query.all()}
      }), 200

  '''
  ✅@TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def questions():
     
    #* Implement pagniation
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    #* ---------------------

    total_questions = [question.format() for question in Question.query.all()]
    paginated_questions = total_questions[start:end]
    
    if (len(paginated_questions)==0): abort(404) # abort if no questions were formatted (no need for a new page)!

    return jsonify({
      'questions':paginated_questions,
      'totalQuestions': len(total_questions),
      'categories': {category.id: category.type for category in Category.query.all()},
      'currentCategory': None, #! can i make use of it?
      'success': True
      }), 200

  '''
  ✅@TODO: 
  Create an endpoint to DELETE question using a question ID. 

  ✅TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):

    Question.query.get_or_404(question_id).delete()
    
    return jsonify({'id':question_id, 'success': True}), 200 #? Optional --> return the id to make the frontend remove the question using the id
 

  '''
  ✅@TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  ✅TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  def create_question():
      body = request.get_json()
      data = [body.get('question'),body.get('answer'),body.get('difficulty'),body.get('category')]
      
      for required in data: # checks if all required fields are present
        if (required == None): abort(422) #! maybe 400?

      Question(data[0],data[1],data[2],data[3]).insert() # create a new question
      
      return jsonify({'success': True}), 201 # status code 201 stand for created :)

  '''
  ✅@TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question.

  ✅TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  def search_question(search_term):
    
      search_results = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()# search is case insensitive :)  
      
      if (len(search_results)==0): abort(404)

      formatted_questions = [question.format() for question in search_results] 

      return jsonify({
        "questions": formatted_questions,
        "totalQuestions": len(formatted_questions),
        'currentCategory': None, #! hmmmm
        'success': True
      }), 200

  #? This route handle all post requests for /questions
  @app.route('/questions', methods=['POST'])
  def create_or_search():

    search_term = request.get_json().get('searchTerm')

    return create_question() if (search_term == None) else search_question(search_term)

  '''
  ✅@TODO: 
  Create a GET endpoint to get questions based on category. 

  ✅TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def questions_in_category(category_id):

    category = Category.query.get_or_404(category_id) # check if category exists
    questions_in_category = Question.query.filter_by(category=category_id).all()

    return jsonify({
      'questions': [question.format() for question in questions_in_category],
      'totalQuestions': len(questions_in_category),
      'currentCategory': category.type,
      'success': True
    }), 200


  '''
  ✅@TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  ✅TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def random_question():

    previous_questions = request.get_json().get('previous_questions')
    quiz_category = request.get_json().get('quiz_category')

    if(previous_questions==None or quiz_category==None): abort(400)

    if(quiz_category['id'] == 0): #if the random question is within all categories
      questions = Question.query.all()       
    else: #if the random question is within a specific category  
      questions = Question.query.filter_by(category=quiz_category['id']).all() 


    if (len(previous_questions)==0): return jsonify({'question': questions[random.randrange(0, len(questions), 1)].format(), 'success': True}), 200 
    # this line handles the case where all questions have been asked before
    if (len(questions)==len(previous_questions)): return jsonify({'success': True}), 200

    #? A question is chosen if it meets the two conditions: 1-random 2-have not been asked before
    question = None
    while(question==None):
        question = questions[random.randrange(0, len(questions), 1)]#* random
        for id in previous_questions: #* cheak if the question have not been asked before
          if (question.id == id):
              question = None 
              break #! have been asked before

    return jsonify({'question': question.format(), 'success': True}), 200 


  '''
  ✅@TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(400)
  #? indicates that the server cannot or will not process the request
  #? due to something that is perceived to be a client error 
  def bad_request(error):
      return jsonify({
          "success": False, 
          "message": "Bad request"
          }), 400

  @app.errorhandler(404)
  #? 404, not found :)
  def not_found(error):
      return jsonify({
          "success": False, 
          "message": "Not found"
          }), 404

  @app.errorhandler(405)
  #? indicates that the request method is known by the server but is
  #? not supported by the target resource.
  def method_not_allowed(error):
      return jsonify({
          "success": False, 
          "message": "Method not allowed"
          }), 405

  @app.errorhandler(422)
  #? indicates that the server understands the content type of the request
  #? entity, and the syntax of the request entity is correct, but it was
  #? unable to process the contained instructions.
  def unprocessable_entity(error):
      return jsonify({
          "success": False, 
          "message": "Unprocessable entity"
          }), 422

  @app.errorhandler(500)
  #? 500, internal server error :)
  def internal_server_error(error):
      return jsonify({
          "success": False, 
          "message": "Internal server error"
          }), 500
#* Status Code Source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
  return app  