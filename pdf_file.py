from create_table_fpdf2 import PDF

pdf = PDF()

def table(data, file_path):
    data_ = [("Arrival date","commodity","District","Market","Max price","Min price"," Modal price", "State","Variety")]
    for i in data:
        i = list(i)
        i[4] = str(i[4])
        data_.append(i)
    pdf.add_page()
    pdf.set_font("Times", size=25)
    pdf.create_table(table_data=data_,title="Commodity Price Manager",cell_width="even")
    pdf.ln()
    pdf.output(file_path)