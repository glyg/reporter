
import datetime
import warnings
import json

def create_header(dico,ville="Paris"):
    """Returns the header strings with authors listed
    
    Parameters
    ----------
    dico : list of dictionary 
        Each element of dico should have the 'first' 
        and 'last' keys
    
    Returns
    -------
    header : str
        The headers string at today's date
    
    """
    ajd = datetime.date.today()
    
    temp = [f'{ville} le {ajd.strftime("%A %d %B %Y")}\n',
           "### auteurs : \n"]
    for aut in dico:
        nom = f'- {aut.get("first","")} {aut.get("last","")}'
        if not aut.get("first",""):
            warnings.warn(f'key "first" not found in {aut}')
        if not aut.get("last",""):
            warnings.warn(f'key "last" not found in {aut}')
            
        temp.append(nom)
    res = print("\n".join(temp))
    return res
 
def header_json(file):
    """Returns the header strings with authors list
    from a json file
    
    Parameters
    ----------
    file : json file containing a list of dictionary 
        Each element of dico should have the 'first' 
        and 'last' keys
    
    Returns
    -------
    header : str
        The headers string at today's date
    
    """
    with open(file, 'r', encoding = "utf-8") as file_handle:
        file_authors = json.load(file_handle)
    
    texte = create_header(file_authors)
    
    return texte