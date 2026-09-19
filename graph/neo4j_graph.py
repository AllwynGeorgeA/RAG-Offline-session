import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()


class Neo4jGraph:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(
                os.getenv("NEO4J_USERNAME"),
                os.getenv("NEO4J_PASSWORD")
            )
        )

    def close(self):
        self.driver.close()

    def add_relationship(
        self,
        source,
        relationship,
        target
    ):

        query = """
        MERGE (a:Entity {name: $source})
        MERGE (b:Entity {name: $target})
        MERGE (a)-[:RELATED_TO {type: $relationship}]->(b)
        """

        with self.driver.session() as session:

            session.run(
                query,
                source=source,
                relationship=relationship,
                target=target
            )

    def search_entity(self, entity):

        query = """
        MATCH (a:Entity)-[r]->(b:Entity)
        WHERE toLower(a.name) CONTAINS toLower($entity)
           OR toLower(b.name) CONTAINS toLower($entity)

        RETURN a.name AS source,
               type(r) AS relationship,
               b.name AS target
        """

        with self.driver.session() as session:

            result = session.run(
                query,
                entity=entity
            )

            return [
                {
                    "source": record["source"],
                    "relationship": record["relationship"],
                    "target": record["target"]
                }
                for record in result
            ]