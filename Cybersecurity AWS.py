import requests
import csv
import json


# Set up the URL and API key
url = "https://li-data-scraper.p.rapidapi.com/company-jobs"
payload = {
    "companyIds": [5383240, 2382910],  # Modify companyIds as necessary
    "page": 1
}
headers = {
    "x-rapidapi-key": "245a0ba893mshf624aad12713292p16050bjsn9403d0ec437d",
    "x-rapidapi-host": "li-data-scraper.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Parse the response
if response.status_code == 200:
    job_data = response.json()['data']['items']
    
    # Save data to CSV
    csv_file = "job_data.csv"
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "URL", "Company", "Location", "Type", "Post Date", "Benefits"])
        for job in job_data:
            writer.writerow([
                job.get('id', ''),
                job.get('title', ''),
                job.get('url', ''),
                job.get('company', {}).get('name', ''),
                job.get('location', ''),
                job.get('type', ''),
                job.get('postAt', ''),
                job.get('benefits', '')
            ])
    print(f"Data saved to {csv_file}")
    
    # Save data to JSON
    json_file = "job_data.json"
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(job_data, file, ensure_ascii=False, indent=4)
    print(f"Data saved to {json_file}")

else:
    print(f"Failed to retrieve data: {response.status_code}, {response.text}")
