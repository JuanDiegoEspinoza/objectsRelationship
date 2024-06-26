import numpy as np
import pandas as pd
import streamlit as st
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
from anytree import Node, render


uploadedFile = st.file_uploader("Choose file")

x = pd.read_csv(uploadedFile)
listNodesNames = []
listNodesObjets = []

if st.button('Read'):
    i = 0
    while i < len(x):
        parentName = x.iloc[i]['ob1']
        childName = x.iloc[i]['ob2']
        parentFlag = 0
        childFlag = 0
        
        newParentNode = Node(parentName)
        listNodesNames +=[parentName]
        listNodesObjets+= [newParentNode]

        #if(parentName in listNodesNames):
        #    newParentNode = listNodesObjets[listNodesNames.index(parentName)]
        #    parentFlag = 1

        #if(childName in listNodesNames):
        #    newChildNode = listNodesObjets[listNodesNames.index(childName)]
        #    childFlag = 1         
        
        newChildNode = Node(childName, parent=newParentNode)
        listNodesNames +=[childName]
        listNodesObjets+= [newChildNode]
        i+=1
    for i in listNodesObjets:
        root = i
        render.RenderTree(root).by_attr()
        st.write(render.RenderTree(root).by_attr())