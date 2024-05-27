import streamlit as st

def about():
    st.title("About us.")
    about_text = """
Welcome to our About page! We are a team of dreamers, thinkers, and doers dedicated to pushing the boundaries of what's possible. Our journey began in the enchanted forests of imagination, where ideas sprouted like wildflowers and dreams took flight on the wings of possibility.

With a sprinkle of curiosity and a dash of determination, we embarked on a quest to explore the uncharted territories of knowledge and creativity. Along the way, we encountered wizards of wisdom, philosophers of folly, and magicians of mischief, each offering a glimpse into the infinite tapestry of human experience.

From the lofty peaks of Mount Inspiration to the mysterious depths of the Creative Abyss, we ventured forth, fueled by a passion for discovery and a thirst for innovation. We delved into the realms of art and science, philosophy and technology, weaving together a tapestry of ideas that danced like fireflies in the night sky.

Our mission is simple yet profound: to inspire, to enlighten, and to empower. We believe that every mind is a universe waiting to be explored, every heart a beacon of possibility. So join us on this grand adventure, as we journey together into the unknown, guided by the light of curiosity and the spark of imagination.
"""
    st.write(about_text)
    st.write(".")
