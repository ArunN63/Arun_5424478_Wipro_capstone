from openpyxl import load_workbook


def get_test_data():

    workbook = load_workbook("testdata/test_data.xlsx")
    sheet = workbook.active
    data = {"mobile":sheet["A2"].value,"condition_index":sheet["B2"].value,"location":sheet["C2"].value}
    return data