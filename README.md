# Lib Chat
CMPE-252 (Final Project Chatbot)

This chatbot is a conversational AI built using the open-source Rasa framework. Its purpose is to provide help as a Library Assistant.

## Creator
* Nemil Nilesh Panchamia
  * nemilnilesh.panchamia@sjsu.edu
  * 016145272
  * MS AI

## Problem Statement

There are times when people need access to library resources during after hours. We cannot expect to have librarians and assistants working day and night.

#### Solution: Created an AI bot which answers basic questions about the library and it's features.

## Requirements

- Rasa 3.0 or higher
- Python 3.7 or higher (Here using 3.8)
- Using Postgres for storing the required data from the user

## APIs used 

- Harvard Library API
- ARXIV Research Papers API

## Installation

1. Clone this repository

`git clone https://github.com/Nemil28/Rasa_Project.git`


2. Install the required dependencies

`pip install -r requirements.txt`


3. Train the chatbot's natural language processing model by running the following command

`rasa train`


4. Run the custom actions file which is used to run the APIs created for this particular chatbot

`rasa run actions`


5. Start the chatbot server by running the following command

`rasa run`


{To run the chatbot in shell run the following command}

`rasa shell`


## File Structure

- The `data` directory contains the training data for the chatbot's natural language processing model, including training examples and NLU annotations.
- The `models` directory contains the trained model files generated during the training process.
- The `actions` directory contains the code for the custom actions that the chatbot can perform.
- The `config.yml` file contains the configuration for the chatbot, including the NLU and Core model settings.

## Dialogue Flow

### One example for the dialogue flow is shown below

Your input ->  Hello                                                                                       
Hello! What can I help you with?

Your input ->  Are you open today?                                                                         
Yes we are open today.

Your input ->  Do you have study rooms available?                                                          
Yes we do have study and presentation rooms available for booking.

Your input ->  For how long can I book a study room?                                                       
The rooms are available from 9am to 9pm and the maximum time you can book it for is 2 hours.

Your input ->  How do I book the study room?                                                               
You can book the room online or you can call the library at 1-800-MLK to make a booking.

Your input ->  What is your location?                                                                      
The library is located at 150 E San Fernando St, San Jose, CA, 95112

Your input ->  Do you charge any fees?                                                                     
The library can be used for free but you need to purchase a $1.99/month membership to borrow the books from the library.

Your input ->  Do you accept credit cards?                                                                 
Unfortunately we are only accepting cash at this moment and we are sorry for the inconvenience caused.

Your input ->  Do you have research papers?                                                                
We have papers from the arxiv archive library. What subject would you like to search for?

Your input ->  Ai                                                                                          
Here are some of the papers for the following subject.. ['Supporting AI/ML Security Workers through an Adversarial Techniques,Tools, and Common Knowledge (AI/ML ATT&CK) Framework', '"Weak AI" is Likely to Never Become "Strong AI", So What is its GreatestValue for us?']

Your input ->  What kind of books are there?                                                               
We have over 20,000 books in the collection. Do you want a list of departments available?

Your input ->  no                                                                                          
Okay. Let me know if I can do something else.

### Another example of a dialogue flow is shown below.

Your input ->  Do you have reserach papers?                                                                
We have papers from the arxiv archive library. What subject would you like to search for?

Your input ->  physics                                                                                     
Here are some of the papers for the following subject.. ['Is Physics Sick? [In Praise of Classical Physics]', 'Modern Mathematical Physics: what it should be?']

Your input ->  What kind of books you have?                                                                
We have over 20,000 books in the collection. Do you want a list of departments available?

Your input ->  yes                                                                                         
Here is a list of some of the genres available.. {'': 0, 'Americas, Europe, and Oceania Division, Widener Library': 0, 'Fine Arts Library': 0, 'Historical and Special Collections, Harvard Law Library': 0, 'Classics Department, FAS': 0, 'Countway Library': 0, 'Middle Eastern Division, Widener Library ': 0, 'Houghton Library': 0, 'Gutman Library': 0, 'Ernst Mayr Library, Museum of Comparative Zoology': 0, 'Artemas Ward House': 0, 'Schlesinger Library': 0, 'Loeb Music Library': 0, 'Harvard Map Collection, Pusey Library': 0, 'Middle Eastern Division, Widener Library': 0}

Your input ->  Can I checkout books?                                                                       
Books may be checked out at the library circulation desk for a maximum of 25 days.

Your input ->  How many books can I check out?                                                             
You can checkout at most 3 books at a time.

Your input ->  How do I make a payment for the book?                                                       
Unfortunately we are only accepting cash at this moment and we are sorry for the inconvenience caused.
                                                                              

## For obtaining the graph for dialogue flow, the code is given below

`rasa visualize`
