from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import socket
import dns.resolver

from config import MONGO_DB_URI

from ..logging import LOGGER

mongodb = None
if MONGO_DB_URI:
    LOGGER(__name__).info("Connecting to your Mongo Database...")
    try:
        # Set DNS settings
        dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
        dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google DNS
        
        # Create client with DNS settings
        _mongo_async_ = AsyncIOMotorClient(
            MONGO_DB_URI,
            serverSelectionTimeoutMS=30000,
            connectTimeoutMS=30000,
            socketTimeoutMS=30000
        )
        
        mongodb = _mongo_async_.Anon
        
        # Test the connection
        asyncio.get_event_loop().run_until_complete(_mongo_async_.admin.command('ping'))
        LOGGER(__name__).info("Connected to your Mongo Database.")
    except Exception as e:
        LOGGER(__name__).error(f"Failed to connect to your Mongo Database: {str(e)}")
        exit()
else:
    LOGGER(__name__).info("MongoDB connection skipped - MONGO_DB_URI not provided.")

