from xml.etree import cElementTree as ET
import os

directory = "corpus_multilingue/corpus_ara"
f = open("fromXML.txt", "a")

for filename in os.listdir(directory):
    if filename.endswith(".xml"):
        tree = ET.parse(os.path.join(directory, filename))
        root = tree.getroot()
        for child in root.iter('p'):
            if child.text is not None:
                f.write(child.text)
        f.write('\n')
