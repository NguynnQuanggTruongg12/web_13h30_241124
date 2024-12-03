from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Mở camera (0 là camera mặc định, bạn có thể thay đổi nếu sử dụng camera khác)
# import cv2

camera = cv2.VideoCapture(0)  # Hoặc thay bằng đường dẫn camera IP nếu sử dụng camera IP
if not camera.isOpened():
    print("Không thể mở camera")
else:
    print("Camera đã kết nối thành công")


def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            print("Không thể đọc frame")
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    # Trả về luồng video
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    # Render trang index và truyền my_variable nếu cần
    return render_template('index.html', my_variable="Welcome to Robot-CAM")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
