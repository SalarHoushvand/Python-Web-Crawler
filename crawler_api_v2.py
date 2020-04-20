import webbrowser
from flask import Flask, render_template
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# defining Flask and html folder
app = Flask(__name__, template_folder='templates')


# First page
@app.route("/")
def first_page():
    return render_template("index.html")


@app.route("/def")
def crawler():
    my_url = "https://www.newegg.com/PS4-Video-Games/SubCategory/ID-3141"

    u_client = uReq(my_url)
    page_html = u_client.read()
    u_client.close()

    prices = []
    titles = []

    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("div", {"class": "item-container"})
    print(len(containers))

    for i in range(0, len(containers)):
        container = containers[i]

        # get product details
        title_container = container.findAll("a", {"class": "item-title"})
        title = title_container[0].text
        titles.append(title)

        # find price
        try:
            price_list = container.findAll("li", {"class": "price-current"})
            price1 = price_list[0].strong.text
            price2 = price_list[0].sup.text
            price_total = price1 + price2
            prices.append(price_total)
            pricess = ' '.join(prices)
            titless = ' '.join(titles)
            titless = titless.replace(',', '')
            titless = titless.replace('-', '')
            titless = titless.replace(' - PlayStation 4', ',')
            titless = titless.replace('PlayStation 4', ',')
            titless = titless.replace('PlayStation', ',')
            titless = titless.replace('PS4', ',')
            titless = titless.replace('Final Fantasy XII: The Zodiac Age  , ', '')

        except:
            print('An error occurred')

    return render_template("def.html", price=pricess, title=titless, )


@app.route("/about-team")
def aboutteam():
    return render_template("about-tem.html")


@app.route("/about-application")
def aboutapp():
    return render_template("about-application.html")


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000'
    webbrowser.open_new(url)
    app.run()
