import requests

from line_reader import read_content

current_book_id = 0
def crawler():
    global current_book_id

    downloaded_book = 0
    while downloaded_book <5:
        url = f"https://www.gutenberg.org/cache/epub/{current_book_id}/pg{current_book_id}.txt"

        response = requests.get(url)
        title = read_content(response.text)

        if response.status_code == 200:
            download_path = r"C:\Users\aadel\Desktop\GCID\Tercero\BD\Task1\Datalake"
            file_name = f"book_{title}.txt"
            full_path = f"{download_path}\\{file_name}"

            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(response.text)

            print(f"El libro {title} ha sido descargado exitosamente en {full_path}.")

            downloaded_book += 1
        current_book_id +=1

