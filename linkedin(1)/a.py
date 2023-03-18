# # a='hrudayesh'
# # l='guntur'
# # # with open('dat.txt','w') as mfile:
# # #     mfile.write(f'my name is {a}\nmy location is {l}')
# # with open('dat.txt','r') as file:
# #     l=file.readlines()
# #     for i in l:
# #         with open('sample.txt','a') as res:
# #             res.write(i)

# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import docx2txt as dt
# import textract
# resume = textract.process("E:\competitve\pythonpractise\linkedin\input.docx")
# job_desc = textract.process("E:\competitve\pythonpractise\linkedin\descript.docx")

# # resume=dt.process('input.docx')
# # MY_TEXT = dt.process("test.docx")
# # job_desc=dt.process('descript.docx')

# # with open('input.txt','r') as mfile:
# #     resume=mfile.readlines()
# # with open('descript.txt','r') as mfile:
# #     job_desc=mfile.readlines()
# text=[resume,job_desc]
# cv=CountVectorizer()
# count_matrix=cv.fit_transform(text)

# match_res=cosine_similarity(count_matrix)
# print(match_res)

# match=(match_res[0][1])*100
# match_final=round(match,2)
# print(match_final)


with open('input.docx','r') as mfile:
    res=mfile.readlines()
    with open('descript.docx','a') as file:
        for line in res:
            file.write(line)


# Python program to convert
# text file to pdf file


# from fpdf import FPDF
# # save FPDF() class into
# # a variable pdf
# pdf = FPDF()

# # Add a page
# pdf.add_page()

# # set style and size of font
# # that you want in the pdf
# pdf.set_font("Times", size = 12)
# # open the text file in read mode
# f = open("ouputresults.txt", "r")

# # insert the texts in pdf
# for x in f:
# 	pdf.cell(185, 10, txt = x, ln = 1, align = 'C')

# # save the pdf with name .pdf
# pdf.output("mygfg.pdf")
