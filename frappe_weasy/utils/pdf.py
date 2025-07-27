from weasyprint import HTML
import frappe
from weasyprint import HTML
from frappe import _



def generate_pdf(html_string):
    print("usint the weasyprint method")
    return HTML(string=html_string).write_pdf()

@frappe.whitelist()
def download_pdf(doctype, name, format=None, doc=None, no_letterhead=0):
    html = frappe.get_print(doctype, name, print_format=format, doc=doc, no_letterhead=no_letterhead)
    
    from weasyprint import HTML
    pdf = HTML(string=html).write_pdf()

    frappe.local.response.filename = f"{name}.pdf"
    frappe.local.response.filecontent = pdf
    frappe.local.response.type = "pdf"    

