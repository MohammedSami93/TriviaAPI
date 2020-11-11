<h1>Trivia API</h1>

<h2>Getting Started</h2>
    <p>Base URL: At present this app can only run locally. the backend app is hosted at the defult, http://127.0.0.1:5000/, 
    which is set as a proxy in the frontend configration.</p>

<h2>Error Handling</h2>
<p>Errors are returned as JSON objects in the following format:</p>

      {
          "error": 404,
          "massage": "resource not found",
          "seccess": false
      }


The API will return three error types when requests fail:

- 400: Bad request
- 404: Resource not found
- 422: Unprocessable


<h2>Endpoints</h2>    
<h3>GET /categories</h3>
<p>Returns a list of all categories</p>

<p>Sample: curl http://127.0.0.1:5000/categories</p>

        {
            "categories": [
                "Science",
                "Art",
                "Geography",
                "History",
                "Entertainment",
                "Sports"
            ],
            "success": true
        }

<h2>GET /questions</h2>
Returns a list of 10 questions, list of all categories, seccess value, and total number of questions.
        
Sample: curl http://127.0.0.1:5000/questions

        {
            "categories": {
                "1": "Science",
                "2": "Art",
                "3": "Geography",
                "4": "History",
                "5": "Entertainment",
                "6": "Sports"
            },
            "questions": [
                {
                    "answer": "Apollo 13",
                    "category": 5,
                    "difficulty": 4,
                    "id": 2,
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                },
                {
                    "answer": "Maya Angelou",
                    "category": 4,
                    "difficulty": 2,
                    "id": 5,
                    "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                },
                {
                    "answer": "Muhammad Ali",
                    "category": 4,
                    "difficulty": 1,
                    "id": 9,
                    "question": "What boxer's original name is Cassius Clay?"
                },
                {
                    "answer": "Brazil",
                    "category": 6,
                    "difficulty": 3,
                    "id": 10,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                },
                {
                    "answer": "Uruguay",
                    "category": 6,
                    "difficulty": 4,
                    "id": 11,
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                },
                {
                    "answer": "George Washington Carver",
                    "category": 4,
                    "difficulty": 2,
                    "id": 12,
                    "question": "Who invented Peanut Butter?"
                },
                {
                    "answer": "Lake Victoria",
                    "category": 3,
                    "difficulty": 2,
                    "id": 13,
                    "question": "What is the largest lake in Africa?"
                },
                {
                    "answer": "The Palace of Versailles",
                    "category": 3,
                    "difficulty": 3,
                    "id": 14,
                    "question": "In which royal palace would you find the Hall of Mirrors?"
                },
                {
                    "answer": "Escher",
                    "category": 2,
                    "difficulty": 1,
                    "id": 16,
                    "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
                },
                {
                    "answer": "Mona Lisa",
                    "category": 2,
                    "difficulty": 3,
                    "id": 17,
                    "question": "La Giaconda is better known as what?"
                }
            ],
            "success": true,
            "total_questions": 22
        }


<h2>POST /questions</h2>
Add a new question by typing the question, answer, category id, and difficulty. Returns success value, created question id, and total questions.

Sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"how old are you?", "answer":"28", "category":"1", "difficulty":1}'

        {
        "created": 35,
        "success": true,
        "total_questions": 23
        }


<h2>DELETE /question/<int:question_id></h2>
Deletes the question of the given ID if exists. Returns the ID of the deleted question, and seccess value.

Sample: curl -X DELETE http://127.0.0.1:5000/questions/4

        {
        "deleted": 4,
        "success": true
        }


<h2>GET /categories/<int:category_id>/questions</h2>
Returns a list of questions by category, seccess value, total number of questions, and current category type.

Sample: curl http://127.0.0.1:5000/categories/6/questions

        {
            "questions": [
                {
                    "answer": "Brazil",
                    "category": 6,
                    "difficulty": 3,
                    "id": 10,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                },
                {
                    "answer": "Uruguay",
                    "category": 6,
                    "difficulty": 4,
                    "id": 11,
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                }
            ],
            "success": true,
            "total_questions": 23
        }

<h2>POST /search</h2>
Searches for questions, Returns questions based on the search term, seccess value, and total of questions.

Sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "Tom"}'

        {
            "searchTerm": [
                {
                    "answer": "Apollo 13",
                    "category": 5,
                    "difficulty": 4,
                    "id": 2,
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                }
            ],
            "success": true,
            "total_questions": 1
        }
    
<h2>POST /quizzes</h2>
Play quiz game. Returns random question based on certain category or without category.

Sample: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category": {"type": "Art", "id": "2"}}'

        {
            "question": {
                "answer": "Mona Lisa",
                "category": 2,
                "difficulty": 3,
                "id": 17,
                "question": "La Giaconda is better known as what?"
            },
            "success": true
        }


