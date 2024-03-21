# bacterial_plant_fungal_domain_directed_graphs
This repository contains a function which will prepare the domain graphs analysis, if you will specify a domain or an interpro, it will give you all the parent and the child graphs for the directed and undirected graphs modelling. I implemented a string pattern search algorithm to make the search faster. 
```python
# for searching all the child categories of the IPR domains
IPRNetworkPlot("/Users/gauravsablok/Desktop/ipr_analyzer.txt", \
                               arg_IPR = "IPR000008", arg_type = "interpro")
[['IPR014705',
  'IPR028692',
  'IPR030537',
  'IPR033884',
  'IPR037300',
  'IPR037301',
  'IPR037302',
  'IPR037303',
  'IPR047897']]
# for searching all the child domains of the specific category
IPRNetworkPlot("/Users/gauravsablok/Desktop/ipr_analyzer.txt", \
                             arg_domain = "C2 domain", arg_type = "domain")
[['Synaptotagmin-17, C2B domain',
  'Synaptotagmin-13, C2B domain',
  'Synaptotagmin-12, C2B domain',
  'Calpain C2 domain',
  'Perforin-1, C2 domain',
  'Toll-interacting protein, C2 domain',
  'Protein Unc-13, C2B domain',
  'Synaptotagmin-like protein 4/5, C2A domain',
  'Synaptotagmins 15/17, C2A domain']]
```
Gaurav Sablok \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany
