# -*- coding: utf-8 -*-
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from os import listdir
from os import scandir
from do_references import classid_dict
from do_references import status_dict
from do_references import reg_status_dict
import re
import os.path
import do_references

layer_name_arr = ['TYPE_SUBJ', 'TYPE_MUN', 'SETTL_LEVEL', 'SETTL_TYPE', 'STATUS_ADM', 'STYPE', 'EDU_SDTYPE', 'SCI_TYPE', 'PRG_TYPE', 'EDU_TUNIT', 'CU_TYPE', 'CLB_TYPE', 'ENT_TYPE', 'AF_TYPE', 'MD_STYPE', 'AMB_TYPE', 'MST_TYPE', 'SU_TYPE', 'MSD_TYPE', 'MC_TYPE', 'NSI_TYPE', 'ST_STYPE', 'SP_STYPE', 'SSAH_STYPE', 'USA_STYPE', 'TYPEMOLPO', 'HOT_STYPE', 'SAF_STYPE', 'CHI_STYPE', 'AL_STYPE', 'SEASON', 'TEM_TYPE', 'RES_STYPE', 'AB_STYPE', 'CR_STYPE', 'TRD_STYPE', 'RS_STYPE', 'PU_STYPE', 'TPARK_TYPE', 'PKIO_TYPE', 'PED_TYPE', 'AQ_STYPE', 'MP_TYPE', 'MAIN_TYPE', 'STORE_TYPE', 'SERV_STYPE', 'TYPE_INP', 'RECYC_TYPE', 'BUR_TYPE', 'ORO_TYPE', 'ORO_STYPE', 'TYPE_BENT', 'CAT_RR', 'EL_SUPPLY', 'TRACK_TYPE', 'NUM_TRACKS', 'RST_TYPE', 'RST_CLASS', 'RFO_TYPE', 'CAT_RDTYPE', 'REG_RDTYPE', 'TIME_LTYPE', 'RDWIN_TYPE', 'RDWIN_CAT', 'STR_R_TYPE', 'STR_L_TYPE', 'STR_G_TYPE', 'STR_O_TYPE', 'STR_TYPE', 'GAS_ST_TYPE', 'PRKNG_TYPE', 'PRKNG_LVL', 'PRKNG_TIME', 'STOP_TYPE', 'AVIA_TYPE', 'RWY_CLASS', 'LAND_TYPE', 'PASS_TERM', 'FERRY_CRGT', 'FERRY_MVT', 'YATCH_CLS', 'INT_TRN_T', 'INT_TRF_T', 'CTM_TIME_T', 'CTM_USE_T', 'BRIDGE_T', 'TUNNEL_T', 'CROSSW_T', 'CROSSR_T', 'USING_TYPE', 'SURFACE_TYPE', 'SUBURBAN_TR', 'POWER_TYPE', 'FUEL_TYPE', 'PL_TYPE', 'FEATURE_LEP', 'VOLTAGE', 'CAT_DISTR', 'WATER_STYPE', 'SNOW_TYPE', 'COMM_TYPE', 'COMM_СTYPE', 'CABLE_TYPE', 'GTS_CLASS', 'CEP_CLASS', 'CURRENT', 'PLINE_TYPE', 'CAT_ MAIN', 'FSES_STYPE', 'FP_TYPE', 'FP_CLASS', 'W_SOURCE', 'FS_OBJECTS', 'D_OBJECTS', 'S_ALERT', 'CEMET_TYPE', 'CEMET_STYPE', 'CEMET_WTYPE', 'CEMET_STAT', 'PRZIFL','SZZ_TYPE', 'SPZ_EVENT', 'ZONE_OOPT', 'FLOODING _T', 'UDERFL_T', 'AEROSZONE', 'Heritage', 'HER_TYPE', 'ANS_TYPE', 'OCH_USE', 'DST_TYPE', 'SPECIFIC', 'SETTL_CAT', 'HIST_CAT', 'HIST_OUT', 'STATUS_OCH', 'EME_SOURCE', 'RISK_CAT', 'TM_SOURCE', 'IND_TYPE', 'RAD_CLASS', 'EME_CLASS', 'MIN_MTYPE', 'MIN_NTYPE', 'MIN_ATYPE', 'FZ_MFSTP', 'FZ_ODSTP', 'FZ_INGSTP', 'FZ_TRSTP', 'FZ_SHSTP', 'FZ_RECSTP', 'FZ_ORECSTP', 'FZ_VIDZIL', 'TYPEOROSH', 'OZSN_TYPE', 'FOREST_CAT', 'FOREST_T', 'FOREST_VAL', 'FOREST_OS', 'HZRD_CLASS', 'HZRD_CAT', 'GROUND_POS', 'DANGER_OBJ']
print(len(layer_name_arr))
dir_path = filedialog.askdirectory()
mid_file_list = []
dict_for_check_reference = {}
dict_with_bool_change_marker = {}
new_dir_name = dir_path + " " + "completed successfully"
f = os.mkdir(new_dir_name)
new_dir_path = os.path.dirname(new_dir_name)


