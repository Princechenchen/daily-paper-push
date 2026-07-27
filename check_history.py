import json

data = json.load(open(r'F:/学习工作/千里之行始于足下/每周论文学习/papers_history.json', encoding='utf-8'))
print('总周数:', len(data))
for w in data:
    date = w['date']
    main = len(w.get('main_papers', []))
    supp = len(w.get('supplementary', []))
    print(f'  周次: {date}, 重点: {main}篇, 补充: {supp}篇')
print('最新周次:', data[-1]['date'])

# 检查格式问题
errors = 0
for i, w in enumerate(data):
    for j, p in enumerate(w.get('main_papers', [])):
        if isinstance(p.get('tags'), list):
            print(f'ERROR: Week {w["date"]} paper {j} tags is array')
            errors += 1
        if not isinstance(p.get('content'), list):
            print(f'ERROR: Week {w["date"]} paper {j} content not array')
            errors += 1
        if p.get('images') and any('/' in str(img) for img in p.get('images', [])):
            print(f'ERROR: Week {w["date"]} paper {j} images has path prefix')
            errors += 1
    for j, p in enumerate(w.get('supplementary', [])):
        if isinstance(p.get('tags'), list):
            print(f'ERROR: Week {w["date"]} supp {j} tags is array')
            errors += 1

print(f'格式错误总数: {errors}')
