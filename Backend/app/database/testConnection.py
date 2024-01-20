from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

from Backend.app.models.reaction import Reaction

from Backend.app.models.molecule import Molecule

load_dotenv()

uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")


class Database:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_node(self, entity):
        with self._driver.session() as session:
            return session.execute_write(entity.create_node)

    def create_relationships(self, reactant1, reactant2, product, reaction):
        with self._driver.session() as session:
            return session.execute_write(
                self._create_reaction_relationships,
                reactant1.to_dict(),
                reactant2.to_dict(),
                product.to_dict(),
                reaction.to_dict(),
            )

    @staticmethod
    def _create_reaction_relationships(tx, reactant1, reactant2, product, reaction):
        query = (
            "MATCH (r1:Molecule {name: $reactant1_name}), "
            "(r2:Molecule {name: $reactant2_name}), "
            "(p:Molecule {name: $product_name}), "
            "(reaction:Reaction {name: $reaction_name}) "
            "CREATE (r1)-[:REACTANT_OF]->(reaction), "
            "(r2)-[:REACTANT_OF]->(reaction), "
            "(reaction)-[:PRODUCT_OF]->(p)"
        )
        tx.run(query, reactant1_name=reactant1["name"], reactant2_name=reactant2["name"], product_name=product["name"],
               reaction_name=reaction["name"])


database = Database(uri, user, password)

# Создать экземпляры классов молекул
ethanol = Molecule("Ethanol", "CCO")
acetic_acid = Molecule("Acetic Acid", "CC(=O)O")
ether = Molecule("Ether", "CCOC")

# Создать экземпляр класса реакции
ether_formation = Reaction("Ether Formation")

# Создать узлы молекул и реакции в базе данных
database.create_node(ethanol)
database.create_node(acetic_acid)
database.create_node(ether)
database.create_node(ether_formation)

# Установить связи между молекулами и реакцией
database.create_relationships(ethanol, acetic_acid, ether, ether_formation)

# Закрыть соединение с базой данных
database.close()
