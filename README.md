# Trivia - Full Stack API Project

July, 13 2021 

## Introduction

The objective of this project is to learn how to structure plan, implement, and test an API. Udacity provides an initial prototype design. Completing this trivia app will help acquire the essential skills for enabling applications to communicate with other applications.

## Getting Started

Follow instruction in \[./backend\](https://github.com/alanoudalbattah/Trivia/tree/master/Trivia\_API/backend/README.md) and \[./frontend\](https://github.com/alanoudalbattah/Trivia/tree/master/Trivia\_API/frontend/README.md)

## Endpoints

\`\`\`

`GET '/categories'`

`GET `'`/`questions'

GET '/categories/<int:category\_id\>/questions'

POST '/questions'

POST '/quizzes'

`DELETE `'/questions/<int:question\_id\>'

``

\`\`\`  

## Examples of Endpoints

\`\`\`

GET '/categories'  
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category  
- Request Arguments: None  
- Returns: An object with a single key, categories, that contains a object of id: category\_string key:value pairs.   
{'1' : "Science",  
'2' : "Art",  
'3' : "Geography",  
'4' : "History",  
'5' : "Entertainment",  
'6' : "Sports"}

`\`\`\`  
`

## Screenshots

!\[image\](https://user-images.githubusercontent.com/72150188/125356000-55c7d780-e36e-11eb-9209-502dfb7d41ba.png)  

!\[image\](https://user-images.githubusercontent.com/72150188/125356302-b1926080-e36e-11eb-821e-1cb8bf1e2b04.png)  

!\[image\](https://user-images.githubusercontent.com/72150188/125356200-8e67b100-e36e-11eb-9a9e-81ea5ac8571d.png)  

``

!\[image\](https://user-images.githubusercontent.com/72150188/125356097-7132e280-e36e-11eb-8741-cd3b2fd7b86c.png)  
