import os
import re
from pathlib import Path
import comtypes.client
from PyPDF2 import PdfMerger
from tqdm import tqdm

def docx_to_pdf(docx_path, pdf_path):
    """Convierte un archivo DOCX a PDF usando Microsoft Word (más preciso)."""
    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(str(docx_path))
        doc.SaveAs(str(pdf_path), FileFormat=17)  # 17 = wdFormatPDF
        doc.Close()
    except Exception as e:
        print(f"Error convirtiendo {docx_path}: {e}")
    finally:
        word.Quit()

def natural_sort_key(file):
    """Extrae números de los nombres de archivos para ordenarlos correctamente."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', file.stem)]

def merge_pdfs(pdf_folder, output_filename):
    """Une todos los PDFs en un solo archivo con orden numérico correcto."""
    merger = PdfMerger()
    pdf_files = sorted(Path(pdf_folder).glob("*.pdf"), key=natural_sort_key)
    
    print("\n🔄 Uniendo PDFs...")
    for pdf in tqdm(pdf_files, desc="Procesando PDFs", unit="archivo"):
        merger.append(str(pdf))
    
    merger.write(output_filename)
    merger.close()

def main():
    user_name = input("Introduce el nombre de la carpeta del usuario del equipo: ")
    input_folder = input("Introduce la carpeta con los archivos DOCX: ")
    output_pdf_name = input("Introduce el nombre del PDF final (sin extensión): ")
    full_input_path = os.path.join("C:\\Users", user_name, "Desktop", input_folder)
    output_folder = os.path.join(full_input_path, "pdf_output")
    os.makedirs(output_folder, exist_ok=True)
    
    docx_files = list(Path(full_input_path).glob("*.docx"))

    # Convertir DOCX a PDF
    print("\n🔄 Convirtiendo DOCX a PDF...")
    for docx_file in tqdm(docx_files, desc="Procesando DOCX", unit="archivo"):
        pdf_path = os.path.join(output_folder, docx_file.stem + ".pdf")
        docx_to_pdf(docx_file, pdf_path)
    
    # Unir los PDFs
    merged_pdf_path = os.path.join(full_input_path, f"{output_pdf_name}.pdf")
    merge_pdfs(output_folder, merged_pdf_path)
    
    print(f"\n✅ Conversión y unión completadas. Archivo final: {merged_pdf_path}")

if __name__ == "__main__":
    main()
