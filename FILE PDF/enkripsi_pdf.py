from PyPDF2 import PdfFileReader, PdfFileWriter

# buat objek pdf writer
out = PdfFileWriter()
  
# buka file pdf asli 
file = PdfFileReader("D:/file_pdf.pdf")
  
# identifikasi total halaman file
num = file.numPages
  
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for idx in range(num):
    
   
    page = file.getPage(idx)
      

    out.addPage(page)
  
  
# masukkan password enkripsi 
password = "sevyra"
  
# enkripsi masing-masing halaman 
out.encrypt(password)
  
# buka file enkripsi "myfile_encrypted.pdf"
with open("D:/UAS_PSKD_TIE_V3921034_SevyraNandaO/encPdf.pdf", "wb") as f:
    
    # simpan pdf 
    out.write(f)