mid_example_path = "empty"
mif_example_path = "empty"


def replace_integer_to_char(key_of_dict_with_bool_value: str, some_data):
    read_mif = open(new_path_to_new_mif, "w")
    for i in range(len(key_of_dict_with_bool_value)):
        if dict_with_bool_change_marker[key_of_dict_with_bool_value] == True:
            cut_for_key = key_of_dict_with_bool_value.split(" ")
            cut_for_key = list(filter(None, cut_for_key))
            cut_for_key[1] = "Char(254)"
            key_for_write = " ".join(cut_for_key)
            key_for_write = "  " + key_for_write
            if some_data.find(key_of_dict_with_bool_value) != -1:
                new_data = some_data.replace(key_of_dict_with_bool_value, key_for_write)

    read_mif.write(new_data)
    read_mif.close()
    return new_data


def check_in_references(layer_code_name: str, k, v):
    layer_code_name = layer_code_name.lower()
    if k.find(layer_code_name) > 0 or k.find(layer_code_name.upper()) > 0:
        dict_for_check_reference[k] = f"\"{layer_code_name[v]}\""
        dict_with_bool_change_marker[k] = True


def castom_split_func(str_for_split:str,num_column, delimitr):

    str_for_split = list(str_for_split)
    get_column = True
    count_mark = 0
    count_column = 1
    start_position = 1
    end_position = len(str_for_split)
    i = 0
    while i < len(str_for_split):

        try:
            if str_for_split[i] == "\"": count_mark += 1

            if count_mark == 2: count_mark = 0

            if str_for_split[i] == delimitr and count_mark == 0:
                count_column += 1
                str_for_split[i] = str_for_split[i].replace(delimitr, "||||")
                if count_column == num_column: start_position += 1
                if count_column == num_column + 1:
                    end_position -= 1
        except IndexError:
            pass
        i += 1
    if num_column < count_column:
        get_column = str_for_split[start_position: end_position]
    new_str = "".join(get_column)

    new_str = new_str.split("||||")

    return new_str


