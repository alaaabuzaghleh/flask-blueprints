from flask import Blueprint, Flask, request, Response, jsonify
from models import Item, toDoList

blueprint = Blueprint('todo' , __name__, url_prefix='/api/v1/todo')
@blueprint.route("/list")
def getAllToDos():
    """
    return all the todo item in the list
    ---
    tags:
      - todo
    responses:
      200:
        description: return all the todo item in the toDoList
        schema:
            type: array
            items:
              schema:
                properties:
                  id:
                    type: string
                  name:
                    type: string
                  desc:
                    type: string
    """
    return jsonify(toDoList)

@blueprint.route("/todo", methods=["POST"])
def createNewToDoItem():
    item=Item(**request.get_json())
    toDoList.append(item.toJson())
    return Response('{"message":"success"}', status=201, mimetype='application/json')

@blueprint.route("/todo/<id>")
def findToDoItemById(id):
    itemToReturn = None
    for item in toDoList:
        if item["id"] == id:
            itemToReturn = item
        else:
            continue
    if itemToReturn == None:
        return Response('{"message":"item not found"}', status=404, mimetype='application/json')
    else:
        response = jsonify(itemToReturn)
        response.status_code = 200
        return response

@blueprint.route("/todo" , methods=["PUT"])
def updateExistingToDoItem():
    item=Item(**request.get_json())
    isExist = False
    for i in toDoList:
        if i["id"] == item.id :
            i["title"] = item.title
            i["desc"] = item.desc
            isExist = True
            break
    if isExist:
        response = jsonify({"message":"item updated successfully"})
        response.status_code = 201
        return response
    else:
        response = jsonify({"message":"item not exist"})
        response.status_code = 404
        return response

@blueprint.route("/todo/<id>" , methods=["DELETE"])
def deleteToDoItemById(id):
    itemToDelete = None
    for item in toDoList:
        if item["id"] == id:
            itemToDelete = item
        else:
            continue
    if itemToDelete == None:
        response = jsonify({"message":"item not exist"})
        response.status_code = 404
        return response
    else:
        toDoList.remove(itemToDelete)
        response = jsonify({"message":"item removed successfully"})
        response.status_code = 200
        return response
