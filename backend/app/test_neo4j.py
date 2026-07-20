from neo4j import GraphDatabase

from app.core.config import settings


driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(
        settings.NEO4J_USERNAME,
        settings.NEO4J_PASSWORD
    )
)


def test_connection():

    try:

        with driver.session() as session:

            result = session.run(
                "RETURN 'Neo4j Connected' AS message"
            )

            print(
                result.single()["message"]
            )

    except Exception as e:

        print(
            "Neo4j connection failed:"
        )

        print(e)


if __name__ == "__main__":
    test_connection()