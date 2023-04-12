from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def print_pdf():
    # Check if a file was uploaded
    if 'pdf' not in request.files:
        return 'No PDF file found', 400

    # Get the uploaded PDF file
    pdf_file = request.files['pdf']
    file_name = request.form.get('filename')
    # Check if a queue name was provided
    queue_name = request.form.get('queue_name')
    if not queue_name:
        return 'No queue name provided', 400

    if not file_name:
        return 'No filename provided', 400

    # Save the PDF file to disk
    #pdf_file.save('uploads/' + file_name)
    #pdf_file.save('uploads' + pdf_file.filename)
    pdf_file.save(os.path.join('/home/nshiroma/printrcubes/uploads/', os.path.basename(pdf_file.filename)))
    # Print the PDF file to the specified queue
    #os.system('lp -d ' + queue_name + ' uploads/' + file_name)
    os.system('lp -d ' + queue_name + ' /home/nshiroma/printrcubes/uploads/' + os.path.basename(pdf_file.filename))
    return 'PDF file printed to ' + queue_name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
