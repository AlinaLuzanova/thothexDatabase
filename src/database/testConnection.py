from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()


class Database:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_molecule_node(self, name, smiles):
        with self._driver.session() as session:
            return session.execute_write(self._create_molecule_node, name, smiles)

    def create_reaction_node(self, reaction_name):
        with self._driver.session() as session:
            return session.execute_write(self._create_single_reaction_node, reaction_name)

    def create_reaction_relationships(self, reactant1, reactant2, product, reaction_name):
        with self._driver.session() as session:
            return session.execute_write(self._create_reaction_relationships, reactant1, reactant2, product,
                                         reaction_name)

    @staticmethod
    def _create_molecule_node(tx, name, smiles):
        query = (
            "CREATE (m:Molecule {name: $name, smiles: $smiles}) "
            "RETURN m"
        )
        result = tx.run(query, name=name, smiles=smiles)
        return result.single()[0]

    @staticmethod
    def _create_reaction_node(tx, reaction_name):
        query = (
            "CREATE (r:Reaction {name: $reaction_name}) "
            "RETURN r"
        )
        result = tx.run(query, reaction_name=reaction_name)
        return result.single()[0]

    @staticmethod
    def _create_reaction_relationships(tx, reactant1, reactant2, product, reaction_name):
        query = (
            "MATCH (r1:Molecule {name: $reactant1}), "
            "(r2:Molecule {name: $reactant2}), "
            "(p:Molecule {name: $product}), "
            "(reaction:Reaction {name: $reaction_name}) "
            "CREATE (r1)-[:REACTANT_OF]->(reaction), "
            "(r2)-[:REACTANT_OF]->(reaction), "
            "(reaction)-[:PRODUCT_OF]->(p)"
        )
        tx.run(query, reactant1=reactant1, reactant2=reactant2,
               product=product, reaction_name=reaction_name)

    @staticmethod
    def _create_single_reaction_node(tx, reaction_name):
        query = (
            "CREATE (r:Reaction {name: $reaction_name}) "
            "RETURN r"
        )
        result = tx.run(query, reaction_name=reaction_name)
        return result.single()[0]


# Пример использования
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

database = Database(uri, user, password)

# Создать узел молекулы для этанола
ethanol = database.create_molecule_node("Ethanol", "CCO")

# Создать узел молекулы для уксусной кислоты
acetic_acid = database.create_molecule_node("Acetic Acid", "CC(=O)O")

# Создать узел реакции образования эфира между этанолом и уксусной кислотой
ether_formation = database.create_reaction_node("Ether Formation")

# Создать узел молекулы для эфира
ether = database.create_molecule_node("Ether", "CCOC")

# Установить связи между молекулами и реакцией
database.create_reaction_relationships(
    "Ethanol", "Acetic Acid", "Ether", "Ether Formation")

# Закрыть соединение с базой данных
database.close()
