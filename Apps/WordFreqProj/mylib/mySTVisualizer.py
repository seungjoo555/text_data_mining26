import streamlit as st
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
from wordcloud import WordCloud

font_path = "c:/Windows/Fonts/malgun.ttf"
def visualize_barh_graph(counter, num_word):
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)
    word_list = [word for word, _ in counter.most_common(num_word)]
    count_list = [count for _, count in counter.most_common(num_word)]
    fig, ax = plt.subplots()
    ax.barh(word_list[::-1], count_list[::-1], height = 0.5)
    st.pyplot(fig)

def visualize_wordcloud(counter, num_word):
    fig, ax = plt.subplots()
    const_wc = WordCloud(font_path = font_path,
                     width= 800,
                     height= 600,
                     background_color= "ivory",
                     max_words= num_word
                     )
    const_wc = const_wc.generate_from_frequencies(counter)
    ax.imshow(const_wc)
    ax.axis(False)
    st.pyplot(fig)