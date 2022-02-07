###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### IMPORT
# From: https://github.com/liannewriting/YouTube-videos-public/tree/main/generate-reports-with-python-sp500
# And:  https://www.youtube.com/watch?v=H7baMf481lU

import string

import pandas as pd

from asyncore import write
from jinja2 import Environment, FileSystemLoader

from weasyprint import HTML, CSS

###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### CLASS

class superHTML_PDF():
    
    def __init__(self, pahtOutputFolder : string, HTMLOutputName : string) -> None:
        self.pahtOutputFolder = pahtOutputFolder 
        self.HTMLOutputName = HTMLOutputName

class HTML_creator(superHTML_PDF):

    def __init__(self, pahtOutputFolder : string, HTMLOutputName : string, htmlTemplateFolder : string, htmlTemplateName : string) -> None:
        super().__init__(pahtOutputFolder, HTMLOutputName)
        self.pathFolder : string
        self.pathFolder = htmlTemplateFolder + "/"
        self.env = Environment(loader=FileSystemLoader(htmlTemplateFolder))
        self.template = self.env.get_template(htmlTemplateName)

    def renderHTMLtemplate(self) -> None:
        dictionary={"Wank": [1780], "Kramer": [1985], "Alpspitze": [2628], "Zugspitze": [2962]}
        df = pd.DataFrame(data=dictionary)
        df = df.fillna(' ').T # Füllt "NaN" in Zelle
        self.html = self.template.render(
                       page_title_text='HTMLreport',
                       title_text='Picture, PandaDF, Dictionary',
                       text ='This HTML is a Report witch contains Pictures, PandaDF and Dictionarys',
                       pictureName='IMG_Example.jpg',
                       dictionary=dictionary,
                       dataFrame = df
                       )

    def creatHTMLwithTemplate(self) -> None:
        with open( self.pahtOutputFolder + self.HTMLOutputName, 'w') as f:
            f.write(self.html)

class HTML_to_PDF(superHTML_PDF):

    def __init__(self, pahtOutputFolder: string, HTMLOutputName : string, PDFOutputName : string) -> None:
        super().__init__(pahtOutputFolder, HTMLOutputName)
        self.PDFOutputName = PDFOutputName
        self.css = CSS(string='''
            @page {size: A4; margin: 1cm;} 
            th, td {border: 1px solid black;}
            ''')

    def creatPDF(self) -> None: 
        HTML(self.pahtOutputFolder + self.HTMLOutputName).write_pdf(self.pahtOutputFolder + self.PDFOutputName, stylesheets=[self.css])

###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###+++###
### TEST

HTML_obj = HTML_creator("Test_Data_HTML_PDF/", "html_report_jinja.html", "HTML_PDF_Data", "template.html")
HTML_obj.renderHTMLtemplate()
HTML_obj.creatHTMLwithTemplate()

HTMLtoPDF_obj = HTML_to_PDF("Test_Data_HTML_PDF/", "html_report_jinja.html", 'weasyprint_pdf_report.pdf')
HTMLtoPDF_obj.creatPDF()