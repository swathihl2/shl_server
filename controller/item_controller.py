# controllers/item_controller.py
from flask import Blueprint, jsonify, request
from db.mongo import db

item_bp = Blueprint('item_bp', __name__)
collection = db['items']


def parse_query_params(params):
    query = {}
    for key, value in params.items():
        if key == '_id':
            try:
                query[key] = int(value)
            except ValueError:
                raise ValueError('Invalid _id. It must be an integer.')
        else:
            query[key] = {'$regex': value, '$options': 'i'}  # Case-insensitive search
    return query


@item_bp.route('/items', methods=['GET'])
def get_items():
    try:
        query = parse_query_params(request.args)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    items = list(collection.find(query))
    for item in items:
        item['_id'] = str(item['_id'])
    return jsonify(items)


@item_bp.route('/items', methods=['POST'])
def create_item():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided.'}), 400

    result = collection.insert_one(data)
    new_item = collection.find_one({'_id': result.inserted_id})
    new_item['_id'] = str(new_item['_id'])
    return jsonify(new_item), 201


@item_bp.route('/items', methods=['PUT'])
def update_items():
    update_data = request.json
    if not update_data:
        return jsonify({'error': 'No data provided for update.'}), 400

    query = parse_query_params(request.args)

    result = collection.update_many(query, {'$set': update_data})
    if result.matched_count:
        return jsonify({'message': f'{result.modified_count} item(s) updated successfully.'}), 200
    return jsonify({'error': 'No items found matching the criteria for update.'}), 404


@item_bp.route('/items', methods=['DELETE'])
def delete_items():
    try:
        query = parse_query_params(request.args)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    result = collection.delete_many(query)
    if result.deleted_count:
        return jsonify({'message': f'{result.deleted_count} item(s) deleted successfully.'}), 200
    return jsonify({'error': 'No items found matching the criteria.'}), 404
