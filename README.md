# CS50 Final Project (Dict aka Dictionary)

### YOUTUBE LINK: https://youtu.be/7Uj0fdoGY1A

#### Simple Overview

This is a simple, easy-to-use english dictionary. Based off of [Wordnet](https://wordnet.princeton.edu/), and the database of words were copied from [here](https://www.kaggle.com/datasets/dfydata/wordnet-dictionary-thesaurus-files-in-csv-format). This project was made using [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/en/3.0.x/), and [SQLite](https://www.sqlite.org/index.html). You can specify the colors of words with multiple meanings for a better viewing experience. There is also a "Word of the Day" for you to test your vocabulary skills.

#### `app.py`

So first for app.py, it simply defines the routes for each possible action, and the only few functions that are defined in it is the "merge" function, which just generates the html alongside with the colors (using the span tag)

#### `helpers.py`

I got this idea from the Week Nine pset: Finance, where CS50 included a "helpers.py" python program that includes some of the core functions needed for Finance, and inside, the specified_color function is just used to de-clutter app.py's merge function, as they are essentially the same code, and the wotd_gen is a part of wotd, and its responsibility is to check whether or not today's word of the day has been generated or not, so it makes sure so remove the previous answer from yesterday, and if someone has already generated the question, then it would just SELECT it from the database.

#### `search.py`

It, as the name implies, does all of the searching for anything word related. So the get_word function is from my other github repo (Projects/dict/, and that's where this also originated from) and I just made it a function, it mostly just generates a word_dict, which is a dictionary for the words searched. check_none is a function to check whether or not some of the data from the database has nothing, and adds a helpful text saying that it doesn't exist. wotd_question is actually what the helpers.py's wotd_gen calls for the Word of the Day generation, now I could've made it even more concise, as the meaning questions generate quite similiar to the synonym questions, so that's a place where i could've improved on.

#### Other notes on the python scripts

You might've noticed that I used the chr() and the ord() function a lot in the Word of the Day creation, it's because I have the options A, B, C, and D, and they could benefit from loops as they are just their ASCII codes plus a few (for example D is A + 3), but in C you could just do char addition (aka char d = "A" + 3;) but in python it's harder as python doesn't recognize the integer addition onto a string, so the ord function essentially makes the string/char a number then I could add 1/2/3/0 to it, then convert it back using the chr() function.

#### JS (`search.js`/`index.js`)

For the two JS files, the index.js just makes the + button next to the color specification work, and so it just adds a new input tag into the form. The search.js file on the other hand, uses AJAX to fetch the data from the server (/autocomplete) and the flask server will return a list of the top 20 results (alphabetically sorted), and change the autocomplete ul.

#### `dict.db`

If you open the db file, you'll see in the schema:

    CREATE TABLE IF NOT EXISTS "adj"(
    "Word" TEXT, "Count" TEXT, "Senses" TEXT, "Definition" TEXT,
    "Example 1" TEXT, "Example 2" TEXT, "Example 3" TEXT, "Example 4" TEXT);
    CREATE TABLE IF NOT EXISTS "n"(
    "Word" TEXT, "Count" TEXT, "POS" TEXT, "Definition" TEXT);
    CREATE TABLE IF NOT EXISTS "syn"(
    "Word" TEXT, "Count" TEXT, "POS" TEXT, "Synonyms" TEXT);
    CREATE TABLE IF NOT EXISTS "v"(
    "Word" TEXT, "Count" TEXT, "Sense" TEXT, "Definition" TEXT,
    "Example 1" TEXT, "Example 2" TEXT);
    CREATE TABLE IF NOT EXISTS "adv"(
    "Word" TEXT, "Count" TEXT, "Senses" TEXT, "Definition" TEXT,
    "Example" TEXT);
    CREATE TABLE wotd (date TEXT NOT NULL, a TEXT NOT NULL, b TEXT NOT NULL, c TEXT NOT NULL, d TEXT NOT NULL, question TEXT NOT NULL, answer TEXT NOT NULL, a_ans INTEGER DEFAULT 0 NOT NULL, b_ans INTEGER DEFAULT 0 NOT NULL, c_ans INTEGER DEFAULT 0 NOT NULL, d_ans INTEGER DEFAULT 0 NOT NULL, total_ans INTEGER DEFAULT 0 NOT NULL);
    CREATE UNIQUE INDEX date on wotd (date);

And so all of this is just pulled off of the link in the first section, and everything except for the nouns (n) have examples in them, now at first I wanted to use a charting library to record the users' responses on the word of the day, but chart.js (charting library I wanted to use) and flask didn't go well together (maybe more like flask and npm don't go well together). And since I didn't want to use a script tag, I decided to scrap that idea.

#### CSS

You might've noticed that I didn't use any style libraries like Tailwind or Boostrap. That's because when I first started this, I didn't use Bootstrap, so I just used good-old CSS to create the style of this website.

#### Other Things About This Project

I didn't want to use this Project as my CS50 Final Project in the first place, as I wanted to do a "Control Panel" for my raspberry pi (which I will be hosting this site on), but later into it, I found out that that project would've been too easy with a few libraries and frameworks, so I scrapped that idea and went with this instead.
