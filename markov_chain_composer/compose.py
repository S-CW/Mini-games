import string, random, re, os
from graph import Graph, Vertex


def get_words_from_text(text_path):
    with open(text_path, 'r', encoding="utf8") as f:
        text = f.read()

        # remove [text in here]
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split())   # replaces tab, enter, indent to space
        text.lower()
        text = text.translate(str.maketrans('','', string.punctuation))    # remove punctuation like !'.

    words = text.split()
    return words
        
def make_graph(words):
    g = Graph()

    previous_word = None

    # for each word
    for word in words:
    # check that word is in the graph, and if not then add it
        word_vertex = g.get_vertex(word)
    # if there was a previous word, then add an edge if it does not already exist
    # in the graph, otherwise increment weight by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)

    # set the word to the previous word and iterate
        previous_word = word_vertex

    # generate the probability mappings before composing
    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # self.vertices[value]
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition
        

def main(artist):
    # step 1: get words from texts
    # words = get_words_from_text('markov_chain_composer/texts/hp_sorcerer_stone.txt')

    # for song lyrics
    words = []
    for song_file in os.listdir(f'markov_chain_composer/songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'markov_chain_composer/songs/{artist}/{song_file}')
        words.extend(song_words)

    # step2: make a graph using those words
    g = make_graph(words)
    # step 3: get the next word for x number of words (defined by user)
    # step 4: show the user!
    composition = compose(g, words, 100)
    return ' '.join(composition) # returns a string

if __name__ == '__main__':
    print(main('taylor_swift'))