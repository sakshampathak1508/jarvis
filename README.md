This is a Very simple Jarvis or you can say Desktop assistant . Coded using pure Python.
NO ML model or AI is used in this project just pure python is used for the very spesific and 
daily to daily tasks to get done using this Desktop assistant or Jarvis.

In order to use this assistant you need 

:-
1. Clone the repository
2. Activate the virtual environment using the command :-  env\Scripts\activate
3. Install the required file as describes in the requirements.txt by the command :-  pip install requirements.txt

The functionalities this awesome jarvis provides are as follows :

After going through the setup and having all requirements fullfilled as in the Readme.md file 

you are ready to use this awesome power packed Desktop assistant aka Jarvis 
(No ML Model or AI is used just the magic of pure python)

user info for additional functianlity of whatsapp messaging and sending emails

1:- in line 17 of jarvis.py you need to provide the name and phone number of contacts you want to communicate in whatsapp just like a phone book
    using this jarvis described in point 9 below. 
2:- in line 59 and 60 you need to provide the email id and password of your gmail account to use the sending email feature in point 10 below


1. Activation:
    say "hi Jarvis" or "Hey jarvis" to activate the assisant just like "ok google" or "Hey siri"

2. Getting time:
    simply ask for the time like "hey what's the time right now?" or "tell me the time!"

3. Wikipedia info:
    say in your message with a keyword "According to wikipedia" + {{Your query}}
    to get brief info about your query accordin to wikipedia.

4. search youtube videos:
    say in your message with a keyword "Search youtube and wait" 
    Jarvis: - "What you want to search"
    say your query to get youtube search results of {{Your query}}

5. Play youtube videos as per latest to the query 
    say in your message with a keyword "Play youtube and wait" 
    Jarvis: - "What you want to play"
    say your query to get play youtube video in browser {{Your query}} asper the latest video added 

6. open any website:
    just simply say "Open"+{{Website name}}
    to open the website in your default browser

7. Search the web:
    simply say "Search" + {{your query}}
    to get the google search results of your query in your default browser

8. send email:
    simply say "send email":
        And say "The mail body you want to mail":
        then it manually asks to input the email id of the user 
        and boom the email has been sent

    Note:- its required for that the sender has a gmail account 

9. send whatsapp messages:
    prerequisite:
        Thers is a feature of A phone book inside the code That will ask you to type the name 
        and phone number of your contacts.
    say "send message" (limited to whatsapp)
    and say the name of the reciver 
    and the say what message you want to send via whatsapp
    and it will be done in a span of maximam 30 seconds
    
10. Quit or exit from jarvis help:
    simply say "Quit jarvis" to turn off the jarvis and exit from the code

