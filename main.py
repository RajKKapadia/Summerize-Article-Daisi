from transformers import pipeline
import streamlit as st

summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

min_length = 30

def get_article_summary(article: str) -> dict:
    ''' Get the article summary.\n
        This function will provide a summary of an article/text, it uses "facebook/bart-large-cnn"
        to generate the summary.\n

        Parameters:
        - article (string): this is the article that will be summerized\n
        
        Return:
        - this function will return a dict, it will have the following keys:\n
            status - 1 for success, 0 for error, -1 for any input error\n
            message - message\n
            summary_text - None for error, otherwise string
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