def IPRNetworkPlot(tree_file, arg_IPR = None, arg_domain = None, arg_type = None):
    """
    _summary_
    A faster function to normalize the parent
    child relationship of the interpro domains and
    plot the undirected graph for the desired interpro
    domain. 

    Arguments:
        tree_file -- _description_
        a intepro domain parent child tree file
        for viewing the undirected acyclic network
        graph. The current release of the tree file
        can be found at: https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/ParentChildTreeFile.txt
    """
    if arg_type == "interpro" and arg_IPR:
        read_file=list(filter(None,[i.strip() for i in open(tree_file).readlines()]))
        domaindict={};
        for line in read_file:
            if line.startswith('IPR'):
                    doname = line.strip()
                    if line not in domaindict:
                        domaindict[line] = ""
                    continue
            domaindict[doname] += line.strip()
        normalize_domain = {}
        for k,v in domaindict.items():
            normalize_domain[k.split("::")[0]] = [i for i in ([i.replace("--", "") \
                                            if i.startswith("--") else i for i in \
                                                v.split("::")]) if i.startswith("IPR")]
        normalize_categories = {}
        for k,v in domaindict.items():
            normalize_categories[k.split("::")[1]] = list(filter(None,[i for i in \
                                                    ([i.replace("--", "") if i.startswith("--") \
                                                           else i for i in v.split("::")]) if \
                                                                         not i.startswith("IPR")]))
        return [v for k,v in normalize_domain.items() if k == arg_IPR]

    if arg_type == "domain" and arg_domain:
        read_file=list(filter(None,[i.strip() for i in open(tree_file).readlines()]))
        domaindict={};
        for line in read_file:
            if line.startswith('IPR'):
                    doname = line.strip()
                    if line not in domaindict:
                        domaindict[line] = ""
                    continue
            domaindict[doname] += line.strip()
        normalize_domain = {}
        for k,v in domaindict.items():
            normalize_domain[k.split("::")[0]] = [i for i in ([i.replace("--", "") \
                                            if i.startswith("--") else i for i in \
                                                v.split("::")]) if i.startswith("IPR")]
        normalize_categories = {}
        for k,v in domaindict.items():
            normalize_categories[k.split("::")[1]] = list(filter(None,[i for i in \
                                                    ([i.replace("--", "") if i.startswith("--") \
                                                           else i for i in v.split("::")]) if \
                                                                         not i.startswith("IPR")]))
        return [v for k,v in normalize_categories.items() if k == arg_domain]
