{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f236cbb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import libraries \n",
    "\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import time\n",
    "import datetime\n",
    "\n",
    "import smtplib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9b531b61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "                   Funny Got Data MIS Data Systems Business Analyst T-Shirt\n",
      "                  \n",
      "\n",
      "                    $16.99\n",
      "                   \n"
     ]
    }
   ],
   "source": [
    "# Connect to Website and pull in data\n",
    "\n",
    "URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'\n",
    "\n",
    "headers = {\"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36\", \"Accept-Encoding\":\"gzip, deflate\", \"Accept\":\"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\", \"DNT\":\"1\",\"Connection\":\"close\", \"Upgrade-Insecure-Requests\":\"1\"}\n",
    "\n",
    "page = requests.get(URL, headers=headers)\n",
    "\n",
    "soup1 = BeautifulSoup(page.content, \"html.parser\")\n",
    "\n",
    "soup2 = BeautifulSoup(soup1.prettify(), \"html.parser\")\n",
    "\n",
    "title = soup2.find(id='productTitle').get_text()\n",
    "\n",
    "price = soup2.find(id='priceblock_ourprice').get_text()\n",
    "\n",
    "\n",
    "print(title)\n",
    "print(price)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b6f7d66e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Funny Got Data MIS Data Systems Business Analyst T-Shirt\n",
      "16.99\n"
     ]
    }
   ],
   "source": [
    "# Clean up the data a little bit\n",
    "\n",
    "price = price.strip()[1:]\n",
    "title = title.strip()\n",
    "\n",
    "print(title)\n",
    "print(price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4f021c23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2021-08-21\n"
     ]
    }
   ],
   "source": [
    "# Create a Timestamp for your output to track when data was collected\n",
    "\n",
    "import datetime\n",
    "\n",
    "today = datetime.date.today()\n",
    "\n",
    "print(today)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "14d703ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create CSV and write headers and data into the file\n",
    "\n",
    "import csv \n",
    "\n",
    "header = ['Title', 'Price', 'Date']\n",
    "data = [title, price, today]\n",
    "\n",
    "\n",
    "with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:\n",
    "    writer = csv.writer(f)\n",
    "    writer.writerow(header)\n",
    "    writer.writerow(data)\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d07eeb86",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(r'C:\\Users\\alexf\\AmazonWebScraperDataset.csv')\n",
    "\n",
    "print(df)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "6b05c1eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Now we are appending data to the csv\n",
    "\n",
    "with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:\n",
    "    writer = csv.writer(f)\n",
    "    writer.writerow(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "8e95b9e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Combine all of the above code into one function\n",
    "\n",
    "\n",
    "def check_price():\n",
    "    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'\n",
    "\n",
    "    headers = {\"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36\", \"Accept-Encoding\":\"gzip, deflate\", \"Accept\":\"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\", \"DNT\":\"1\",\"Connection\":\"close\", \"Upgrade-Insecure-Requests\":\"1\"}\n",
    "\n",
    "    page = requests.get(URL, headers=headers)\n",
    "\n",
    "    soup1 = BeautifulSoup(page.content, \"html.parser\")\n",
    "\n",
    "    soup2 = BeautifulSoup(soup1.prettify(), \"html.parser\")\n",
    "\n",
    "    title = soup2.find(id='productTitle').get_text()\n",
    "\n",
    "    price = soup2.find(id='priceblock_ourprice').get_text()\n",
    "\n",
    "    price = price.strip()[1:]\n",
    "    title = title.strip()\n",
    "\n",
    "    import datetime\n",
    "\n",
    "    today = datetime.date.today()\n",
    "    \n",
    "    import csv \n",
    "\n",
    "    header = ['Title', 'Price', 'Date']\n",
    "    data = [title, price, today]\n",
    "\n",
    "    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:\n",
    "        writer = csv.writer(f)\n",
    "        writer.writerow(data)\n",
    " \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c72f2c4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Runs check_price after a set time and inputs data into your CSV\n",
    "\n",
    "while(True):\n",
    "    check_price()\n",
    "    time.sleep(86400)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00af7126",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(r'C:\\Users\\alexf\\AmazonWebScraperDataset.csv')\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d14fce5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it\n",
    "# out with this script\n",
    "\n",
    "def send_mail():\n",
    "    server = smtplib.SMTP_SSL('smtp.gmail.com',465)\n",
    "    server.ehlo()\n",
    "    #server.starttls()\n",
    "    server.ehlo()\n",
    "    server.login('AlexTheAnalyst95@gmail.com','xxxxxxxxxxxxxx')\n",
    "    \n",
    "    subject = \"The Shirt you want is below $15! Now is your chance to buy!\"\n",
    "    body = \"Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3\"\n",
    "   \n",
    "    msg = f\"Subject: {subject}\\n\\n{body}\"\n",
    "    \n",
    "    server.sendmail(\n",
    "        'AlexTheAnalyst95@gmail.com',\n",
    "        msg\n",
    "     \n",
    "    )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
