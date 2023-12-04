import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
random.seed(42)

neighborhoods = ['A', 'B', 'C', 'D', 'E']

data = {
    'Neighborhood': random.choices(neighborhoods, k=100),
    'Price': [random.randint(80, 150) for _ in range(100)],
    'Occupancy': [random.randint(50, 90) for _ in range(100)],
    'Review_Score': [round(random.uniform(3.5, 5.0), 1) for _ in range(100)]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
price_heatmap = df.pivot_table(index='Neighborhood', values='Price', aggfunc='mean').sort_values(by='Price', ascending=False)
sns.heatmap(price_heatmap, cmap='YlGnBu', annot=True, fmt=".2f", cbar_kws={'label': 'Preț mediu'})
plt.title('Hartă de căldură pentru prețuri în funcție de cartier')

plt.subplot(2, 1, 2)
occupancy_heatmap = df.pivot_table(index='Neighborhood', values='Occupancy', aggfunc='mean').sort_values(by='Occupancy', ascending=False)
sns.heatmap(occupancy_heatmap, cmap='YlGnBu', annot=True, cbar_kws={'label': 'Ocupare medie'})
plt.title('Hartă de căldură pentru ocupare în funcție de cartier')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Review_Score', y='Price', data=df, hue='Neighborhood', palette='viridis', alpha=0.7)
plt.title('Scatter plot pentru relația dintre prețuri și scorurile de recenzie')
plt.xlabel('Scor de recenzie')
plt.ylabel('Preț')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
