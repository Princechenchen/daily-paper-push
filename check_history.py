import json
with open('F:/学习工作/千里之行始于足下/每周论文学习/papers_history.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(f"Total weeks in history: {len(data)}")
for h in data:
    print(f"  - {h['date']}: {len(h['main_papers'])} main, {len(h['supplementary'])} supp")
