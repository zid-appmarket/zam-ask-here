---
# Synced from https://docs.zid.sa/questions-jinja-1914528m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-questions-jinja
title: "questions.jinja"
product: theme_market
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/questions-jinja-1914528m0
tags: [from-docs-site, partner-docs]
language: en
---

> questions.jinja - Zid Docs
# questions.jinja

**Route:** `/products/{slug}/questions`

**Path Operation:** `product_questions`

## Variables #

Variable Type

`product` Product

`questions` QuestionList

`store` Store

`session` Session

## Question Properties #

Property Description

`question.question` Question text

`question.name` Asker name

`question.is_anonymous` Anonymous flag

`question.answers` List of answers

## Example #

```
`{% extends "layout.jinja" %}

{% block main_content %}
<h1>{{ product.name }} - {{ _("Questions") }}</h1>

{% for question in product.questions.results %}
<div class="question">
{% if not question.is_anonymous %}
<strong>{{ question.name }}</strong>
{% endif %}
<p>{{ question.question }}</p>

{% if question.answers %}
<div class="answer">
{{ question.answers[0].answer }}
</div>
{% endif %}
</div>
{% endfor %}
{% endblock %}`
```

Modified at 2026-07-30 11:49:13

Previous

reviews.jinja

Next

shipping_payment.jinja
