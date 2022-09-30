# Summerize Article

This Daisi is a simple application that will summarize your article in the minimum possible words. This application uses the state-of-the-art NLP technology by Facebook with the help of HuggingFace🤗 and Transformers.

The technology I have used are:
* [Transformers](https://github.com/huggingface/transformers)
* [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)

```python
import pydaisi as pyd

summerize_article = pyd.Daisi('rajkkapadia/Summerize Article')
article = '''The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'''
result = summerize_article.get_article_summary(article).value

print(result)
```