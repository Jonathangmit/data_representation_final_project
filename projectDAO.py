import mysql.connector
# DAO is data access object
class ProjectDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tutu",
            database="datarepresentation"
        )
        #print("connection made")

    def create(self, larder):
        cursor = self.db.cursor()
        sql="insert into larder (VIN,chateau,notes,price) values (%s,%s,%s,%s)"
        values = [larder['VIN'],larder['chateau'],larder['notes'],larder['price']]
        cursor.execute(sql,values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from larder"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray =[]
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray
    
    def findById(self,VIN):
        cursor =self.db.cursor()
        sql = 'select * from larder where VIN = %s'
        values =[VIN]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, larder):
        cursor =self.db.cursor()
        sql = "update larder set chateau = %s, notes =%s, price =%s where VIN =%s"
        values =[
            larder['chateau'],
            larder['notes'],
            larder['price'],
            larder['VIN']
        ]
        cursor.execute(sql,values)
        self.db.commit()

        return larder

    def delete(self,VIN):
        cursor = self.db.cursor()
        sql = 'delete from larder where VIN = %s'
        values =[VIN]
        cursor.execute(sql,values)
        return {}
        

    def convertToDict(self,result):
        colnames =['VIN','chateau','notes','price']
        book ={}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                book[colName] = value
        return book
#************
#second sheet
    def create2(self, pantry):
        cursor = self.db.cursor()
        sql="insert into pantry (fromage,farm,notes,price) values (%s,%s,%s,%s)"
        values = [pantry['fromage'],pantry['farm'],pantry['notes'],pantry['price']]
        cursor.execute(sql,values)
        self.db.commit()
        return cursor.lastrowid

    def getAll2(self):
        cursor = self.db.cursor()
        sql = "select * from pantry"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray2 =[]
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict2(result)
            returnArray2.append(resultAsDict)
        return returnArray2
    
    def findById2(self,fromage):
        cursor =self.db.cursor()
        sql = 'select * from pantry where fromage = %s'
        values =[fromage]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict2(result)

    def update2(self, pantry):
        cursor =self.db.cursor()
        sql = "update pantry set farm = %s, notes =%s, price =%s where fromage =%s"
        values =[
            pantry['farm'],
            pantry['notes'],
            pantry['price'],
            pantry['fromage']
        ]
        cursor.execute(sql,values)
        self.db.commit()

        return pantry

    def delete2(self,fromage):
        cursor = self.db.cursor()
        sql = 'delete from pantry where fromage = %s'
        values =[fromage]
        cursor.execute(sql,values)
        return {}
        

    def convertToDict2(self,result):
        colnames =['fromage','farm','notes','price']
        book ={}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                book[colName] = value
        return book



#************
projectDAO = ProjectDAO()
