from do_references import classid_dict
from do_references import status_dict
from do_references import reg_status_dict
from class_holding import Var_maker
from class_holding import ignore_quotes


mid_file_list = []
dict_for_check_reference = {}
qouts_deliter = Var_maker()

mid_example_path = "C:\Челябинская область (СТП РФ)\MIF — копия\GasFacility.mid"
mif_example_path = "C:\Челябинская область (СТП РФ)\MIF — копия\GasFacility.mif"

mif_file_show = open(mif_example_path, "r")
mid_file_show = open(mid_example_path, "r")

mif_data = mif_file_show.read()
# mid_data = mid_file_show.read()
were_is_colomns = mif_data.find("Columns")
were_is_data = mif_data.find("Data")
string_of_codes = mif_data[were_is_colomns : were_is_data]

list_of_codes = string_of_codes.split("\n")
list_of_codes.pop()
list_of_codes.pop(0)

for i in mid_file_show:
    mid_file_list.append(i)

list_of_mid_values = mid_file_list[1].split(",")
list_of_mid_values.pop()
if len(list_of_codes) == len(list_of_mid_values):
    for i in range(len(list_of_codes)):
            dict_for_check_reference[list_of_codes[i]] = list_of_mid_values[i]

    for k,v in dict_for_check_reference.items():
        if k.find("classid") > 0:
            dict_for_check_reference[k] = f"\"{classid_dict[v]}\""
        elif k.find("status") > 0 and k.find("reg") == -1:
            print(status_dict)
            print(dict_for_check_reference)
            dict_for_check_reference[k] = f"\"{status_dict[v]}\""

        elif k.find("reg_status") > 0:
            dict_for_check_reference[k] = f"\"{reg_status_dict[v]}\""
    back_to_list_for_join = dict_for_check_reference.values()
    str_for_write = ",".join(back_to_list_for_join)


    print(str_for_write)
else:
    print(len(list_of_codes))
    print(len(list_of_mid_values))
    print(status_dict)
    print(dict_for_check_reference)
