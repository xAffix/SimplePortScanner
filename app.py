from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_ports():
    target_host = request.form['target_host']
    start_port = int(request.form['start_port'])
    end_port = int(request.form['end_port'])

    total_ports = end_port - start_port + 1
    scanned_ports = 0
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        sock.close()

        scanned_ports += 1
        progress_percentage = (scanned_ports / total_ports) * 100

        if result == 0:
            open_ports.append(port)

    if not open_ports:
        result_message = "No open ports found."
    else:
        result_message = f"Open ports: {', '.join(map(str, open_ports))}"

    return render_template('result.html', result_message=result_message)

if __name__ == '__main__':
    app.run(debug=True)
