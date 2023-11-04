from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# URI de conexão com o banco de dados
colecao = "mongodb+srv://dbUser:dbUserPassword@cluster0.xiyzpaj.mongodb.net/?retryWrites=true&w=majority"

# Conectando ao banco de dados
client = MongoClient(colecao, server_api=ServerApi('1'))

# Acessando o banco de dados Lumus
db = client.get_database('Lumus')

# Acessando a coleção Lumus dentro do banco de dados
colecao = db.Lumus
