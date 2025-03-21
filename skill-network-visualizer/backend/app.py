from flask import Flask, jsonify
from neo4j import GraphDatabase
import os

app = Flask(__name__)

# Connect to Neo4j
driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
)

# Example API endpoint
@app.route('/api/people', methods=['GET'])
def get_people():
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p.name AS name")
        return jsonify([record["name"] for record in result])

if __name__ == '__main__':
    app.run(debug=True)