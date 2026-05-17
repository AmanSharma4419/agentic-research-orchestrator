from langgraph.checkpoint.mongodb import MongoDBSaver

# MongoDB configuration
MONGO_URI = "mongodb://admin:admin123@localhost:27017/?authSource=admin"
MONGO_DB_NAME = "langgraph_db"
MONGO_COLLECTION_NAME = "checkpoints"

# Create context manager
checkpointer_cm = MongoDBSaver.from_conn_string(
    conn_string=MONGO_URI,
    db_name=MONGO_DB_NAME,
    collection_name=MONGO_COLLECTION_NAME
)

checkpointer = checkpointer_cm.__enter__()