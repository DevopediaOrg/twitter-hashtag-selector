# Overview

Once a technical article is published on Devopedia, we would like to send out a tweet. Along with the tweet, we want to insert the most relevant hashtags for the topic. The popularity of a particular hashtag must also be considered along with relevance.

For example, for an article titled "Data Science", should we use `#DataScience`, `#DataScientist` or `#DataScientists`? Should we use also `#MachineLearning`? What are other related hashtags that could be used for this topic?

The goal is to get maximum number of visitors to visit the article page once we publish and tweet about it.


# Deliverables

Project must be implemented in Python3 with a modular design. Provide basic documentation and example output. Designing a nice web-based UI to show the results is optional. It's sufficient to write output to console.

Code should support the following:
* Identify phrases that are semantically similar to the main article's title. You could use ML approaches such as word2vec to solve this.
* Use Twitter API to obtain the presence/absence of hashtags based on article's title and related phrases.
* For hashtags already available on Twitter, rank them by number of followers, number of recent tweets, etc.
* An algorithm to ranking suitable hashtags.