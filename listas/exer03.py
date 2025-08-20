tecnologias = [
    {'nome': 'Python', 'tipo': 'linguagem'},
    {'nome': 'Django', 'tipo': 'framework'},
    {'nome': 'Flask', 'tipo': 'framework'},
    {'nome': 'Javascript', 'tipo': 'linguagem'},
    {'nome': 'React', 'tipo': 'framework'},
    {'nome': 'Vue.js', 'tipo': 'framework'},
    {'nome': 'Angular', 'tipo': 'framework'},
    {'nome': 'Java', 'tipo': 'linguagem'},
    {'nome': 'Spring Boot', 'tipo': 'framework'}
]
framework = []

for frame in tecnologias:
    if frame['tipo'].find('framework') != -1:
        framework.append(frame['nome'])

print("Frameworks encontrados:", framework)