with scandir(dir_path) as files:
    for file in files:
        file_name = file.name
        file_name, file_extencion =file_name.split(".")
        new_file = open(file.name, "w")
        new_file_path = os.path.abspath(new_file.name)
        new_file.close()
        if file_extencion == "mid":
            mid_example_path = file.path
            name_for_compare_mid = file_name
            new_path_to_new_file = shutil.move(new_file_path, new_dir_name)

        elif file_extencion == "mif":
            mif_example_path = file.path
            name_for_compare_mif = file_name
            new_path_to_new_mif = shutil.move(new_file_path, new_dir_name)
        else:
            print("ОШИБКА: файл не МИФ и не МИД")
        try:

            if mid_example_path != mif_example_path and name_for_compare_mif == name_for_compare_mid:

                mif_file_show = open(mif_example_path, "r")
                mid_file_show = open(mid_example_path, "r")
                mid_for_write = open(new_path_to_new_file, "w")
                mif_data = mif_file_show.read()
                                # mid_data = mid_file_show.read()
                were_is_colomns = mif_data.find("Columns")
                were_is_data = mif_data.find("Data")
                string_of_codes = mif_data[were_is_colomns : were_is_data]
                pre_delimitr_id = mif_data.find("Delimiter")
                delimiter = mif_data[pre_delimitr_id +len("Delimiter") + 2]
                list_of_codes = string_of_codes.split("\n")
                list_of_codes.pop()
                list_of_codes.pop(0)
                mif_file_show.close()

                for i in mid_file_show:

                    list_of_mid_values =castom_split_func(i, 0, delimiter)

                    for i in range(len(list_of_codes)):
                        try:
                            dict_for_check_reference[list_of_codes[i]] = list_of_mid_values[i]
                            dict_with_bool_change_marker[list_of_codes[i]] = False # Хранит коды атрибутов с ложью и меняется когда атрибут изменяется (с цифры на строку)

                        except IndexError:
                            print("I AM HERE, I AM ERRROOR")
                    for k,v in dict_for_check_reference.items():
                        try:
                            if k.find("classid") > 0 or k.find("CLASSID") > 0:

                                dict_for_check_reference[k] = f"\"{classid_dict[v]}\""
                                dict_with_bool_change_marker[k] = True

                            elif k.find("status") > 0 and k.find("reg") == -1 and k.find("pr") == -1:

                                dict_for_check_reference[k] = f"\"{status_dict[v]}\""
                                dict_with_bool_change_marker[k] = True

                            elif k.find("STATUS") > 0 and k.find("REG") == -1 and k.find("PR") == -1:
                                dict_for_check_reference[k] = f"\"{status_dict[v]}\""
                                dict_with_bool_change_marker[k] = True

                            elif k.find("reg_status") > 0 or k.find("REG_STATUS") > 0:
                                dict_for_check_reference[k] = f"\"{do_references.reg_status_dict[v]}\""
                                dict_with_bool_change_marker[k] = True

                            # elif k.find("status_pr") > 0 or k.find("STATUS_PR") > 0:
                            #     dict_for_check_reference[k] = f"\"{do_references.STATUS_PR[v]}\""
                            #     dict_with_bool_change_marker[k] = True
                            # elif k.find("danger_obj") > 0 or k.find("DANGER_OBJ"):
                            #     dict_for_check_reference[k] = f"\"{do_references.DANGER_OBJ[v]}\""
                            #     dict_with_bool_change_marker[k] = True

                        except KeyError:
                            pass
                            #messagebox.showerror(title="ERROOOOR", message=f"{file_name}")

                    back_to_list_for_join = dict_for_check_reference.values()
                    str_for_write = ",".join(back_to_list_for_join)
                    str_for_write = "\"" + str_for_write

                    mid_for_write.write(str_for_write)
                    mid_file_list.clear()
                    dict_for_check_reference.clear()

                for k, v in dict_with_bool_change_marker.items():  # ПРОЕБГАЮСЬ ПО СЛОВАРЮ С ИЗЕМЕНЕНИЯМИ И ЕСЛИ БЫЛО ТО ДЕЛАЮ ФУНКЦИЮ, И ПОТОМ В ЛЮБОМ СЛУЧАЕ ОБНОВЛЯЮ ВСЕ ДО False
                    if dict_with_bool_change_marker[k] == True:
                        mif_data = replace_integer_to_char(k, mif_data)

                        dict_with_bool_change_marker[k] == False

        except NameError:
                pass

def low_to_UPP():
    with scandir(new_dir_name) as files:
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
                list_of_codes = map(lambda x: " " + x + " ", list_of_codes)
                list_of_codes = list(list_of_codes)
                new_data = mif_data

                for i in list_of_codes:
                    if mif_data.find(i) > 0 and i.find("\n") == -1:
                        new_data = new_data.replace(i, i.upper())

                read_mif = open(file.path, "w")
                read_mif.write(new_data)
                read_mif.close()


low_to_UPP()




# with scandir(new_dir_name) as files:
    #     for file in files:
    #         file_name = file.name
    #         file_name, file_extencion = file_name.split(".")
    #         if file_extencion == "mif":
    #             with open(file.path, "+r") as mif_file_data:
    #                 mif_for_chage_integer = mif_file_data.read()
    #             print(mif_for_chage_integer)



