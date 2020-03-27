# Tutorial from https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# find a specific ID (in this case the results container menu on the left)
results = soup.find(id='ResultsContainer')
# print(results.prettify())

# each hit is its own section with class="card-content"
job_elems = results.find_all('section', class_='card-content')
# print the indivudal jobs one by one
for job_elem in job_elems:
    print(job_elem, end='\n'*2)

    # It's a lot of HTML, but there are class names on several elements, so let's dig those out:
for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    # Nones (e.g. an advert) will break the printing below, so skip the rest of that iteration
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

python_jobs = results.find_all('h2', string='Python Developer')
print(python_jobs)  # -> sadly, there are no Python Developer jobs? :/

# No, BeautifulSoup searches for that string specifically, let's try with a lambda function that converts the <h2> texts to lower
python_jobs = results.find_all('h2',
                               string=lambda text: 'python' in text.lower())
print(python_jobs)  # -> now there is one :)

# Can we dig out an attribute like e.g. the actual URL?
for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")
