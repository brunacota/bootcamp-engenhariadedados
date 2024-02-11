import csv
import requests  

def read_csv_from_github(file_path):
    github_base_url = 'https://raw.githubusercontent.com/brunacota/bootcamp-engenhariadedados/main'
    full_url = github_base_url + file_path

    data = []
    try:
        response = requests.get(full_url)
        response.raise_for_status()  
        lines = response.text.split('\n')
        csv_reader = csv.reader(lines)
        for row in csv_reader:
            data.append(row)
    except Exception as e:
        print(f"Error reading CSV file from GitHub: {e}")
    
    return data

relative_file_path = '/exercicio/megasena.csv'  
csv_data = read_csv_from_github(relative_file_path)

for row in csv_data:
    print(row)