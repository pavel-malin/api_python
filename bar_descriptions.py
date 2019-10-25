import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 44036, 'label': 'Description of flack.'},
    {'value': 41532, 'label': 'Description of django.'},
    {'value': 41137, 'label': 'Description of httpie.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
