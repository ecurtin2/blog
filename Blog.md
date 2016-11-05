---
layout: page
---

<div class="posts">
  {% for post in site.posts %}
    <article class="post">

      <h1><a href="{{ post.url }}">{{ post.title }}</a></h1>
      <div class="date">
        {{ post.date | date: "%B %e, %Y" }}
        <br>
        <br>
      </div>

      <div class="entry">
        {{ post.excerpt }}
      </div>

    </article>
  {% endfor %}
</div>
