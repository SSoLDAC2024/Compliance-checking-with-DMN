import rdflib

# Load your Turtle file into a graph
g = rdflib.Graph()
g.parse("data/stairsGraph.ttl", format="turtle")

# Define your SPARQL query
query = """
prefix ex: <http://example.org/myData#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?stairs ?rh ?tl ?nr ?n
WHERE {
 ?stairs a ex:stairs ;
    ex:riserHeight ?rh ;
    ex:threadLength ?tl ;
    ex:numberOfRailings ?nr ;
    rdfs:label ?n .
}
"""

# Execute the query
results = g.query(query)

myDict = []
# Iterate over and print the results
for row in results:
   stairsInstance = {
      "RiserHeight": row.rh.value,
      "ThreadLength": row.tl.value,
      "NumberOfRailings": row.nr.value,
      "name": row.n.value
   }

   myDict.append(stairsInstance)

print(myDict)