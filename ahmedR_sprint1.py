#Raahima Ahmed
#SDID 1892523
from sql import create_connection 
from sql import execute_query
from sql import execute_read_query
import flask 
from flask import jsonify
from flask import request, make_response
from sql import create_connection, execute_read_query,execute_query
from datetime import datetime

conn = create_connection('hw1cis3368.c8aubdep9gnu.us-east-2.rds.amazonaws.com','admin','Passward1!','intersteller') #Creates connection between MySql and Python file
app = flask.Flask(__name__) #Creates app init
app.config["DEBUG"] = True 

@app.route('/',methods=['GET'])
def home():
    return "<h1>WELCOME TO OUR PROJECT</h1>"


########################GET ROUTES FOR ALL TABLES#####################


##########CARGO TABLE GET ROUTE###########
@app.route('/api/cargo/all',methods=['GET']) #Creates get request for all cargo
def get_cargo():
    cargos = [] #Houses the SQL results
    sql_select = "SELECT * FROM cargo" #SQL command to get all cargo data
    cargos_ = execute_read_query(conn,sql_select) #Executes SQL
    for items in cargos_:#for loop to add data once get request is sent
        cargos.append(items) #Adds SQL records to cargo list
    return jsonify(cargos) #Turns list into JSON

app.run()

@app.route('/api/cargo',methods=['GET'])  #Can be tested by using link like this: http://127.0.0.1:5000/api/cargo?id=[ID of your choosing]
def get_cargo_id():
    cargos = [] #Houses the SQL results
    sql_select = "SELECT * FROM cargo" #SQL command to get all cargo
    cargos_ = execute_read_query(conn,sql_select) #Executes SQL
    for items in cargos_:
        cargos.append(items) #Adds SQL records to cargo list

#CREATED A NEW JSON WITHIN GET REQUESTS BECAUSE IT WOULD NOT CHANGE WHEN I USED A POST METHOD.

    if 'id' in request.args:  #Checks if and id is given in api parameters
        id = int(request.args['id']) #ID in parameter to be compared later in for loop.
    else:
        return "NO ID GIVEN" #If there is not ID in the parameter this will be returned.
    result = [] #All the results will be placed here
    for item in cargos_: #For loop iterates through cargo list in line 20
        if item['id'] == id: 
            result.append(item) #Adds record in result list if the id matches the parameter.
    return jsonify(result) #Turns the results list into JSON.

##########CAPTAIN TABLE GET ROUTE ##########
@app.route('/api/captain/all',methods=['GET']) #Creates get request for all captains
def get_captains():
    captain = [] #Houses the SQL results
    sql_select = "SELECT * FROM captain" #SQL command to get all captains
    captains = execute_read_query(conn,sql_select) #Executes SQL
    for c in captains:
        captain.append(c) #Adds SQL records to captain list
    return jsonify(captain) #Turns list into JSON


@app.route('/api/captain',methods=['GET'])  
def get_captain_id():
    captain = [] #get the sql 
    sql_select = "SELECT * FROM captain" #SQL command to get all captains
    captains = execute_read_query(conn,sql_select) #Executes SQL
    for item in captain:
        captains.append(item) #Adds SQL records to captains list
#CREATED A NEW JSON WITHIN GET REQUESTS BECAUSE IT WOULD NOT CHANGE WHEN I USED A POST METHOD.

    if 'id' in request.args:  #Checks if and id is given in api parameters
        id = int(request.args['id']) #ID in parameter to be compared later in for loop.
    else:
        return "NO ID GIVEN" #If there is not ID in the parameter this will be returned.
    result = [] #All the results will be placed here
    for item in captains: #For loop iterates through captains list 
        if item['id'] == id: 
            result.append(item) #Adds record in result list if the id matches the parameter.
    return jsonify(result) #Turns the results list into JSON and when testing start with 4 


##############SPACESHIP TABLE GET ROUTE ###################
@app.route('/api/spaceship/all',methods=['GET']) #Creates get request for all spaceships
def get_spaceshipss():
    spaceship = [] #Houses the SQL results
    sql_select = "SELECT * FROM spaceship" #SQL command to get all spaceships
    spaceships = execute_read_query(conn,sql_select) #Executes SQL
    for ships in spaceships:
        ships.append(ships) #Adds SQL records to spaceship list
    return jsonify(ships) #Turns list into JSON

@app.route('/api/spaceship',methods=['GET'])  
def get_spaceship_id():
    spaceship = [] #get the sql 
    sql_select = "SELECT * FROM spaceship" #SQL command to get all spaceship
    spaceships = execute_read_query(conn,sql_select) #Executes SQL
    for item in spaceships:
        item.append(spaceships) #Adds SQL records to spaceship list
#CREATED A NEW JSON WITHIN GET REQUESTS BECAUSE IT WOULD NOT CHANGE WHEN I USED A POST METHOD.

    if 'id' in request.args:  #Checks if and id is given in api parameters
        id = int(request.args['id']) #ID in parameter to be compared later in for loop.
    else:
        return "NO ID GIVEN" #If there is not ID in the parameter this will be returned.
    result = [] #All the results will be placed here
    for item in spaceships:
        if item['id'] == id: 
            result.append(item) #Adds record in result list if the id matches the parameter.
    return jsonify(result) #Turns the results list into JSON and when testing


    #####################POST ROUTES FOR ALL TABLES###################

    ###CARGO TABLE###
    @app.route('/api/cargo',methods=['POST']) #Adds new cargo to cargo table
    def add_cargo():
        request_data = request.get_json() #Allows data to added in JSON format
        new_weight = request_data['Weight'] #weight to add
        new_cargotype = request_data['Cargotype'] #cargotype to add
        new_departure = request_data['departure'] #departure to add
        new_arrival = request_data['arrival']  #arrival to add 
        new_shipid = request_data['shipid']  #shipid to add 

        add_sql = f"INSERT INTO Cargo VALUES (id,'{new_weight}','{new_cargotype}','{new_departure}','{new_arrivsl}'.'{shipid}')"  #Turns JSON data to SQL insert
        execute_query(conn,add_sql)

        return "NEW Cargo ADDED"


    ###CAPTAIN TABLE###
    @app.route('/api/captain',methods=['POST']) #Adds new captain to captain table
    def add_captain():
        request_data = request.get_json() #Allows data to added in JSON format
        new_firstname = request_data['firstname']
        new_lastname = request_data['lastname'] #new lastname to be added
        new_captainrank = request_data['captainrank'] #new captainrank to be added
        new_homeplanet = request_data['homeplanet'] #new homeplanet to be added
    
        add_sql = f"INSERT INTO Captain VALUES (id,{new_firstname},'{new_lastname}','{new_captainrank}','{new_homeplanet}')"  #Turns JSON data to SQL insert
        execute_query(conn,add_sql)

        return "NEW Captain ADDED"


    @app.route('/api/spaceship',methods=['POST']) #Adds new sapceship to spaceship table
    def add_spaceship():
        request_data = request.get_json() #Allows data to added in JSON format
        new_maxweight = request_data['maxweight']
        new_captainid = request_data['captainid'] #new captainif to be add

    
        add_sql = f"INSERT INTO Spaceship VALUES (id,{new_maxweight},'{new_captainid}')"  #Turns JSON data to SQL insert
        execute_query(conn,add_sql)

        return "NEW Spaceship ADDED"


###################PUT REQUEST FOR ALL TABLES##################

########CARGO TABLE############

@app.route('/api/cargo',methods=['PUT']) #Can be tested by using link like this: http://127.0.0.1:5000/api/cargo?id=[ID of your choosing]
def change_item():
    if 'id' in request.args:
        id=int(request.args['id'])
        request_data = request.get_json()
        it_weight = request_data['Weight'] #weight to update
        it_cargotype = request_data['Cargotype'] #cargotype to update
        it_departure = request_data['Departure'] #Departure to update
        it_arrival = request_data['Arrival'] 
        it_shipid = request_data['shipid']
        #arrival to update
        update_item_sql = f"UPDATE cargo SET Weight='{it_weight}', Cargotype'{it_cargotype}',Departure='{it_departure}',Arrival='{it_arrival},Shipid='{it_shipid}'  WHERE id={id}"
        execute_query(conn,update_item_sql)
        
    else:
        return 'NO ID GIVEN TO UPDATE' #If there is no ID in the API url this is returned.
    return 'CARGO UPDATED' #Confirms that cargo is updated.









