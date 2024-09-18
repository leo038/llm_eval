import base64
import cv2


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def visulize(image_path, xyxy=[[243, 416], [509, 860]]):
    xyxy_list = [[[102, 505], [324, 860]],
    [[236, 405], [506, 853]],
    [[224, 427], [534, 842]],
    [[243, 416], [509, 860]]]
    img = cv2.imread(image_path)

    img_w, img_h = img.shape[1], img.shape[0]
    scale_w = img_w / 999  ## 注意yi-vision模型的输出 需要用缩放因子999 进行处理  https://github.com/01-ai/Yi/issues/376
    scale_h = img_h / 999
    # scale_w, scale_h = 1, 1

    for xyxy in xyxy_list:
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

    cv2.imwrite("./result/yi_vision.jpg", img)


if __name__ == "__main__":
    image_path = "image/dog_and_girl.jpeg"
    visulize(image_path=image_path)
