from questionsFromDB import question_texts

GENDER = ("нет ответа", "мальчик", "девочка")
HEALTH = ("нет ответа", "здоров", "выздоровел", "ослаблен", "болен")
EDUCATION = ("нет ответа", "в семье", "в дет/с и дома",
             "в круглосут.яслях", "в детском доме")
PEOPLE = ("нет ответа", "мать", "отец", "бабушка", "родств.", "няня")
WHOEDUS = ("нет ответа", "мать", "отец", "бабушка", "родств.", "няня")
BEST = ("нет ответа", "послушание", "общительность", "любопытство")
BIRTH = ("нет ответа", "не было", "у ребенка", "у матери", "у обоих")
SEIZURES = ("нет ответа", "да", "нет")
LANGUAGE = ("нет ответа", "только русский", "русский и другой")
MOOD = ("нет ответа", "бодрое", "спокойное", "раздраженное", "подавленное")
FINANCE = ("нет ответа", "хорошее", "среднее", "плохое", "оч. плохое")
P_EDUCATION = ("нет ответа", "неп. среднее", "среднее",
               "ср. специальное", "неп. высшее", "высшее")
DATE_VALUES = ("d_birth", "m_birth", "y_birth", "d_fill", "m_fill", "y_fill")
CDI_QUESTIONS = question_texts("cdi_questions")
KID_QUESTIONS = question_texts("kid_questions")
ANSWERS = ("(0) нет ответа", "(1) делает давно",
           "(2) делает недавно", "(3) пока не делает")
TEXT_KEYES = ("name", "address", "phone")
KEYS = ("name", "gender", "d_birth", "m_birth", "y_birth", "d_fill", "m_fill", "y_fill",
        "address", "phone", "numberofkids", "weekofbirth", "m_age", "f_age", "g_age",
        "m_edu", "f_edu", "g_edu", "whofills", "health", "where_edu", "who_edu",
        "what_best", "birth_complications", "seizures", "language", "mood", "finance")
QUESTLENGTH = {"KID": 252, "RCDI": 216}
KEYSCHILD = ("name", "birthday")
DATETIMED = ("birthday", "day_filled")
AllKEYS = ('id', 'name', 'birthday', 'quiz_id', 'child_id', 'gender', 'day_filled', 'address', 'phone', 'numberofkids',
           'weekofbirth', 'm_age', 'f_age', 'g_age', 'm_edu', 'f_edu', 'g_edu', 'whofills', 'health', 'where_edu',
           'who_edu', 'what_best', 'birth_complications', 'seizures', 'language', 'mood', 'finance', 'testtype', 'test')
