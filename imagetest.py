import time

import cv2
import easyocr
import pytesseract
from PIL import Image, ImageFile

# путь к исполняемому файлу tesseract
pytesseract.pytesseract.tesseract_cmd = r"D:/Tesseract/tesseract.exe"
# распозавание с помощью pytesseract, открытие картинки PIL.Image
def teseract_recognition(img: ImageFile, psm: int):
    return pytesseract.image_to_string(img, lang='rus', config=r'--oem 3 --psm '+str(psm))
# сохранение текста в текстовый файл
def save_text(text, name):
    print(text)
    with open(f'{name}.txt', 'w', encoding='utf-8') as file:
        file.write(text)
    print(f'[+] Распознанный текст сохранен в файл: "{name}.txt"')
    return
def crop_image(team: int, position: int, image: ImageFile) -> ImageFile:
    yourImage = image
    target = [[315, 213], [1520, 218]]
    height = [17, 26]
    box = position
    #---------------
    image = yourImage.crop((target[team][0], target[team][1] + box * 100, target[team][0] + 135,
                    target[team][1] + box * 100 + height[team]))
    timestamp = str(time.time())
    image.save("cropped.png")
    image.save("cropped/"+timestamp+".png")
    image = cv2.imread("cropped/"+timestamp+".png", cv2.IMREAD_GRAYSCALE)
    #---------------
    return image
def optimize_image(img: ImageFile) -> ImageFile:
    image = cv2.imread("cropped.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    invert = 255 - thresh
    return invert

def get_full_team(which_team: int, img: str) -> str:
    for i in range(5):
        yourImage = Image.open(img)
        cropped = crop_image(which_team, i, yourImage)
        optimized = optimize_image(cropped)
        if which_team:

            text = teseract_recognition(optimized, 8)
            if "выбор" in text.lower() or "выбирает" in text.lower() or "следующий" in text.lower():
                break

            # print(str(i + 1) + ") Персонаж: " + split[0].lower())
            # print(text.split())
            print(str(i + 1) + ") " + text.lower())
            #for x in heroes:
                #if x.lower() in text.lower():
                    #print(x.lower())
        else:

            text = teseract_recognition(cropped, 8)
            if "выбор" in text or "выбирает" in text.lower() or "следующий" in text.lower():
                break
            split = text.split()

            # print(str(i + 1) + ") Персонаж: " + split[0].lower() + ", Роль: " + split[1].lower() + ", Ник: " + split[2])
            print(str(i + 1) + ") " + split[0].lower())
        #print(str(i+1) + ") Персонаж: " + split[0] + ", Роль: " + split[1] + ", Ник: " + split[2])
        #print(text.split())
        #save_text(text, os.path.split(path_img)[1].split(".")[0])

# ввод данных и выбор библиотеки для распознавания
def main():
    print("Твоя команда:")
    get_full_team(0, "screen3.png")
    print("Команда противника:")
    get_full_team(1, "screen3.png")
    print("\n")
    print("Твоя команда:")
    get_full_team(0, "screen4.png")
    print("Команда противника:")
    get_full_team(1, "screen4.png")


if __name__ == "__main__":
    main()

