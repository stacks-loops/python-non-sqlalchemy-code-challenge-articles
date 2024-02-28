import ipdb

class Article:
    all = []

    def __init__(self, author, magazine, title="placeholder"):
        self.author = author
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
        
class Author:
    def __init__(self, name="placeholder"):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __setattr__(self, attr, value):
        if attr == "name" and hasattr(self, attr):
            raise AttributeError("Cannot change the value of 'name'")
        else:
            super().__setattr__(attr, value)


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
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass