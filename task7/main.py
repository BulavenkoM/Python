import random

answers = ["Так", "Ні", "Можливо"]

def charivna_kulka(question: str):
    global answers
    idx = random.randint(0,2)
    if not question:
        return None
    else:
        return answers[idx]
        
def configure_charivna_kulka(new_answers: list):
    global answers
    answers.extend(new_answers)

def update_procent(answer,procent):
    global answers
    count_add = 1
    actual_procent = 0
    list_answers = []
    for item in answers:
        if answer != item:
            list_answers.append(item)
    idx_add = 0
    while actual_procent != procent:
        if actual_procent > procent:
            if idx_add == len(list_answers):
                idx_add = 0
            answers.append(list_answers[idx_add])
            idx_add+=1
        else:
            answers.append(answer)
            count_add += 1
        count = len(answers)
        answer_procent = 100/count
        actual_procent = answer_procent*count_add
    return answers



