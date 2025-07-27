__version__ = "0.0.1"

import frappe.utils.pdf
from frappe_weasy.utils import pdf as weasy_pdf

frappe.utils.pdf.get_pdf_from_html = weasy_pdf.generate_pdf
