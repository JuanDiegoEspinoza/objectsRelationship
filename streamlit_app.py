import numpy as np
import pandas as pd
import streamlit as st
from anytree import Node, RenderTree, render, DoubleStyle
from anytree.exporter import UniqueDotExporter
from anytree import Node, render
from anytree import AnyNode
from anytree.exporter import JsonExporter
from anytree.exporter import DictExporter


def get_image_download_link(img, filename, text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href


uploadedFile = st.file_uploader("Choose file")

x = pd.read_csv(uploadedFile)
listNodesNames = []
listNodesObjets = []
grandParentNode = Node("GPP")

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
            i.parent = grandParentNode

    root = grandParentNode
   # exporter = JsonExporter(indent=2, sort_keys=True)
    #st.write(RenderTree(root, style=DoubleStyle()).by_attr())
    #exporter = DictExporter()
    #st.json(exporter.export(root))

    UniqueDotExporter(root).to_picture("udo")

