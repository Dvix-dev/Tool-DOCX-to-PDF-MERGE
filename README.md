# 📄 DOCX to PDF + MERGE TOOL
Un script en Python que convierte archivos **.docx** en **.pdf** y luego los une en un único documento.  

## 🚀 Características  
✅ Convierte **todos los archivos DOCX** de una carpeta a PDF.  
✅ Usa **Microsoft Word** para la conversión.  
✅ **Une todos los PDFs** generados en un único archivo final.   

---

## 🔧 Instalación  
### 1️⃣ **Clonar el repositorio**  
```sh
git clone https://github.com/Dvix-dev/tool-docx-to-pdf-merge.git
cd tool-docx-to-pdf-merge
```

### 2️⃣ Crear un entorno virtual (opcional)
```sh
python -m venv .venv
source .venv/bin/activate  # En Linux/macOS
.venv\Scripts\activate  # En Windows
```

### 3️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```

> [!IMPORTANT]  
> Este script usa Word para convertir DOCX a PDF.
> Si no tienes Microsoft Office instalado, no funcionará.

## 🛠 Uso
### Ejecuta el script en una terminal con:
```sh
python DOCX_to_PDF_MERGE.py
```

### ✨ Pasos interactivos dentro del script
1️⃣ Introduce el nombre del usuario del equipo.<br>
2️⃣ Especifica la carpeta con los archivos DOCX.<br>
3️⃣ El script convertirá los archivos DOCX → PDF y los guardará en pdf_output/.<br>
4️⃣ Introduce el nombre del PDF final.<br>
5️⃣ Se generará el archivo combinado en la misma carpeta.

> [!IMPORTANT]  
> Asegurate de que la carpeta que contenga los archivos DOCX se encuentre en el escritorio.

## 📂 Estructura del proyecto
```sh
📂 tool-docx-to-pdf-merge/
 ├── 📄 TOOL_DOCX_to_PDF_MERGE.py   # Script principal
 ├── 📄 README.md                   # Documentación
 ├── 📄 requirements.txt            # Dependencias
```

## 📜 Licencia
Este proyecto está bajo la licencia MIT. ¡Puedes usarlo y modificarlo libremente!

## 🫂 Contribuciones
Si tienes alguna sugerencia, mejora o te ha surgido un problema, ¡haz un pull request o abre un issue en GitHub! 😁