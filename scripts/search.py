from sqlite3 import *
from random import randint, shuffle
from re import findall, I, M
from datetime import datetime

search_dbs = ['n', 'adj', 'adv', 'v']

def get_word(search_word):
    global search_dbs
    db = connect("./dict.db")
    cur = db.cursor()
    words = []; temp = []

    def return_pos(iter_cnt):
        if iter_cnt == 0: return "noun"
        elif iter_cnt == 1: return "adjective"
        elif iter_cnt == 2: return "adverb"
        elif iter_cnt == 3: return "verb"

    def word_dict(word, pos):
        syn_search = cur.execute("SELECT * FROM syn WHERE Word=?", [word[0]]).fetchall()
        syn = []
        for i in range(len(syn_search)):
            syn.append(syn_search[i][3])

        if pos == "verb" or pos == "adverb":
            return {
                "word": word[0],
                "pos": pos,
                "definition": word[3],
                "sentence": word[4],
                "synonyms": syn,
            }
        elif pos == "noun":
            return {
                "word": word[0],
                "pos": pos,
                "definition": word[3],
                "synonyms": syn,
            }
        elif pos == "adjective":
            return {
                "word": word[0],
                "pos": pos,
                "definition": word[3],
                "sentence": word[7],
                "synonyms": syn,
            }

    for i in range(len(search_dbs)):
        pos = return_pos(i)
        search = cur.execute(f"SELECT * FROM {search_dbs[i]} WHERE Word=?", [search_word]).fetchall()
        temp.append(search)
        if len(temp[i]) == 0: pass
        else: 
            for l in range(len(temp[i])):
                words.append(word_dict(temp[i][l], pos))

    return words

def check_none(pos, word):
    n_check_things = ["pos","definition", "synonyms"]

    non_n_check_things = ["pos", "definition", "sentence", "synonyms"]
    if pos == "noun":
        for i in range(len(n_check_things)):
            if word[n_check_things[i]] == "":
                word[n_check_things[i]] = "None (Blank from database)"
    else:
        for i in range(len(non_n_check_things)):
            if word[non_n_check_things[i]] == "":
                word[non_n_check_things[i]] = "None (Blank from database)"
    
    return word

def wotd_question():
    def get_opt(opt_cnt, db_search_query, ans):
        ans_list = []
        ans_list.append(ans)
        for _ in range(opt_cnt):
            temp = cur.execute(f"SELECT Word FROM {db_search_query};").fetchall()
            temp = temp[randint(0, len(temp) - 1)][0]
            if temp not in ans_list:
                ans_list.append(temp)

        return ans_list

    db = connect("./dict.db")
    cur = db.cursor()
    global search_dbs
    q_type = search_dbs[randint(0, (len(search_dbs) - 1))]

    q = {}

    all_items = cur.execute(f"SELECT * FROM {q_type};").fetchall()
    q_word = all_items[randint(0, (len(all_items) - 1))]
    ans_list = []

    if q_type == "syn":
        ans_options = findall(r"[^;|\s]+", q_word[len(q_word) - 1], I | M)

        ans = ans_options[randint(0, len(ans_options) - 1)]
        print(ans)

        ans_list = get_opt(3, q_type, ans)
        shuffle(ans_list)
        print(ans_list)
        q.update({"question": f'What is one of the synonyms for the word or phrase "{q_word[0]}"'})

        for i in range(len(ans_list)):
            ans_char = chr(ord("A") + i)
            q.update({ans_char: ans_list[i]})
        print(q)
    else:
        ans = q_word[3]

        print(ans)

        ans_list = get_opt(3, q_type, ans)

        shuffle(ans_list)
        q.update({"question": f'What is one of the meanings for the word or phrase "{q_word[0]}"?'})

        for i in range(len(ans_list)):
            ans_char = chr(ord("A") + i)
            q.update({ans_char: ans_list[i]})

        print(q)
    
    print(ans_list.index(ans))
    date = datetime.now().strftime("%Y-%m-%d")
    ans = chr(ord('A') + ans_list.index(ans))
    try:
        cur.execute("INSERT INTO wotd (date, a, b, c, d, question, answer) VALUES (?, ?, ?, ?, ?, ?, ?);", [date, q['A'], q['B'], q['C'], q['D'], q['question'], ans])
        db.commit()
    except IntegrityError:
        pass        
    print([date, q['A'], q['B'], q['C'], q['D'], q['question'], ans])
