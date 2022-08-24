# Summerize Article

This Daisi is a simple application that will summarize your article in the minimum possible words. This application uses the state-of-the-art NLP technology by Facebook with the help of HuggingFace🤗 and Transformers.

The technology I have used are:
* [Transformers](https://github.com/huggingface/transformers)
* [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)

```python
import pydaisi as pyd

summerize_article = pyd.Daisi('rajkkapadia/Summerize Article')
article = '''This is a sample article for the Daisi. The summary of this article is generated using Facebook's BERT Large CNN model. The Daisi is developed using Hugging Face.'''
result = summerize_article.get_article_summary(article).value

print(result)
```