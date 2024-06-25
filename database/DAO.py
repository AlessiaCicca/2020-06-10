from database.DB_connect import DBConnect
from model.attore import Attore
from model.connessione import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct mg.genre as genere 
from movies_genres mg 
order by  mg.genre"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["genere"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a.*  
from actors a ,roles r , movies_genres mg 
where mg.genre =%s and mg.movie_id =r.movie_id 
and r.actor_id =a.id  """

        cursor.execute(query,(genere,))

        for row in cursor:
            result.append(Attore(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessioni(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.a1 as v1,t2.a2 as v2,count(distinct t1.m1) as peso
from(select distinct r.actor_id as a1, r.movie_id as m1
from movies_genres mg , roles r 
where mg.movie_id =r.movie_id 
and mg.genre  =%s) as t1,
(select distinct r.actor_id as a2, r.movie_id as m2
from movies_genres mg , roles r 
where mg.movie_id =r.movie_id 
and mg.genre  =%s) as t2
where t1.a1<t2.a2 and t1.m1=t2.m2
group by t1.a1,t2.a2"""

        cursor.execute(query,(genere,genere,))

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result

