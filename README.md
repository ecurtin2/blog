# Blog

My blog which contains some posts and recipes, made using [hugo](https://gohugo.io/)

To add markdown posts, just copy/paste an existing directory structure from `/content/blog` or `/content/recipes` and write away. For jupyter notebook posts, you can write a new notebook in `notebooks/`, the hugo frontmatter in yaml format (see other examples there), and `use the convert-notebooks.py` script to generate hugo compatible markdown file. Easiest way to do this is to use `docker-compose build generate && docker-compose run generate`. 
