import numpy as np
import pandas as pd
import streamlit as st
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
from anytree import Node, render
from anytree import AnyNode
from anytree.exporter import JsonExporter


uploadedFile = st.file_uploader("Choose file")

x = pd.read_csv(uploadedFile)
listNodesNames = []
listNodesObjets = []
GPP_Node = Node("GPP")

listNodesObjets += GPP_Node
listNodesNames += "GPP"

if st.button('Read'):
    i = 0
    while i < len(x):
        parentName = x.iloc[i]['ob1']
        childName = x.iloc[i]['ob2']

        newParentNode = Node(parentName)
        
        if(parentName in listNodesNames):
            newParentNode = listNodesObjets[listNodesNames.index(parentName)]       
        
        listNodesNames +=[parentName]
        listNodesObjets +=[newParentNode]

        newChildNode = Node(childName, parent=newParentNode)

        if(childName in listNodesNames):
            newChildNode = listNodesObjets[listNodesNames.index(childName)]

        listNodesNames +=[childName]
        listNodesObjets +=[newChildNode]

        i+=1
    #root = listNodesObjets[listNodesNames.index('V01_CPT_RESULTS')]
    #exporter = JsonExporter(indent=2, sort_keys=True)
    #st.write(exporter.export(root))

    for i in listNodesObjets:
        if i.is_root:
            i.parent = GPP_Node

    root = listNodesObjets[listNodesNames.index('GPP')]
    exporter = JsonExporter(indent=2, sort_keys=True)
    st.write(exporter.export(root))

