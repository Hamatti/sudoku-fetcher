# A simple downloader to retrieve printable sudokus in pdf format
# so that I can later combine them into one pdf and export that
# into my reMarkable

# @author Juha-Matti Santala / https://hamatti.org
# @license MIT


import urllib.request as request

difficulties = ['Easy', 'Medium', 'Hard']
ranges = [
    range(1, 21),
    range(1, 18),
    range(1, 21)
]

for difficulty, nums in zip(difficulties, ranges):
    for number in nums:
        filename = f'{difficulty}Sudoku{number:03d}.pdf'
        url = f'http://www.printablesudoku99.com/pdf/{filename}'
        print(f'Downloading from {url}')
        request.urlretrieve(url, f'./{filename}')
