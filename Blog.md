---
layout: page
title: Blog
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

      <!--<a href="{{ post.url }}" class="read-more">Read the full post</a> -->
    </article>
  {% endfor %}
</div>
