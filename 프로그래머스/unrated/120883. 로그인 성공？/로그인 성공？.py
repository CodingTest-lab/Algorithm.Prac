def solution(id_pw, db):
    db_keys = [key for key,value in db]
    db_values = [value for key,value in db]
    
    for i in range (len(db)):
        if id_pw[0] == db_keys[i] and id_pw[1] == db_values[i]:
            return 'login'
        elif id_pw[0] == db_keys[i] and id_pw[1] != db_values[i]:
            return 'wrong pw'
        elif id_pw[0] != db_keys[i]:
            continue
    return 'fail'