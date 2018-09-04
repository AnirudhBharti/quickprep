from django.db import  connection
import MySQLdb as mySql

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
                dict(zip([col[0] for col in desc], row)) 
                for row in cursor.fetchall()
           ]

def gettutorialmenu():
    cursor=connection.cursor()
    query = ("SELECT tm.tutorialmenuid,tm.tutorialmenuname,tm.tutorialmenudesc,tm.tutorialmenuroute, "
            "tt.tutorialtopicsmenuname,tt.tutorialtopicsmenudescription,tt.tutorialtopicroute,tt.tutorialmenuid as 'tutorialmenuidfk' "
             "FROM Tutorialmenu as tm "
             "left join Tutorialtopicsmenu as tt on tm.tutorialmenuid=tt.tutorialmenuid"
            )
    cursor.execute(query)
    rows = dictfetchall(cursor)
    #print(rows)
    return rows