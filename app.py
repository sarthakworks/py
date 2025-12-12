from flask import Flask, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# https://cloud.mongodb.com/ sarthak420@gmail
# open http://localhost:5001/comments to see data from sample_mflix.comments.
## in .env add relace password with actuall password from https://cloud.mongodb.com/v2/693be87fe6f5dd4307982816#/setup/access
# MongoDB Connection from.env for security, it should be pushed to github
uri = os.getenv('MONGO_URI')
if not uri:
    raise ValueError("No MONGO_URI found in environment variables")

if not uri.startswith("mongodb://") and not uri.startswith("mongodb+srv://"):
    raise ValueError(f"Invalid MONGO_URI: must start with 'mongodb://' or 'mongodb+srv://'. Got: {uri[:10]}...")

# Create a new client and connect to the server MongoDB Stable API version 1
client = MongoClient(uri, server_api=ServerApi('1'))

# Select database and collection  sample_mflix.comments
db = client['sample_mflix']
collection = db['comments']

def test_connection():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"Connection failed: {e}")

# Run connection test on startup (optional, but good for debugging)
test_connection()

@app.route('/')
def home():
    return "API is running! Go to /users to see data from sample_mflix.comments."

@app.route('/comments', methods=['GET'])
def get_users():
    try:
        # Fetch comments, exclude _id field for cleaner JSON output, limit to 10
        cursor = collection.find({}, {'_id': 0}).limit(10)
        comments = []
        for doc in cursor:
            # Convert ObjectId to string (e.g. movie_id)
            if 'movie_id' in doc:
                doc['movie_id'] = str(doc['movie_id'])
            # Convert datetime to string
            if 'date' in doc:
                doc['date'] = doc['date'].isoformat()
            comments.append(doc)
            
        return jsonify(comments)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)


