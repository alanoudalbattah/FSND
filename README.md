# Trivia - Full Stack API Project

The objective of this project is to learn how to structure plan, implement, and test an API. Udacity provides an initial prototype design. Completing this trivia app will help acquire the essential skills for enabling applications to communicate with other applications.

## Getting Started

Follow instruction in [./backend](https://github.com/alanoudalbattah/Trivia/tree/master/Trivia\_API/backend/README.md) and [./frontend](https://github.com/alanoudalbattah/Trivia/tree/master/Trivia\_API/frontend/README.md)

## Endpoints

```

GET '/categories'

GET '/questions'

GET '/categories/<int:category\_id\>/questions'

POST '/questions'

POST '/quizzes'

DELETE '/questions/<int:question\_id\>'

```  

## Examples of Endpoints

```

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs. 
{
    'categories': { '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports" }
}
```

```

GET '/questions?page=${integer}'
- Fetches a paginated set of questions, a total number of questions, all categories and current category string. 
- Request Arguments: page - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string
{
    'questions': [
        {
            'id': 1,
            'question': 'This is a question',
            'answer': 'This is an answer', 
            'difficulty': 5,
            'category': 2
        },
    ],
    'totalQuestions': 100,
    'categories': { '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports" },
    'currentCategory': None
}

```
<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125356000-55c7d780-e36e-11eb-9209-502dfb7d41ba.png">
</p>
<p align = "center">
Fig.1 - GET categories and GET questions frontend expected result
</p>

```

GET '/categories/${id}/questions'
- Fetches questions for a cateogry specified by id request argument 
- Request Arguments: id - integer
- Returns: An object with questions for the specified category, total questions, and current category string 
{
    'questions': [
        {
            'id': 1,
            'question': 'This is a question',
            'answer': 'This is an answer', 
            'difficulty': 5,
            'category': 4
        },
    ],
    'totalQuestions': 100,
    'currentCategory': None
}

```
<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125356302-b1926080-e36e-11eb-821e-1cb8bf1e2b04.png">
</p>
<p align = "center">
Fig.1 - GET questions based on category frontend expected result
</p>

```
POST '/questions'
- Sends a post request in order to add a new question
- Request Body: 
{
    'question':  'Heres a new question string',
    'answer':  'Heres a new answer string',
    'difficulty': 1,
    'category': 3,
}
- Returns: Does not return any new data
```

<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125356200-8e67b100-e36e-11eb-9a9e-81ea5ac8571d.png">
</p>
<p align = "center">
Fig.1 - 4K Mountains Wallpaper
</p>

```
POST '/questions'
- Sends a post request in order to search for a specific question by search term 
- Request Body: 
{
    'searchTerm': 'this is the term the user is looking for'
}
- Returns: any array of questions, a number of totalQuestions that met the search term and the current category string 
{
    'questions': [
        {
            'id': 1,
            'question': 'This is a question',
            'answer': 'This is an answer', 
            'difficulty': 5,
            'category': 5
        },
    ],
    'totalQuestions': 100,
    'currentCategory': 'Entertainment'
}
```

<p align = "center">
<img src = "">
</p>
<p align = "center">
Fig.1 - some caption 
</p>

```
POST '/quizzes'
- Sends a post request in order to get the next question 
- Request Body: 
{'previous_questions':  an array of question id's such as [1, 4, 20, 15]
'quiz_category': a string of the current category }
- Returns: a single new question object 
{
    'question': {
        'id': 1,
        'question': 'This is a question',
        'answer': 'This is an answer', 
        'difficulty': 5,
        'category': 4
    }
}
```

<p align = "center">
<img src = "https://user-images.githubusercontent.com/72150188/125356097-7132e280-e36e-11eb-8741-cd3b2fd7b86c.png">
</p>
<p align = "center">
Fig.1 - 4K Mountains Wallpaper
</p>

```
DELETE '/questions/${id}'
- Deletes a specified question using the id of the question
- Request Arguments: id - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code.
```
<p align = "center">
<img src = "">
</p>
<p align = "center">
Fig.1 - some caption 
</p>
