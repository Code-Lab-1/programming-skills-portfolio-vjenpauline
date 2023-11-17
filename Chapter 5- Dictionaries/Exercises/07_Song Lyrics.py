# Chapter 5, Exercise 7: Song Lyrics

song_lyrics = {
    'Hello':'Hello, it\'s me.',
    'Eye of the Tiger':'It\'s the eye of the tiger.',
    'We Are The Champions':'We are the champions, my friends.',
    'Billie Jean':'Billie Jean is not my lover.',
    'Y.M.C.A':'It\'s fun to stay at the Y.M.C.A',
    'The Sound of Silence':'Hello darkness my old friend.'
}

# Outputs a popular song with its song lyrics
for key, value in song_lyrics.items(): 
    print(f"The song '{key}' includes: '{value}' \n") 