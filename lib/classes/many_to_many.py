import ipdb

class Article:
    all = []

    def __init__(self, author, magazine, title="placeholder"):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if type(new_title) == str and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            print("Title is not valid")

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
          if isinstance(author, Author):
              self._author = author
          else:
              print("Author is not valid")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
          if isinstance(magazine, Magazine):
              self._magazine = magazine

        
class Author:
    def __init__(self, name):
        self._name = name
        self._name_assigned = True

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name != "" and not hasattr(self, 'name'):
            self._name = name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    def add_article(self, magazine, title):
      new_article = Article(self, magazine, title)
      return new_article

    def magazines(self):
        return {magazine for magazine in Article.all if magazine.author == self}
    def add_magazine(self, magazine):
        return [self, magazine]

    def topic_areas(self):
        if self.articles():
            return list(set(article.magazine.category for article in self.articles()))
        else:
            return None
class Magazine:
    all = {}

    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and category != "":
            self._category = category

    def articles(self):
        return [article for article in Article.all if article._magazine == self]

    def contributors(self):
        return [article._author for article in Article.all if article._magazine == self]

    def article_titles(self):
        if self.articles():
            return [article.title for article in self.articles()]
        else:
            return None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            if isinstance(article.author, Author):
                if article.author in author_count:
                    author_count[article.author] += 1
                else:
                    author_count[article.author] =1
        contributing_authors =[author for author, count in author_count.items() if count > 2]        
        
        if contributing_authors:
            return contributing_authors
        else:
            return None