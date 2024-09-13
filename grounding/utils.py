import base64
import cv2


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def visulize(image_path, xyxy=[[102, 505], [324, 860]]):
    img = cv2.imread(image_path)

    img_w, img_h = img.shape[1], img.shape[0]
    scale_w = img_w / 999
    scale_h = img_h / 999

    start_x_min = int(xyxy[0][0] * scale_w)
    start_y_min = int(xyxy[0][1] * scale_h)
    end_x_min = int(xyxy[1][0] * scale_w)
    end_y_min = int(xyxy[1][1] * scale_h)

    img = cv2.rectangle(img, (start_x_min, start_y_min), (end_x_min, end_y_min), [0, 0, 255], thickness=3)

    cv2.namedWindow('image', flags = cv2.WINDOW_NORMAL |cv2.WINDOW_KEEPRATIO |cv2.WINDOW_GUI_EXPANDED)
    cv2.imshow("image", img)

    # 等待按下任意键
    cv2.waitKey(0)

    # 关闭窗口
    cv2.destroyAllWindows()


if __name__ == "__main__":
    image_path = "image/dog_and_girl.jpeg"
    visulize(image_path=image_path)
