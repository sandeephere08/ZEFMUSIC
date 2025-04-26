from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def test_connection():
    try:
        # MongoDB connection string
        uri = "mongodb+srv://rekhasharma13061990:hV4rvUCBlWmpajo0@cluster0.t86veax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        
        # Create client
        client = AsyncIOMotorClient(uri)
        
        # Test connection
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        # List databases
        databases = await client.list_database_names()
        print("Available databases:", databases)
        
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
    finally:
        if 'client' in locals():
            client.close()

# Run the test
asyncio.run(test_connection()) 