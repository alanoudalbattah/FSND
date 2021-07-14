# Trivia - Full Stack API Project

The project's objective is to learn how to structure plan, implement, document, and test an API. Udacity provides an initial prototype design of the Trivia website. Trivia display questions both all questions and by category, delete questions, add questions and require that they include a question and an answer text, search for questions based on a text query string, and finally, play the quiz game, randomizing either all questions or within a specific category. Completing this trivia app will help acquire the essential skills for enabling applications to communicate with other application.

## Getting Started

Follow instruction in [./backend](https://github.com/alanoudalbattah/Trivia/tree/master/Trivia\_API/backend/README.md) and [./frontend](https://github.com/alanoudalbattah/Trivia/tree/master/Trivia\_API/frontend/README.md)

## Endpoints

```

GET '/categories'

GET '/questions'

GET '/categories/${id}/questions'

POST '/questions'

POST '/quizzes'

DELETE '/questions/${id}'

```  

## Endpoints Examples

```

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs. 
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true
}
```

```

GET '/questions?page=${integer}'
- Fetches a paginated set of questions, a total number of questions, all categories and current category string. 
- Request Arguments: page - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "currentCategory": null,
    "questions": [
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        }
    ],
    "success": true,
    "totalQuestions": 18
}

```
<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125356000-55c7d780-e36e-11eb-9209-502dfb7d41ba.png">
</p>
<p align = "center">
Fig.1 - GET categories and GET questions frontend expected view
</p>

```

GET '/categories/${id}/questions'
- Fetches questions for a cateogry specified by id request argument 
- Request Arguments: id - integer
- Returns: An object with questions for the specified category, total questions, and current category string 
{
    "currentCategory": "Sports",
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
    "totalQuestions": 2
}

```
<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125356302-b1926080-e36e-11eb-821e-1cb8bf1e2b04.png">
</p>
<p align = "center">
Fig.2 - GET questions based on category frontend expected view
</p>

```
POST '/questions'
- Sends a post request in order to add a new question
- Request Body: 
{
    "question":  "some new question :)",
    "answer":  "hahahahah",
    "difficulty": 1,
    "category": 3
}
- Returns: Does not return any new data
{
    "success": true
}
```

<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125362256-44cf9400-e377-11eb-9b49-a6405111ab30.png">
</p>
<p align = "center">
Fig.3 - POST questions with a question, answer, difficulty and category frontend expected view
</p>

```
POST '/questions'
- Sends a post request in order to search for a specific question by search term 
- Request Body: 
{
    "searchTerm": "clay"
}
- Returns: any array of questions, a number of totalQuestions that met the search term and the current category string 
{
    "currentCategory": null,
    "questions": [
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        }
    ],
    "success": true,
    "totalQuestions": 1
}
```

<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125362079-f3bfa000-e376-11eb-9e5c-e3c98ffe2b08.png">
</p>
<p align = "center">
Fig.4 - POST questions with a searchTerm frontend expected view
</p>

```
POST '/quizzes'
- Sends a post request in order to get the next question 
- Request Body: 
{'previous_questions':  an array of question id's such as [1, 4, 20, 15]
'quiz_category': a string of the current category }
{
    "previous_questions": [19],
    "quiz_category": {"type":"Art", "id":"2"}

}
- Returns: a single new question object 
{
    "question": {
        "answer": "Escher",
        "category": 2,
        "difficulty": 1,
        "id": 16,
        "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    "success": true
}
```

<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125361719-6419f180-e376-11eb-8d5d-7b61bfc84ad0.png">
</p>
<p align = "center">
Fig.5 - POST quizzes frontend expected view
</p>

```
DELETE '/questions/${id}'
- Deletes a specified question using the id of the question
- Request Arguments: id - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code optinally returens an id of the deleted question.
{
    "id": 14,
    "success": true
}
```
<p align = "center">

<img src = "https://user-images.githubusercontent.com/72150188/125361203-ac84df80-e375-11eb-95cf-5face81619eb.png">
<img src = "https://user-images.githubusercontent.com/72150188/125361290-c9b9ae00-e375-11eb-9bc4-131c2dfb6ae6.png">
</p>
<p align = "center">
Fig.6 - DELETE questions based on id frontend expected view
</p>
