from collections import OrderedDict
from PyPDF2 import PdfFileWriter, PdfFileReader
import form_values as fv
from pprint import pprint
import re


def _getFields(obj, tree=None, retval=None, fileobj=None):
    """
    Extracts field data if this PDF contains interactive form fields.
    The *tree* and *retval* parameters are for recursive use.

    :param fileobj: A file object (usually a text file) to write
        a report to on all interactive form fields found.
    :return: A dictionary where each key is a field name, and each
        value is a :class:`Field<PyPDF2.generic.Field>` object. By
        default, the mapping name is used for keys.
    :rtype: dict, or ``None`` if form data could not be located.
    """
    fieldAttributes = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name', '/TU': 'Alternate Field Name',
                       '/TM': 'Mapping Name', '/Ff': 'Field Flags', '/V': 'Value', '/DV': 'Default Value'}
    if retval is None:
        retval = OrderedDict()
        catalog = obj.trailer["/Root"]
        # get the AcroForm tree
        if "/AcroForm" in catalog:
            tree = catalog["/AcroForm"]
        else:
            return None
    if tree is None:
        return retval

    obj._checkKids(tree, retval, fileobj)
    for attr in fieldAttributes:
        if attr in tree:
            # Tree is a field
            obj._buildField(tree, retval, fileobj, fieldAttributes)
            break

    if "/Fields" in tree:
        fields = tree["/Fields"]
        for f in fields:
            field = f.getObject()
            obj._buildField(field, retval, fileobj, fieldAttributes)

    return retval


def remove_slash(str_val):
    if str_val == '' or str_val == '/':
        return 0
    if str_val[0] == '/':
        return int(str_val[1])
    else:
        return int(str_val)


def get_form_fields(infile, length):
    infile = PdfFileReader(open(infile, 'rb'))
    fields = _getFields(infile)
    dict1 = OrderedDict((k, v.get('/V', '')) for k, v in fields.items())
    dict_p1 = {}
    list_p2 = [0] * length
    for key in dict1:
        if key not in fv.TEXT_KEYES and dict1[key] != '' and key in fv.KEYS:
            dict_p1[key] = remove_slash(dict1[key])
        if key in fv.TEXT_KEYES:
            dict_p1[key] = dict1[key]

        if key not in fv.KEYS:
            if "Radio" in key:
                digit = (re.findall(r'\d+', str(key)))
                digit = int(digit[0])
                list_p2[digit] = remove_slash(dict1[key])
#                 print (digit, list_p2[digit])

    return dict_p1, list_p2


if __name__ == '__main__':
    pdf_file_name = 'RCDI_Blueprint_Final.pdf'

    d1, d2 = get_form_fields(pdf_file_name, 216)
#     print(d2)
