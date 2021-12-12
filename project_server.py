from flask import Flask,url_for,request,redirect,abort,jsonify
from projectDAO import projectDAO

app = Flask(__name__, static_url_path='',static_folder='staticpages')


@app.route('/')
def index():
    return ("hello")

#get all
@app.route('/books')
def getAll():
    return jsonify(projectDAO.getAll())

#find by Id
@app.route('/books/<int:VIN>')
def findById(VIN):
    return jsonify(projectDAO.findById(VIN))

# create
@app.route('/books',methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    book={ 
        "VIN": request.json['VIN'],
        "chateau":request.json['chateau'],
        "notes":request.json['notes'],
        "price":request.json['price']
    }
    return jsonify(projectDAO.create(book))

# update
@app.route('/books/<int:VIN>',methods =['PUT'])
def update(VIN):
    foundWine=projectDAO.findById(VIN)
    print(foundWine)
    if foundWine == 0:
        return jsonify({}),404
    currentWine = foundWine
    if 'chateau' in request.json:
        currentWine['chateau'] = request.json['chateau']
    if 'notes' in request.json:
        currentWine['notes'] = request.json['notes']  
    if 'price' in request.json:
        currentWine['price'] = request.json['price'] 
    projectDAO.update(currentWine)
    return jsonify(currentWine)

# delete
@app.route('/books/<int:VIN>',methods=['DELETE'])
def delete(VIN):
    projectDAO.delete(VIN)
    return jsonify({"done":True})

###### new zone

@app.route('/food')
def getAll2():
    return jsonify(projectDAO.getAll2())

#find by Id
@app.route('/food/<int:fromage>')
def findById2(fromage):
    return jsonify(projectDAO.findById2(fromage))

# create
@app.route('/food',methods=['POST'])
def create2():
    
    if not request.json:
        abort(400)
    book={ 
        "fromage":request.json['fromage'],
        "farm":request.json['farm'],
        "notes":request.json['notes'],
        "price":request.json['price']
    }
    return jsonify(projectDAO.create2(book))

# update
@app.route('/food/<int:fromage>',methods =['PUT'])
def update2(fromage):
    foundcheese=projectDAO.findById2(fromage)
    print(foundcheese)
    if foundcheese == 0:
        return jsonify({}),404
    currentcheese = foundcheese
    if 'farm' in request.json:
        currentcheese['farm'] = request.json['farm']
    if 'notes' in request.json:
        currentcheese['notes'] = request.json['notes']  
    if 'price' in request.json:
        currentcheese['price'] = request.json['price'] 
    projectDAO.update(currentcheese)
    return jsonify(currentcheese)
# delete
@app.route('/food/<int:fromage>',methods=['DELETE'])
def delete2(fromage):
    projectDAO.delete2(fromage)
    return jsonify({"done":True})

###### end new zone

if __name__ == "__main__":
    app.run(debug=True)

