import os
from subprocess import call, STDOUT

class Block():
    
    def __init__(self, file_name = 'latex.tex'):
        self.file_name = 'tmp/' + file_name
        self.content = ''
    
    
    def add_text(self, text):

        beginning = r"""
        \documentclass[a4paper]{article}
        \begin{document}
                    """

        end = """
        \end{document}
              """
        
        self.content = beginning + self.content + text + end
    
    
    def render_latex(self):
                
        with open(self.file_name, 'w') as f:
            f.write(self.content)
            f.close()
    
    
    def convert_pdf(self):
        
        self.render_latex()

        cmd = ["pdflatex",
              "-interaction=nonstopmode",
              "-file-line-error",
              ]

        if os.path.dirname(self.file_name):
            cmd += ['-output-directory', os.path.dirname(self.file_name)]

        cmd += ["-halt-on-error", self.file_name]
        
        call(cmd, stderr=STDOUT)
        
    
    def show(self, size = (600,500)):
        return PDF(self.file_name.replace('.tex', '.pdf'), size)
    
    
class PDF(object):
  def __init__(self, pdf, size=(200,200)):
    self.pdf = pdf
    self.size = size

  def _repr_html_(self):
    return '<iframe src={0} width={1[0]} height={1[1]}></iframe>'.format(self.pdf, self.size)

  def _repr_latex_(self):
    return r'\includegraphics[width=1.0\textwidth]{{{0}}}'.format(self.pdf)