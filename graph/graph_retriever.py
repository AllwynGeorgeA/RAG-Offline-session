from graph.neo4j_graph import Neo4jGraph


def get_graph_context(entity):

    graph = Neo4jGraph()

    try:
        results = graph.search_entity(entity)

        if not results:
            return []

        context = []

        for item in results:

            text = (
                f"{item['source']} "
                f"{item['relationship']} "
                f"{item['target']}"
            )

            context.append(text)

        return context

    finally:
        graph.close()