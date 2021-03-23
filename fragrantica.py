from bs4 import BeautifulSoup
import requests
import time

companies = {"Jo-Malone": ["154",
"Grapefruit",
"Nectarine Blossom & Honey",
"Dark Amber Ginger Lily",
"Lime Basil Mandarin",
"Red Roses",
"Mayrrh Tonka",
"Mimosa Cardamom",
"Basil Neroli",
"Vetiver Golden Varilla",
"Velvet Rose Oud",
"Blackberry Bay",
"Amber Lavender",
"Earlgrey Cucumber",
"Oud Bergamot",
"Orange Blossom",
"Wild Bluebell",
"Wood Sage Sea Salt",
"English Oak Hazelnut",
"English Pear Fressia",
"Tuberose Angelica",
"Pomegranate Noir",
"Poppy Barley",
"Peony Blushsuede",
"Honeysuckle Davana"
]}
#https://www.fragrantica.com/perfume/Calvin-Klein/CK-One-276.html
#https://www.fragrantica.com/perfume/Jo-Malone-London/154-Cologne-17819.html
def main():
    file = open("jomalone.txt", "w")

    names = companies.keys()
    for name in names:
        url = "https://www.fragrantica.com/designers/"+name+".html"
        headers = {'User-Agent': 'Mozilla/5.0'}
        # print(url)
        response = requests.get(url, headers=headers).text
        # print(response.encoding)
        # html = response.content.decode('utf-8').strip('\n')
        soup = BeautifulSoup(response, "html.parser")
        # print(soup)
        text = soup.select(".flex-child-auto a")
        count = 0
        for t in text:
            t_url = "https://www.fragrantica.com"+t["href"]
            t_name = " ".join(t_url.replace('/','.').split('.')[-2].split("-")[:-1])
            # print(t_name)
            if t_name in companies[name]:
                print(t_name)
                count += 1
                t_response = requests.get(t_url, headers=headers)
                t_html = t_response.content.decode('utf-8').strip('\n')
                t_soup = BeautifulSoup(t_html, "html.parser")
                # print(t_soup)
                graphs = t_soup.select(".grid-x .accord-bar")
                # print(graph)
                for g in graphs:
                    graph = " ".join([g.text, g["style"].split("width: ")[-1].split("%")[0]]) + "\n"
                    print(graph)
                    file.write(graph)

                #main-content > div.grid-x.grid-margin-x > div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div > div:nth-child(1) > div.show-for-medium > span
                # moods = t_soup.select(".grid-x .show-for-medium")
                # moods = t_soup.select("div.grid-x,grid-margin-x div.cell.small-6 .vote-button-legend")
                # votes = t_soup.select(".grid-x .voting-small-chart-size > div > div")
                # print(moods)
                # print(votes)
                # for index in range(len(moods)):
                #     moodvote = " ".join([moods[index].text, votes[index]["style"]]) + "\n"
                #     print(moodvote)
                #     file.write(moodvote)
                top_note = t_soup.select("#pyramid > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(4) > div > div:nth-child(1) > div:nth-child(2)")
                print(top_note)

                time.sleep(5)
    file.close()

            



if __name__ == "__main__":
    main()