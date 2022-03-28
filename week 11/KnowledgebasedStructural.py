''' 
 usually have rules stored somewhere
 humans use natural language and symbols are used for computers
 the symbols normaly used to represents a knownledge
 knowledge relationships can be used in representatiosn such as Decision tables - spreadsheets
 Decision trees - nodes and links, knowledge diagraming
 computational logic - propsitional true/false statement, predicate logic

knowledge representations
1. sematic network - used for putting your facts forward
2. production rules - commonly has a condition within it 
3. frame representation - useful for metadatas
4. logical representaion - facts that can be accepted and vice versa

Logic programming - is based on formal logic 
facts are unconditionally true in nature 

'''
from kanren import * 

tools = Relation()
careers = Relation()
facts(tools, ("Java", "Language"),
 ("Java", "Language"),
 ("Pyhton", "Language"),
 ("Word", "Package"),
 ("Excel", "Package"),
 ("Windows", "OS"),
 ("Linux", "OS")
)

facts(careers, ("Programming", "Language"),
("User", "Package"),
("Networking", "OS")
)

careers_tool, tools_v, careers_v = var(), var(), var()
run(0, careers_tool, tools(careers_tool, tools_v), careers("Networking", tools_v))

def career_tools(x,y):
    z = var()
    return conde ((tools(x,z), careers(y,z)))
what = var()
print (run(0, what, careers_tool(what, "Networking")))   