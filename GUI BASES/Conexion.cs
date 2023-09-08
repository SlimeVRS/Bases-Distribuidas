using System;
using MongoDB.Bson;
using MongoDB.Driver;

namespace ConexionMongoDB
{
    class Program
    {
        static void Main(string[] args)
        {
            // Cadena de conexión a MongoDB (asegúrate de que MongoDB esté en ejecución)
            string connectionString = "mongodb+srv://sebasmena:abcd1234@lab01bda.dravvoh.mongodb.net/";

            // Crea un cliente de MongoDB
            MongoClientSettings settings = MongoClientSettings.FromUrl(new MongoUrl(connectionString));
            MongoClient client = new MongoClient(settings);

            // Accede a una base de datos específica
            IMongoDatabase database = client.GetDatabase("ProyectoUnoBDA");

            // Accede a una colección específica dentro de la base de datos
            IMongoCollection<BsonDocument> collection = database.GetCollection<BsonDocument>("Usuario");

            // Realiza operaciones en la colección
            var documents = collection.Find(new BsonDocument()).ToList();

            // Imprime solo campos específicos de los documentos
            foreach (var document in documents)
            {
                // Accede a un campo específico y conviértelo a una cadena de texto
                string fieldValue = document["apellido"].AsString; // Reemplaza "campo" con el nombre del campo que deseas
                string fieldValue1 = document["nombre"].AsString; // Reemplaza "campo" con el nombre del campo que deseas
                string fieldValue2 = document["identificación"].AsString; // Reemplaza "campo" con el nombre del campo que deseas
                string fieldValue3 = document["morosidad"].AsString; // Reemplaza "campo" con el nombre del campo que deseas


                Console.WriteLine(fieldValue);
                Console.WriteLine(fieldValue1);
                Console.WriteLine(fieldValue2);
                Console.WriteLine(fieldValue3);

                Console.WriteLine(); // Agrega un salto de línea en blanco después de cada valor
            }
        }
    }
}
