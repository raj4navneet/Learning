# Get a specfic node to read the scenegraph from
node = NodegraphAPI.GetNode('Dot2')
# Collects specfic location matching the CEL statement
collector = Widgets.CollectAndSelectInScenegraph('''/root/world/lgt//*{@type == "light"}''', "/root/world/lgt")
# collect and save them all in the variable
matchedLocationPaths = collector.collectAndSelect(select=False, node=node)

# Cooking scene from the particular node
rootProducer = Nodes3DAPI.GetGeometryProducer(node)
# 
sg = ScenegraphManager.getActiveScenegraph()

lightRigs = []
for location in matchedLocationPaths:
    locationProducer = rootProducer.getProducerByPath(location)
    lightRigs.append(locationProducer)
    #print(dir(locationProducer))
    print(locationProducer.getGlobalAttribute('material.prmanLightParams.intensity').getValue())
