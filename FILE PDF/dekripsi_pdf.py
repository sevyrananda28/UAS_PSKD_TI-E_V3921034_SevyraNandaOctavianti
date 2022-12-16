from PyPDF2 import PdfFileReader, PdfFileWriter

# buat objek pdf writer
out = PdfFileWriter()
  
# buka file pdf yg terenkripsi
file = PdfFileReader("D:/encPdf.pdf")
  
# masukkan password enkripsi 
password = "sevyra"
  
# cek file terenkripsi atau tidak 
if file.isEncrypted:
  
    # jika file terenkripsi, langsung di dekripsi pakai password 
    file.decrypt(password)
  
    # dekripsi dilakukan setiap halaman file pdf
    # simpan ke dalam file baru 
    for idx in range(file.numPages):
        
        # identifikasi halaman file 
        page = file.getPage(idx)
          
        # masukkan halaman yg sudah diidentifikasi dan sudah di dekripsi ke file baru 
        out.addPage(page)
      
    # buka file baru "myfile_decrypted.pdf"
    with open("D:/UAS_PSKD_TIE_V3921034_SevyraNandaO/decPdf.pdf", "wb") as f:
        
        # simpan file baru 
        out.write(f)
  

    print("File decrypted Successfully.")
else:
    
    print("File already decrypted.")