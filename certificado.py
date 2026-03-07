from fpdf import FPDF

def generar_certificado(nombre):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial","B",16)

    pdf.cell(0,10,"CERTIFICADO MENFA",0,1,"C")

    pdf.set_font("Arial","",12)

    pdf.cell(0,10,f"Se certifica que {nombre}",0,1,"C")

    pdf.cell(0,10,"Aprobó el simulador operativo",0,1,"C")

    pdf.output("certificado.pdf")
