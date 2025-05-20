import csv
from  transformers  import  pipeline
import matplotlib.pyplot as plt
sentiment_pipeline = pipeline("sentiment-analysis", framework="pt",model="distilbert-base-uncased-finetuned-sst-2-english")
final=[]
pcount=0
ncount=0
with open('datascraped.csv') as f:
    reader= csv.reader(f)
    for rows in reader:
     
     res = sentiment_pipeline(rows)
     print(res)
     
     if res[0]['label']=="POSITIVE":
      pcount+=1
     if res[0]['label']=="NEGATIVE":
       ncount+=1
    
print(f"positive headlines  {pcount}")
print(f"negative headlines {ncount}")
labels = ['Positive', 'Negative']
counts = [pcount, ncount]

colors = ['#4CAF50', '#F44336']

plt.figure(figsize=(6, 4))
bars = plt.bar(labels, counts, color=colors)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(height), ha='center', fontsize=12)

plt.title('Sentiment Distribution of News Headlines')
plt.ylabel('Number of Headlines')
plt.ylim(0, max(counts) + 5)
plt.show()







