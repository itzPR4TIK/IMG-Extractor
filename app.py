import io
import zipfile
from flask import Flask, render_template, request, send_file
import fitz  # PyMuPDF

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB max upload

def pdf_bytes_to_png(pdf_bytes, dpi=200):
    """Convert a PDF (as bytes) to a list of (filename, image_bytes) for each page."""
    images = []
    # fitz.open can read directly from bytes
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(dpi=dpi)
        img_bytes = pix.tobytes("png")
        filename = f"page_{page_num+1:04d}.png"
        images.append((filename, img_bytes))
    doc.close()
    return images

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            return "No file part", 400

        file = request.files['pdf_file']
        if file.filename == '':
            return "No selected file", 400

        if file and file.filename.lower().endswith('.pdf'):
            # Read the whole PDF into memory (no disk write)
            pdf_bytes = file.read()

            try:
                images = pdf_bytes_to_png(pdf_bytes, dpi=200)
            except Exception as e:
                return f"Error processing PDF: {e}", 500

            # Create ZIP in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
                for fname, img_bytes in images:
                    zf.writestr(fname, img_bytes)
            zip_buffer.seek(0)

            # Send ZIP as download
            download_name = f"{file.filename.rsplit('.', 1)[0]}_images.zip"
            return send_file(
                zip_buffer,
                mimetype='application/zip',
                as_attachment=True,
                download_name=download_name
            )
        else:
            return "Please upload a PDF file.", 400

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)