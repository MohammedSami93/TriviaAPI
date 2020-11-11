import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  cors = CORS()

  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response
  
  
  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    formatted_categories = [category.type for category in categories]

    if len(formatted_categories) == 0:
      abort(404)

    return jsonify({
      'success':True,
      'categories': formatted_categories
    }) 

  
  @app.route('/questions')
  def get_questions():
    selection = Question.query.order_by(Question.id).all()
    total_questions = len(selection) 
    current_questions = paginate_questions(request, selection)
    #print("current_questions = ",current_questions)
    categories = Category.query.all()
    formatted_categories = [category.type for category in categories]

    #print(formatted_categories[0])
    data2={
           1:formatted_categories[0],
           2:formatted_categories[1],
           3:formatted_categories[2],
           4:formatted_categories[3],
           5:formatted_categories[4],
           6:formatted_categories[5]}
    
    #print ("HERE",data2)
    if len(current_questions) == 0:
      abort(404)
    
    return jsonify({
      'success':True,
      'questions': current_questions,
      'total_questions': len(Question.query.all()),
      'categories': data2
      })

  
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)

      question.delete()

      return jsonify({
        'success':True,
        'deleted': question_id
      })
    
    except:
      abort(422)

  
  @app.route('/questions', methods=['POST'])
  def add_question():

    body = request.get_json()

    new_question = body.get('question',None)
    new_answer = body.get('answer',None)
    new_category = body.get('category',None)
    new_difficulty = body.get('difficulty',None)


    question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)

    question.insert()

    return jsonify({
      'success':True,
      'created': question.id,
      'total_questions': len(Question.query.all())
    })


  @app.route('/search', methods=['POST'])
  def search():
    
    body = request.get_json()
    #print(body, "check the answer")
    
    searchTerm = body['searchTerm']
    #print(searchTerm, "next")

    selection = Question.query.filter(Question.question.ilike(f'%{searchTerm}%')).all()
    #print("first selection: ",selection)
    
    selection = [i.format() for i in selection]
    #print("here's the search",selection)
    
    if len(selection) == 0:
      abort(404)

    return jsonify({
      'success':True,
      'searchTerm': selection,
      'total_questions': len(selection)
    })


  @app.route('/categories/<int:category_id>/questions')
  def get_questions_by_category(category_id):
    
    selection = Question.query.filter(Question.category == category_id).all()
    #print("here's the selection: ",selection)

    current_questions = paginate_questions(request, selection)
    
    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(Question.query.all())
      })

  
  @app.route('/quizzes', methods=['POST'])
  def post_quiz():
    
    body = request.get_json()
    #print("here's the body",body)

    categoryID = body['quiz_category']
    ID = categoryID["id"]
    #print(categoryID, "is the category ID")
    #print("the ID is: ",ID)


    if (ID == 0):
       selection = Question.query.all()
      #  print(questions) 

    else:
       selection = Question.query.filter(Question.category == ID).all()
      #  print(selection)
    
    if selection is None:
      abort(400)
      
    selection = [i.format() for i in selection]
    #print(selection)

    random_question = random.choice(selection)
    #print(random_question)
    
    return jsonify({
            'success': True,
            'question': random_question
      })


  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "seccess": False,
      "error": 404,
      "massage": "Resource not found"
    }), 404


  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "seccess": False,
      "error": 422,
      "massage": "Unprocessable"
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "seccess": False,
      "error": 400,
      "massage": "Bad request"
    }), 400


  
  return app