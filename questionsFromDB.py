from sqlalchemy import (create_engine)


def question_texts(tablename):
    questions = []
    engine = create_engine('sqlite:///questions.db')
    connection = engine.connect()
    result = connection.execute("SELECT text FROM %s" % (tablename))
    for row in result:
        questions.append(row["text"])
    connection.close()
    return questions
