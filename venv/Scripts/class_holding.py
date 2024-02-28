# -*- coding: utf-8 -*-
from do_references import classid_dict
from do_references import status_dict
from do_references import reg_status_dict
import re
import math
from os import listdir
from os import scandir
dir_path = f"C:\Челябинская область (СТП РФ)\MIF — копия completed successfully"
def low_to_UPP():
    with scandir(dir_path) as files:
        for file in files:
            file_name = file.name
            file_name, file_extencion = file_name.split(".")
            if file_extencion == "mif":
                read_mif = open(file.path, "r+")
                mif_data = read_mif.read()
                read_mif.close()
                # mid_data = mid_file_show.read()
                were_is_colomns = mif_data.find("Columns")
                were_is_data = mif_data.find("Data")
                string_of_codes = mif_data[were_is_colomns: were_is_data]
                list_of_codes = string_of_codes.split(" ")
                list_of_codes.pop(0)
                list_of_codes.pop(0)
                list_of_codes = list(filter(None, list_of_codes))
                list_of_codes = map(lambda x : " " + x + " ", list_of_codes)
                list_of_codes = list(list_of_codes)
                new_data = mif_data
                if " status " in new_data:
                    new_data.replace(" status Integer", " status Char(254)")
                elif " reg_status " in new_data:
                    new_data.replace(" reg_status Integer", " reg_status Char(254)")
                elif " classid " in new_data:
                    new_data.replace(" classid Integer", " classid Char(254)")
                for i in list_of_codes:
                    if mif_data.find(i)> 0 and i.find("\n") == -1 :
                        new_data = new_data.replace(i , i.upper())
                        print(i.upper())
                read_mif = open(file.path, "w")

                read_mif.write(new_data)


