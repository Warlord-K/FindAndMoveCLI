import os
import argparse
def mover(args):
    path = args.path
    files = os.listdir(path)
    moving_files = []
    keyword = args.keyword
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(path, file), 'r') as f:
                lines = f.read()
                if lines.lower().find(keyword.lower()) != -1:
                    moving_files.append(file)
    if len(moving_files) != 0:
        print(f"Files Containing {keyword} are {moving_files}")                 
        try:
            os.mkdir(f"{path}/{keyword}", 0o666)
            print("Directory Created")
        except FileExistsError:
            print("Directory already exists")

        for file in moving_files:
            os.rename(f'{path}/{file}', f'{path}/{keyword}/{file}')
    else:
        print("No files contain the keyword: f{keyword}")
def main():
    parser = argparse.ArgumentParser(description = "Move files that contain the keyword")
    parser.add_argument('-k', '--keyword',default = None, type=str, help='Keyword to search for')
    parser.add_argument('-p', '--path',default = '.', type=str, help='Path to search in, default is current directory')
    args = parser.parse_args()
    if args.keyword is not None:
        mover(args)
    else:
        print("Keyword not provided")