########captain TABLE########
@app.route('/api/captain',methods=['PUT']) #Can be tested by using link like this: http://127.0.0.1:5000/api/captain?id=[ID of your choosing]
def change_item():
    if 'id' in request.args:
        id=int(request.args['id'])
        request_data = request.get_json() #Allows data to added in JSON format
        new_firstname = request_data['firstname']
        new_lastname = request_data['lastname'] #new lastname to be added
        new_captainrank = request_data['captainrank'] #new captainrank to be added
        new_homeplanet = request_data['homeplanet'] #new homeplanet to be added
    
        add_sql = f"INSERT INTO Captain VALUES (id,firstname='{new_firstname}',lastname='{new_lastname}',captainrank='{new_captainrank}',homeplanet='{new_homeplanet}')"  #Turns JSON data to SQL insert
        execute_query(conn,add_sql)
    else:
        return 'NO ID GIVEN TO UPDATE' #If there is no ID in the API url this is returned.
    return 'CAPTAIN UPDATED' #Confirms that captain is updated.


########SPACESHIP TABLE########

@app.route('/api/spaceship',methods=['PUT']) #Can be tested by using link like this: http://127.0.0.1:5000/api/spaceship?id=[ID of your choosing]
def change_spaceship():
    if 'id' in request.args:
        id=int(request.args['id'])
        request_data = request.get_json() #Allows data to added in JSON format
        sp_maxweight = request_data['maxweight']
        sp_captainid = request_data['captainid'] #new captainid to be added
        update_c_sql = f"UPDATE Spaceship SET (id, maxweight='{sp_maxweight}',captainid='{sp_captainid}' WHERE id={id}"
        execute_query(conn,update_c_sql)
        
    else:
        return 'NO ID GIVEN TO UPDATE' #If there is no ID in the API url this is returned.
    return 'Capiain UPDATED' #Confirms that captain is updated.




    #################DELETE ROUTES##################

    ###########CARGO TABLE##############
@app.route('/api/cargo',methods=['DELETE']) #Can be tested by using link like this: http://127.0.0.1:5000/api/cargo?id=[ID of your choosing]
def del_item():
    if 'id' in request.args:
        id=int(request.args['id']) #Allows user to user ID as parameter.
    else:
        return "NO ID GIVEN TO DELETE" #If no ID parameter is given this is returned
    delete_item_sql = f"DELETE FROM Cargo WHERE id={id}" #Runs SQL statment using the id param as WHERE constraint. 
    execute_query(conn,delete_item_sql) 

    return f"Cargo WITH ID:{id} DELETED" #Delete conformation

    ############CAPTAIN TABLE################
@app.route('/api/captain',methods=['DELETE']) #Can be tested by using link like this: http://127.0.0.1:5000/api/captain?id=[ID of your choosing]
def del_c():
    if 'id' in request.args:
        id=int(request.args['id']) #Allows user to user ID as parameter.
    else:
        return "NO ID GIVEN TO DELETE" #If no ID parameter is given this is returned
    delete_c_sql = f"DELETE FROM captain WHERE id={id}" #Runs SQL statment using the id param as WHERE constraint. 
    execute_query(conn,delete_c_sql) 
    return f"Captain WITH ID:{id} DELETED" 

    ############SPACESHIP TABLE################
    @app.route('/api/spaceship',methods=['DELETE']) #Can be tested by using link like this: http://127.0.0.1:5000/api/spaceship?id=[ID of your choosing]
    def del_ships():
        if 'id' in request.args:
            id=int(request.args['id']) #Allows user to user ID as parameter.
        else:
            return "NO ID GIVEN TO DELETE" #If no ID parameter is given this is returned
        delete_c_sql = f"DELETE FROM spaceship WHERE id={id}" #Runs SQL statment using the id param as WHERE constraint. 
        execute_query(conn,delete_c_sql) 

        return f"Spaceship WITH ID:{id} DELETED" 

app.run()

        ###############login API##############

# Pre-configured username and password
USERNAME = 'myusername'
PASSWORD = 'mypassword'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        if username == USERNAME and password == PASSWORD:
            return jsonify({'message': 'Logged in successfully'})
    return jsonify({'message': 'Invalid username or password'})

if __name__ == '__main__':
    app.run(debug=True)