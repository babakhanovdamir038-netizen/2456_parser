from .Base import BaseParser
class ArticleParser(BaseParser):
    def get_articles_data(self, category_url):
        category_soup = self.get_soup(category_url)
        content_block = category_soup.find('div', id='content-block')
        items = content_block.find_all('div', class_='sh-news')
        # print(len(items))
        result = []
        for i in items:
            title = i.find('h2', class_='sh-title').get_text()
            print(title)
            img_url = i.find('img').get('data-src')
#            print(img_u)
            date = i.find('div', class_='side-date').find('span').get_text(strip=True)
#            print(date)
            desc = i.find('div', class_='sh-text').next.get_text(strip=True)
#            print(desc)

            result.append({
                'title': title,
                'img_url': img_url,
                'date': date,
                'desc': desc
            })
        return result
