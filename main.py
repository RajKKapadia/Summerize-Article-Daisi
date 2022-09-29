from transformers import pipeline
import streamlit as st

summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

min_length = 30

def get_article_summary(article: str) -> dict:
    '''
    Get the article summary in minimum word, this function will provide a summary of an article/text, 
    it uses "facebook/bart-large-cnn" to generate the summary. This function will take an article/text as an input. 
    The output of this function will be an object and it will have three things, the status of the response, 
    either 0 or 1, message about the response, and last the summary text.

    :param article(str): this is the article that will be summerized
    
    :return object: Result of the Bert model
    '''
    try:
        words = article.split(' ')
        if len(words) < min_length:
            return {
                'status': -1,
                'message': f'Article length is too small. It must have than {min_length} words in it.',
                'summary_text': None
            }
        summary = summarizer(article, max_length=len(words), min_length=min_length, do_sample=False)
        return {
                'status': 1,
                'message': 'Success.',
                'summary_text': summary[0]['summary_text']
            }
    except:
        return {
            'status': 0,
            'message': 'We are facing an issue.',
            'summary_text': None
        }

def st_ui():
    ''' Function to render the Streamlit UI.
    '''
    st.title('Summerize Article')
    article = st.text_area('Paste you article here...', '')
    button = st.button('Summerize...')
    if button:
        result = get_article_summary(article=article)
        st.write('This is the summary.')
        st.json(result)

if __name__ == '__main__':
    st_ui()