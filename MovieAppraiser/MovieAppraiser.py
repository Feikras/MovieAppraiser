
import pandas as pd
from IPython.display import HTML
from IPython.display import display

df = pd.read_csv('PopularMovies.csv')
df2 = df[df["Released_Year"] >=2000]


html = df2.to_html()
  
# write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
