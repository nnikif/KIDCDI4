import re
import form_values as fv
import xml.etree.ElementTree as ET

def parsexml_quiz(fname='Петрова Маша_данные1.xml'):
    
    tree = ET.parse(fname)
    root=tree.getroot()
    dict0={}
    dict1={}
    for child in root:
        dict0[child.tag]=child.text
#         print(child.tag)
    # print(dict)
    for key in fv.KEYS:
        if key not in dict0:
            dict1[key]="Off"
        else:
            dict1[key]=dict0[key]    
    for key in dict1:
        if dict1[key] and dict1[key]!="Off":
            # print(key,dict1[key])

            if not key in fv.TEXT_KEYES:
                dict1[key]=int(str(dict1[key]))
            else:
                dict1[key]=str(dict1[key])
        else:
            if key in fv.TEXT_KEYES:
                dict1[key]=''
            else:
                dict1[key]=0
                
    
    return dict1

def parsexml_test(fname,length):
    lst=[None]*length
    tree = ET.parse(fname)
    root=tree.getroot()
    for child in root.iter('field'):
        digit=(re.findall(r'\d+',str(child.attrib)))
        digit=int(digit[0])
        if child.text!="Off":
            lst[digit]=int(child.text)
        else:
            lst[digit]=0
    return lst