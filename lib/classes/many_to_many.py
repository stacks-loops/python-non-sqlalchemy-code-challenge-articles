import ipdb

class Article:
    all = []

    def __init__(self, author, magazine, title="placeholder"):
        self._author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new_title):
        if type(new_title) == str and 5 <= len(new_title) <= 50:
            self._title = new_title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
          if isinstance(author, Author):
              self._author = author

        
class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name != "" and hasattr(self, 'name'):
            self._name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass