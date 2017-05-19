from datetime import datetime
from sqlalchemy import (MetaData, Table, Column, Integer, String, DateTime,
                        ForeignKey, create_engine, select, update, and_)


class DbWork():
    def __init__(self):
        self.metadata = MetaData()
        self.engine = create_engine("sqlite:///children.db")
        self.connection = self.engine.connect()
        self.definetables()

    def definetables(self):
        self.children = Table('children', self.metadata,
                              Column("id", Integer(), primary_key=True),
                              Column("name", String(60)),
                              Column("birthday", DateTime()))

        self.quizzes = Table('quizzes', self.metadata,
                             Column("quiz_id", Integer(), primary_key=True),
                             Column("child_id", ForeignKey("children.id")),
                             Column("gender", Integer()),
                             Column("day_filled", DateTime()),
                             Column("address", String(100)),
                             Column("phone", String(20)),
                             Column("numberofkids", Integer()),
                             Column('weekofbirth', Integer()),
                             Column("m_age", Integer()),
                             Column("f_age", Integer()),
                             Column("g_age", Integer()),
                             Column("m_edu", Integer()),
                             Column("f_edu", Integer()),
                             Column("g_edu", Integer()),
                             Column("whofills", Integer()),
                             Column("health", Integer()),
                             Column("where_edu", Integer()),
                             Column("who_edu", Integer()),
                             Column("what_best", Integer()),
                             Column("birth_complications", Integer()),
                             Column("seizures", Integer()),
                             Column("language", Integer()),
                             Column("mood", Integer()),
                             Column("finance", Integer()),
                             Column("testtype", Integer()),
                             Column("test", String(252)))

    def kidslist(self, name):
        s = select([self.children]).where(
            self.children.c.name.like(name + "%",)).order_by("name")

        rp = self.connection.execute(s)
        return rp.fetchall()
#

    def insert_child(self, child_dict):
        result = self.connection.execute(self.children.insert(), child_dict)
        return result.inserted_primary_key

    def insert_quiz(self, quiz_dict):

        self.connection.execute(self.quizzes.insert(), quiz_dict)

    def testlist(self, id, ttype):
        s = select([self.quizzes.c.quiz_id, self.quizzes.c.day_filled])
        s = s.where(
            and_(self.quizzes.c.child_id == id,
                 self.quizzes.c.testtype == ttype)).order_by("day_filled")

#         print(str(s))
        return self.connection.execute(s).fetchall()

    def namebyid(self, c_id):
        s = select([self.children.c.name]).where(self.children.c.id == c_id)
        return str(self.connection.execute(s).first()[0])

    def load_name_n_quiz(self, id):
        s = select([self.children, self.quizzes])
        s_join = s.select_from(self.children.join(self.quizzes)).where(
            self.quizzes.c.quiz_id == id)
        rp = self.connection.execute(s_join)
        results = rp.first()
#         print(results.keys())
        return results

    def load_name_only(self, id):
        s = select([self.children])
        s = s.where(self.children.c.id == id)
        rp = self.connection.execute(s)
        results = rp.first()
#         print(results.keys())
        return results

    def update_child(self, dict_w, c_id):
        u = update(self.children).where(self.children.c.id == c_id)
        self.connection.execute(u, dict_w)

#         print(str(u))
    def update_quiz(self, dict_w, id):
        u = update(self.quizzes).where(self.quizzes.c.quiz_id == id)
        self.connection.execute(u, dict_w)


dbase = DbWork()

if __name__ == '__main__':
    db = DbWork()
#     db.load_name_n_quiz(1)


#     db.metadata.create_all(db.engine)
#     ins=db.children.update().where(db.children.c.id==1).values(
#         name="Пушкин Олег",
#         birthday=datetime.now()
#         )
#     print(str(ins))
#     print(ins.compile().params)
#     result=db.connection.execute("SELECT id,name,birthday FROM children WHERE name LIKE ? ORDER BY name",("Пу"+"%",))
#     rp=result.fetchall()
#     print(rp)
#     for re in result:
#         print(result)
#
